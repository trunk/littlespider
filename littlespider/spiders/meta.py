from littlebrother.crawling import gather
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
import config
import logging
import md5
import os
import shutil
import time
import urlparse
import uuid

DEFAULT_DD = 1  # download delay
ENCODING = 'UTF-8'


def processable(self, url):
	'''Return true if url fits 'process' pattern in spider's config'''

	if not self.process:
		return True

	matches_filter = False
	for filter in self.process:
		if filter.match(url):
			matches_filter = True
			break

	return matches_filter


def process_links(self, links):
	'''
	Return list of links suitable for crawling.
	It depends on 'allow' and 'disallow' args in spider's config
	'''

	if not self.allow and not self.disallow:
		return links

	pass_links = []
	for link in links:
		pass_it = True

		if self.allow:
			allow = False
			for filter in self.allow:
				if filter.match(link.url):
					allow = True
					break
			pass_it = allow

		if pass_it:
			for filter in self.disallow:
				if filter.match(link.url):
					pass_it = False
					break

		if pass_it:
			pass_links.append(link)
#		else:
#			print '!!! filtering', link.url

	return pass_links


def index_dir(basedir = config.index.get('basedir', 'index')):
	return basedir


def render(url, title, identities):
	netloc = urlparse.urlparse(url).netloc
	index = os.path.join(index_dir(), netloc)
	if not os.path.isdir(index):
		try:
			os.makedirs(index)
		except OSError, e:
			if e.errno != 17:
				raise  # meh

	filename = md5.md5(url).hexdigest()
	filename = os.path.join(index, filename)
	logging.info('rendering "%s" to "%s"' % (url, filename))

	try:
		fp = open(filename, 'wt')
		print >> fp, url.encode(ENCODING)
		print >> fp, title.encode(ENCODING)
		for ident, xpath, tag in identities:
			print >> fp, tag.encode(ENCODING)
			print >> fp, ident.encode(ENCODING)
			print >> fp, xpath.encode(ENCODING)
	except Exception, e:
		logging.exception(e)


def callback(self, response):
	'''Callback for data extraction'''

	content_type = response.headers.get('Content-Type', None)

	if 'text/html' not in content_type:
		return

	if not self.processable(unicode(response.url)):
		return

	logging.info('processing %s' % (response.url))
	start = time.time()
	url = unicode(response.url)
	title, identities = gather.extract(response.body)
	render(url, title, identities)
	stop = time.time()
	logging.info('processing time: %d' % (stop - start))


def construct_spiders():
	'''Create all spiders described in config'''

	for index, spider in enumerate(config.spiders):
		crawler_class_name = 'Spider' + str(index)
		spider_class = type(crawler_class_name, (CrawlSpider,),
			{
				'callback' : callback,
				'process_links' : process_links,
				'processable' : processable,
			}
		)

		spider_class.download_delay = DEFAULT_DD
		spider_class.domain = spider['domain']
		spider_class.name = spider.get('name', spider_class.domain + '_spider')
		spider_class.start_urls = spider.get('start_urls', [ 'http://' + spider_class.domain ])
		spider_class.allowed_domains = spider.get('allowed_domains', [ spider_class.domain ])
		spider_class.process = spider.get('process', ())
		spider_class.allow = spider.get('allow', ())
		spider_class.disallow = spider.get('disallow', ())
		spider_class.rules = (
			Rule(SgmlLinkExtractor(allow_domains = spider_class.allowed_domains)
				, callback = 'callback'
				, process_links = 'process_links'
				, follow = True
			),
		)

		globals()[crawler_class_name] = spider_class


# yeah
# scrapy is looking for classes imported from module
# so create a class for each spider in config
# triggered on import
construct_spiders()

if __name__ == '__main__':
	import unittest

	class RenderTest(unittest.TestCase):
		def setUp(self):
			try:
				shutil.rmtree(index_dir())
			except OSError, e:
				if e.errno != 2:
					raise

		def tearDown(self):
			self.setUp()

		def testIt(self):
			url = 'http://example.com/page?number=42'
			directory = os.path.join(index_dir(), 'example.com')
			self.assertFalse(os.path.isdir(directory))
			render(url, 'sup', [('ident1 ident1', 'xpath1', 'tag1'), ('ident2 ident2', 'xpath2', 'tag2')])
			self.assertTrue(os.path.isdir(directory))

	unittest.main()
