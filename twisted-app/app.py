from scrapyd.config import Config
from scrapyd.eggstorage import FilesystemEggStorage
from scrapyd.environ import Environment
from scrapyd.interfaces import IEggStorage, IPoller, ISpiderScheduler, \
	IEnvironment
from scrapyd.launcher import Launcher
from scrapyd.poller import QueuePoller
from scrapyd.scheduler import SpiderScheduler
from scrapyd.website import Root
from twisted.application.internet import TimerService, TCPServer
from twisted.application.service import Application
from twisted.cred.checkers import FilePasswordDB
from twisted.cred.portal import IRealm, Portal
from twisted.python import log
from twisted.web import server
from twisted.web.guard import HTTPAuthSessionWrapper, BasicCredentialFactory, \
	DigestCredentialFactory
from twisted.web.resource import IResource
from twisted.web.static import File
from zope.interface import implements

from scrapyd.webservice import WsResource


class Procmon(WsResource):
	
	def render_GET(self, txrequest):
		processes = []
		for p in self.root.launcher.processes.values():
			processes.append({ 
				'project' : p.project,
				'spider' : p.spider,
				'job' : p.job,  
			})
		
		return {
			"status" : "ok", 
			"processes" : processes, 
		}


class LittleExtention(Root):
	
	def __init__(self, app, config):
		Root.__init__(self, app, config)
		
		self.putChild('procmon.json', Procmon(self))


class PublicHTMLRealm(object):
	implements(IRealm)
	
	def __init__(self, config, app):
		super(PublicHTMLRealm, self).__init__()
		
		self.config = config
		self.app = app

	def requestAvatar(self, avatarId, mind, *interfaces):
		if IResource in interfaces:
			return (IResource, LittleExtention(self.config, self.app), lambda: None)
		
		raise NotImplementedError()


def application(config):
	app = Application("Scrapyd")
	http_port = config.getint('http_port', 6800)
	
	portal = Portal(PublicHTMLRealm(config, app), [FilePasswordDB(str(config.get('passwd', '')))])
	credentialFactory = DigestCredentialFactory("md5", "Go away")
	
	poller = QueuePoller(config)
	eggstorage = FilesystemEggStorage(config)
	scheduler = SpiderScheduler(config)
	environment = Environment(config)
	
	app.setComponent(IPoller, poller)
	app.setComponent(IEggStorage, eggstorage)
	app.setComponent(ISpiderScheduler, scheduler)
	app.setComponent(IEnvironment, environment)
	
	launcher = Launcher(config, app)
	timer = TimerService(5, poller.poll)
	webservice = TCPServer(http_port, server.Site(HTTPAuthSessionWrapper(portal, [credentialFactory])))
	log.msg("Scrapyd web console available at http://localhost:%s/" % http_port)
	
	launcher.setServiceParent(app)
	timer.setServiceParent(app)
	webservice.setServiceParent(app)
	
	return app
