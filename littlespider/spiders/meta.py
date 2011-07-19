from littlebrother.crawling import gather
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
import config
import time

default_dd = 1 # download delay


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


def callback(self, response):
	'''Callback for data extraction'''
	
	content_type = response.headers.get('Content-Type', None)
	
	if 'text/html' not in content_type:
		return
	
	if not self.processable(unicode(response.url)):
		return
	
	print '>>> processing', response.url
	start = time.time()
	gather.gather(unicode(response.url), response.body)
	stop = time.time()
	print '<<< processing time:', stop - start


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
		
		spider_class.DOWNLOAD_DELAY = default_dd
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

# TODO: this need testing
