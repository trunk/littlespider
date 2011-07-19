import re

spiders = (
		# test spider for localhost
		{
			'name' : 'localspider',
			'domain' : '127.0.0.1',  
			'allowed_domains' : [ '127.0.0.1' ],  
			'start_urls' : [ 'http://127.0.0.1' ], 
			'process' : (
					re.compile(ur'.*/samples/.*\.htm[l]?$', re.IGNORECASE | re.UNICODE), 
				), 
			'allow' : (
				), 
			'disallow' : (
				), 
		}, 
		
		# lenta.ru spider
		# processing printable versions of news
		{
			'domain' : 'lenta.ru', 
			'allowed_domains' : [ 'lenta.ru' ], 
			'start_urls' : [ 'http://lenta.ru' ], 
			'process' : (
					re.compile(ur'.*/_Printed.htm[l]?$', re.UNICODE | re.IGNORECASE), 
				),
			'allow' : (
					re.compile(ur'^http://lenta.ru/.*', re.UNICODE | re.IGNORECASE),
					re.compile(ur'^http://www.lenta.ru/.*', re.UNICODE | re.IGNORECASE),
				), 
#			'disallow' : (
#					re.compile(ur'.*pda\.lenta.*', re.UNICODE | re.IGNORECASE),
#					re.compile(ur'.*orsn\.lenta.*', re.UNICODE | re.IGNORECASE),
#					re.compile(ur'.*readers\.lenta.*', re.UNICODE | re.IGNORECASE), 
#				), 
		},
		
		# rusrep.ru spider
		# processing printable versions of articles
		{
			'domain' : 'rusrep.ru', 
			'allowed_domains' : [ 'rusrep.ru' ], 
			'start_urls' : [ 'http://rusrep.ru' ], 
			'process' : (
					re.compile(ur'.*/print/\d+/$', re.UNICODE | re.IGNORECASE), 
				),
			'allow' : (
					re.compile(ur'^http://rusrep.ru/.*', re.UNICODE | re.IGNORECASE),
					re.compile(ur'^http://www.rusrep.ru/.*', re.UNICODE | re.IGNORECASE),
				), 
			'disallow' : (
					re.compile(ur'/photo', re.UNICODE | re.IGNORECASE),
				), 
		},
		
		# gzt.ru spider
		# processing printable versions of news
		# from robots.txt: Disallow: /print*
#		{
#			'domain' : 'gzt.ru', 
#			'allowed_domains' : [ 'gzt.ru' ], 
#			'start_urls' : [ 'http://gzt.ru' ], 
#			'process' : (
#					re.compile(ur'.*/print/\d+\.html/$', re.UNICODE | re.IGNORECASE), 
#				),
#			'allow' : (
#					re.compile(ur'^http://gzt.ru/.*', re.UNICODE | re.IGNORECASE),
#					re.compile(ur'^http://www.gzt.ru/.*', re.UNICODE | re.IGNORECASE),
#				), 
#			'disallow' : (
#					re.compile(ur'.*/multimedia/.*', re.UNICODE | re.IGNORECASE),
#					re.compile(ur'.*/video/.*', re.UNICODE | re.IGNORECASE),
#					re.compile(ur'.*/picture/.*', re.UNICODE | re.IGNORECASE),
#					re.compile(ur'.*/photo/.*', re.UNICODE | re.IGNORECASE),
#					re.compile(ur'.*/livecity/.*', re.UNICODE | re.IGNORECASE),
#				), 
#		},
		
		# interfax.ru spider
		# processing printable versions of news
		{
			'domain' : 'interfax.ru', 
			'allowed_domains' : [ 'interfax.ru' ], 
			'start_urls' : [ 'http://interfax.ru' ], 
			'process' : (
					re.compile(ur'.*/print.asp\?.*$', re.UNICODE | re.IGNORECASE), 
				),
			'allow' : (
					re.compile(ur'^http://interfax.ru/.*', re.UNICODE | re.IGNORECASE),
					re.compile(ur'^http://www.interfax.ru/.*', re.UNICODE | re.IGNORECASE),
				), 
			'disallow' : (
					re.compile(ur'/realty', re.UNICODE | re.IGNORECASE),
					re.compile(ur'/tourism', re.UNICODE | re.IGNORECASE),
				), 
		},
		
		# ru.reuters.com spider
		# processing printable versions of news
		{
			'domain' : 'ru.reuters.com', 
			'allowed_domains' : [ 'ru.reuters.com' ], 
			'start_urls' : [ 'http://ru.reuters.com' ], 
			'process' : (
					re.compile(ur'.*/articlePrint\?.*$', re.UNICODE | re.IGNORECASE), 
				),
			'allow' : (
					re.compile(ur'^http://ru.reuters.com/.*', re.UNICODE | re.IGNORECASE),
					re.compile(ur'^http://www.ru.reuters.com/.*', re.UNICODE | re.IGNORECASE),
				), 
			'disallow' : (
				), 
		},
		
		# kommersant.ru spider
		# processing printable versions of articles
		{
			'domain' : 'kommersant.ru', 
			'allowed_domains' : [ 'kommersant.ru' ], 
			'start_urls' : [ 'http://kommersant.ru' ], 
			'process' : (
					re.compile(ur'.*/Print$', re.UNICODE | re.IGNORECASE), 
				),
			'allow' : (
					re.compile(ur'^http://kommersant.ru/.*', re.UNICODE | re.IGNORECASE),
					re.compile(ur'^http://www.kommersant.ru/.*', re.UNICODE | re.IGNORECASE),
				), 
			'disallow' : (
					re.compile(ur'/photo', re.UNICODE | re.IGNORECASE),
					re.compile(ur'/video', re.UNICODE | re.IGNORECASE),
					re.compile(ur'/library', re.UNICODE | re.IGNORECASE),
				), 
		},
		
		# rian.ru spider
		# processing printable versions of news
		# from robots.txt: Disallow: *-print.html$
#		{
#			'domain' : 'rian.ru', 
#			'allowed_domains' : [ 'rian.ru' ], 
#			'start_urls' : [ 'http://rian.ru' ], 
#			'process' : (
#					re.compile(ur'.*-print\.html', re.UNICODE | re.IGNORECASE), 
#				),
#			'allow' : (
#					re.compile(ur'^http://rian.ru/.*', re.UNICODE | re.IGNORECASE),
#					re.compile(ur'^http://www.rian.ru/.*', re.UNICODE | re.IGNORECASE),
#				), 
#			'disallow' : (
#					re.compile(ur'.*/game/.*', re.UNICODE | re.IGNORECASE),
#					re.compile(ur'.*/loop/.*', re.UNICODE | re.IGNORECASE),
#					re.compile(ur'.*/infografika/.*', re.UNICODE | re.IGNORECASE),
#				), 
#		},
		
		# vedomosti.ru spider
		# processing printable versions of articles
		# from robots.txt: Disallow: /politics/print/, etc
#		{
#			'domain' : 'vedomosti.ru', 
#			'allowed_domains' : [ 'vedomosti.ru' ], 
#			'start_urls' : [ 'http://vedomosti.ru' ], 
#			'process' : (
#					re.compile(ur'.*/print/.*', re.UNICODE | re.IGNORECASE), 
#				),
#			'allow' : (
#					re.compile(ur'^http://vedomosti.ru/.*', re.UNICODE | re.IGNORECASE),
#					re.compile(ur'^http://www.vedomosti.ru/.*', re.UNICODE | re.IGNORECASE),
#					re.compile(ur'^http://old.vedomosti.ru/.*', re.UNICODE | re.IGNORECASE),
#					re.compile(ur'^http://www.old.vedomosti.ru/.*', re.UNICODE | re.IGNORECASE),
#				), 
#			'disallow' : (
#					re.compile(ur'.*/realty/.*', re.UNICODE | re.IGNORECASE),
#					re.compile(ur'.*/tnews/.*', re.UNICODE | re.IGNORECASE),
#					re.compile(ur'.*/wine/.*', re.UNICODE | re.IGNORECASE),
#					re.compile(ur'.*/ad/.*', re.UNICODE | re.IGNORECASE),
#					re.compile(ur'.*/timeline/.*', re.UNICODE | re.IGNORECASE),
#					re.compile(ur'.*/photogallery/.*', re.UNICODE | re.IGNORECASE),
#					re.compile(ur'.*/smartmoney/.*', re.UNICODE | re.IGNORECASE),
#					re.compile(ur'.*/guide/.*', re.UNICODE | re.IGNORECASE),
#				), 
#		},
		
		# kp.ru spider
		# from robots.txt: Disallow: /print/
#		{
#			'domain' : 'kp.ru',  
#			'allowed_domains' : [ 'kp.ru' ],  
#			'start_urls' : [ 'http://kp.ru' ], 
#			'process' : (
#					re.compile(ur'.*/print/', re.IGNORECASE | re.UNICODE), 
#					re.compile(ur'.*/print$', re.IGNORECASE | re.UNICODE), 
#				), 
#			'allow' : (
#					re.compile(ur'^http://kp.ru/.*', re.IGNORECASE | re.UNICODE), 
#					re.compile(ur'^http://www.kp.ru/.*', re.IGNORECASE | re.UNICODE), 
#				), 
#			'disallow' : (
#					re.compile(ur'.*/afisha/.*', re.IGNORECASE | re.UNICODE), 
#					re.compile(ur'.*/classfieds/.*', re.IGNORECASE | re.UNICODE), 
#					re.compile(ur'.*/bigbook/.*', re.IGNORECASE | re.UNICODE), 
#					re.compile(ur'.*/summer/.*', re.IGNORECASE | re.UNICODE),
#					re.compile(ur'.*/radio/.*', re.IGNORECASE | re.UNICODE),
#					re.compile(ur'.*/mydacha/.*', re.IGNORECASE | re.UNICODE),
#					re.compile(ur'.*/mama/.*', re.IGNORECASE | re.UNICODE),
#					re.compile(ur'.*/rest/.*', re.IGNORECASE | re.UNICODE),
#					re.compile(ur'.*/digital/.*', re.IGNORECASE | re.UNICODE),
#					re.compile(ur'.*/club/.*', re.IGNORECASE | re.UNICODE), 
#					re.compile(ur'.*/video/.*', re.IGNORECASE | re.UNICODE), 
#					re.compile(ur'.*/valio2011/.*', re.IGNORECASE | re.UNICODE), 
#					re.compile(ur'.*/health/.*', re.IGNORECASE | re.UNICODE), 
#					re.compile(ur'.*/tv/.*', re.IGNORECASE | re.UNICODE), 
#				), 
#		},
		
		# vz.ru spider
		# from robots.txt: Disallow: /print.html
#		{
#			'domain' : 'vz.ru',  
#			'allowed_domains' : [ 'vz.ru' ],  
#			'start_urls' : [ 'http://vz.ru' ], 
#			'process' : (
#					re.compile(ur'.*\.print\.html$', re.IGNORECASE | re.UNICODE), 
#				), 
#			'allow' : (
#					re.compile(ur'^http://vz.ru/.*', re.IGNORECASE | re.UNICODE),
#					re.compile(ur'^http://www.vz.ru/.*', re.IGNORECASE | re.UNICODE),
#				), 
#			'disallow' : (
#					re.compile(ur'.*/photoreport/.*', re.IGNORECASE | re.UNICODE), 
#					re.compile(ur'.*/vote/.*', re.IGNORECASE | re.UNICODE), 
#				), 
#		},
		
		# ura.ru spider
		# from robots.txt: Disallow: /print
#		{
#			'name' : 'ura.ru',
#			'domain' : 'ura.ru',  
#			'allowed_domains' : [ 'ura.ru' ],  
#			'start_urls' : [ 'http://ura.ru' ], 
#			'process' : (
#					re.compile(ur'.*/print/.*', re.IGNORECASE | re.UNICODE), 
#				), 
#			'allow' : (
#					re.compile(ur'^http://ura.ru/.*', re.IGNORECASE | re.UNICODE), 
#					re.compile(ur'^http://www.ura.ru/.*', re.IGNORECASE | re.UNICODE), 
#				), 
#			'disallow' : (
#				), 
#		}, 

		# forbes.ru spider
		{
			'domain' : 'forbes.ru',  
			'allowed_domains' : [ 'forbes.ru' ],  
			'start_urls' : [ 'http://forbes.ru' ], 
			'process' : (
					re.compile(ur'.*/print$', re.IGNORECASE | re.UNICODE), 
				), 
			'allow' : (
					re.compile(ur'^http://forbes.ru/.*', re.IGNORECASE | re.UNICODE), 
					re.compile(ur'^http://www.forbes.ru/.*', re.IGNORECASE | re.UNICODE), 
				), 
			'disallow' : (
					re.compile(ur'/stil-zhizni', re.IGNORECASE | re.UNICODE),
					re.compile(ur'/forbes-woman', re.IGNORECASE | re.UNICODE),
					re.compile(ur'/tehno', re.IGNORECASE | re.UNICODE),
					re.compile(ur'/lichnye-dengi', re.IGNORECASE | re.UNICODE),
					re.compile(ur'/karera', re.IGNORECASE | re.UNICODE),
					re.compile(ur'/guide', re.IGNORECASE | re.UNICODE),
				), 
		},
		
		# newru.com spider
		{
			'domain' : 'newsru.com',  
			'allowed_domains' : [ 'newsru.com' ],  
			'start_urls' : [ 'http://newsru.com' ], 
			'process' : (
					re.compile(ur'.*_print.html$', re.IGNORECASE | re.UNICODE), 
				), 
			'allow' : (
					re.compile(ur'^http://newsru.com/.*', re.IGNORECASE | re.UNICODE), 
					re.compile(ur'^http://www.newsru.com/.*', re.IGNORECASE | re.UNICODE), 
				), 
			'disallow' : (
				), 
		}, 
		
		# echo.msk.ru spider
		{
			'domain' : 'echo.msk.ru',  
			'allowed_domains' : [ 'echo.msk.ru' ],  
			'start_urls' : [ 'http://echo.msk.ru' ], 
			'process' : (
					re.compile(ur'.*\.phtml$', re.IGNORECASE | re.UNICODE), 
				), 
			'allow' : (
					re.compile(ur'^http://echo.msk.ru/.*', re.IGNORECASE | re.UNICODE), 
					re.compile(ur'^http://www.echo.msk.ru/.*', re.IGNORECASE | re.UNICODE),
				), 
			'disallow' : (
					re.compile(ur'/tag', re.IGNORECASE | re.UNICODE),
					re.compile(ur'/top', re.IGNORECASE | re.UNICODE),
					re.compile(ur'/polls', re.IGNORECASE | re.UNICODE),
					re.compile(ur'/schedule', re.IGNORECASE | re.UNICODE),
					re.compile(ur'/log', re.IGNORECASE | re.UNICODE),
					re.compile(ur'/news', re.IGNORECASE | re.UNICODE),
					re.compile(ur'/doc', re.IGNORECASE | re.UNICODE),
				), 
		}, 
		
		# newtimes.ru spider
		{
			'domain' : 'newtimes.ru',  
			'allowed_domains' : [ 'newtimes.ru' ],  
			'start_urls' : [ 'http://newtimes.ru' ], 
			'process' : (
					re.compile(ur'.*/print/.*', re.IGNORECASE | re.UNICODE), 
				), 
			'allow' : (
					re.compile(ur'^http://newtimes.ru/.*', re.IGNORECASE | re.UNICODE), 
					re.compile(ur'^http://www.newtimes.ru/.*', re.IGNORECASE | re.UNICODE),
				), 
			'disallow' : (
					re.compile(ur'/media', re.IGNORECASE | re.UNICODE),
					re.compile(ur'/forum', re.IGNORECASE | re.UNICODE),
					re.compile(ur'/shop', re.IGNORECASE | re.UNICODE),
					re.compile(ur'/login', re.IGNORECASE | re.UNICODE),
				), 
		}, 
)
