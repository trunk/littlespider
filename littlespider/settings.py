# Scrapy settings for littlespider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
# Or you can copy and paste them from where they're defined in Scrapy:
#
#     scrapy/conf/default_settings.py
#

BOT_NAME = 'littlespider'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['littlespider.spiders']
NEWSPIDER_MODULE = 'littlespider.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

EXTENSIONS_BASE = {
#	'scrapy.contrib.corestats.CoreStats': 0,
#	'scrapy.webservice.WebService': 0,
	'scrapy.telnet.TelnetConsole': 0,
#	'scrapy.contrib.memusage.MemoryUsage': 0,
#	'scrapy.contrib.memdebug.MemoryDebugger': 0,
}

DOWNLOADER_MIDDLEWARES = {
	'scrapy.contrib.downloadermiddleware.robotstxt.RobotsTxtMiddleware' : 500,
	'scrapy.contrib.downloadermiddleware.redirect.RedirectMiddleware' : 501,
	'scrapy.contrib.spidermiddleware.offsite.OffsiteMiddleware' : 502,
#	'scrapy.contrib.downloadermiddleware.httpcompression.HttpCompressionMiddleware' : 503,
	'scrapy.contrib.downloadermiddleware.downloadtimeout.DownloadTimeoutMiddleware' : 504,
}

SPIDER_MIDDLEWARES = {
	'scrapy.contrib.spidermiddleware.depth.DepthMiddleware' : 500,
}

ROBOTSTXT_OBEY = True
REDIRECT_MAX_TIMES = 2

LOG_LEVEL = 'INFO'
#LOG_LEVEL = 'DEBUG'
DEPTH_LIMIT = 5  # need HUGE amount of memory if no depth limit

SCHEDULER_ORDER = 'DFO'  # should use less memory
#SCHEDULER_ORDER = 'BFO'

WEBSERVICE_ENABLED = False
TELNETCONSOLE_HOST = '127.0.0.1'

TRACK_REFS = True  # for the debugging or something
