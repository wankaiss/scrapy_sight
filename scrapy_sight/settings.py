# -*- coding: utf-8 -*-

# Scrapy settings for sight project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrapy_sight.spiders'

SPIDER_MODULES = ['scrapy_sight.spiders']
NEWSPIDER_MODULE = 'scrapy_sight.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'sight (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 5
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

SPLASH_URL = 'http://172.26.30.78:8050'

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'sight.middlewares.SightSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # 'sight.middlewares.MyCustomDownloaderMiddleware': 543,
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
    'scrapy_sight.spiders.rotate_useragent.RotateUserAgentMiddleware': 400,
    'scrapyjs.SplashMiddleware': 725,  # render html for crawl user splash
    # 'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110, # proxy use only
    # 'scrapy_sight.middlewares.ProxyMiddleware': 100,  # proxy use only
    # 'scrapy_splash.SplashCookiesMiddleware': 723,  # render html with scrapy_splash
    # 'scrapy_splash.SplashMiddleware': 725,  # render html with scrapy_splash
    # 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,  # render html with scrapy_splash

}

# render html about js content with scrapyjs
DUPEFILTER_CLASS = 'scrapyjs.SplashAwareDupeFilter'

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'sight.pipelines.SightPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

PROXIES = [
    {"ip_port": "27.38.137.65:8118", "user_pass": ""},
    {"ip_port": "110.250.77.228:8118", "user_pass": ""},
    {"ip_port": "124.89.33.75:9999", "user_pass": ""},
    {"ip_port": "123.138.89.133:9999", "user_pass": ""},
    {"ip_port": "125.45.87.12:9999", "user_pass": ""},
    {"ip_port": "111.194.93.155:9999", "user_pass": ""},
    {"ip_port": "101.200.44.5:8888", "user_pass": ""},
    {"ip_port": "61.143.228.162:3128", "user_pass": ""},
    {"ip_port": "117.9.135.72:9999", "user_pass": ""},
    {"ip_port": "120.76.47.120:3128", "user_pass": ""},
    {"ip_port": "220.248.36.57:9080", "user_pass": ""},
    {"ip_port": "123.207.30.187:3128", "user_pass": ""},
    {"ip_port": "122.72.32.93:80", "user_pass": ""},
    {"ip_port": "219.141.189.236:3128", "user_pass": ""},
    {"ip_port": "180.168.179.193:8080", "user_pass": ""},
    {"ip_port": "122.72.32.75:80", "user_pass": ""},
    {"ip_port": "61.163.39.70:9999", "user_pass": ""},
    {"ip_port": "42.202.130.246:3128", "user_pass": ""},
    {"ip_port": "27.215.7.230:9999", "user_pass": ""},
    {"ip_port": "175.18.53.101:80", "user_pass": ""},
    {"ip_port": "183.66.64.120:3128", "user_pass": ""},
    {"ip_port": "1.196.161.124:9999", "user_pass": ""},
    {"ip_port": "1.119.193.36:8080", "user_pass": ""},
    {"ip_port": "59.39.129.188:9000", "user_pass": ""},
    {"ip_port": "120.84.160.210:9797", "user_pass": ""},
    {"ip_port": "218.56.132.155:8080", "user_pass": ""},
    {"ip_port": "113.200.159.155:9999", "user_pass": ""},
    {"ip_port": "125.33.165.58:9000", "user_pass": ""},
    {"ip_port": "115.59.111.207:9999", "user_pass": ""},
    {"ip_port": "118.178.124.33:3128", "user_pass": ""},
    {"ip_port": "119.190.125.11:9999", "user_pass": ""},
    {"ip_port": "114.252.223.132:9999", "user_pass": ""},
    {"ip_port": "61.141.186.159:9797", "user_pass": ""},
    {"ip_port": "222.52.142.242:8080", "user_pass": ""},
    {"ip_port": "113.97.232.94:9999", "user_pass": ""},
    {"ip_port": "116.30.192.16:3128", "user_pass": ""},
    {"ip_port": "183.56.177.130:808", "user_pass": ""},
    {"ip_port": "58.59.68.91:9797", "user_pass": ""},
    {"ip_port": "122.7.226.126:8888", "user_pass": ""},
    {"ip_port": "218.29.111.106:9999", "user_pass": ""},
    {"ip_port": "14.117.210.193:9797", "user_pass": ""},
    {"ip_port": "183.30.197.69:9797", "user_pass": ""},
    {"ip_port": "221.217.29.80:9000", "user_pass": ""},
    {"ip_port": "119.53.106.124:9000", "user_pass": ""},
    {"ip_port": "163.125.182.89:9999", "user_pass": ""},
    {"ip_port": "123.115.161.245:9000", "user_pass": ""},
    {"ip_port": "123.117.81.7:53281", "user_pass": ""},
    {"ip_port": "124.88.84.154:8080", "user_pass": ""},
    {"ip_port": "219.154.122.132:9000", "user_pass": ""},
    {"ip_port": "112.86.199.198:8123", "user_pass": ""},
    {"ip_port": "114.240.197.187:9797", "user_pass": ""},
    {"ip_port": "163.125.180.205:9797", "user_pass": ""},
    {"ip_port": "222.73.85.77:8090", "user_pass": ""},
    {"ip_port": "119.90.63.3:3128", "user_pass": ""},
    {"ip_port": "14.211.9.72:9797", "user_pass": ""},
    {"ip_port": "183.45.173.84:9797", "user_pass": ""},
    {"ip_port": "218.75.116.58:9999", "user_pass": ""},
    {"ip_port": "124.239.177.85:8080", "user_pass": ""},
    {"ip_port": "163.125.126.187:9797", "user_pass": ""},
    {"ip_port": "61.191.61.139:8000", "user_pass": ""},
    {"ip_port": "220.198.98.116:9797", "user_pass": ""},
    {"ip_port": "114.115.210.154:3128", "user_pass": ""},
    {"ip_port": "14.119.209.205:808", "user_pass": ""},
    {"ip_port": "113.94.8.135:9797", "user_pass": ""},
    {"ip_port": "218.20.55.150:9797", "user_pass": ""},
    {"ip_port": "118.188.20.162:8080", "user_pass": ""},
    {"ip_port": "123.172.197.62:80", "user_pass": ""},
    {"ip_port": "183.12.14.40:9797", "user_pass": ""},
    {"ip_port": "60.214.19.217:9999", "user_pass": ""},
    {"ip_port": "59.39.128.241:9000", "user_pass": ""},
    {"ip_port": "222.247.69.41:8888", "user_pass": ""},
    {"ip_port": "121.42.151.5:3128", "user_pass": ""},
    {"ip_port": "14.29.92.196:80", "user_pass": ""},
    {"ip_port": "180.105.183.215:9999", "user_pass": ""},
    {"ip_port": "113.97.54.48:9000", "user_pass": ""},
    {"ip_port": "59.32.153.237:9000", "user_pass": ""},
    {"ip_port": "14.153.55.129:3128", "user_pass": ""},
    {"ip_port": "59.38.61.215:9797", "user_pass": ""},
    {"ip_port": "116.23.138.110:9999", "user_pass": ""},
    {"ip_port": "115.209.15.189:9999", "user_pass": ""},
    {"ip_port": "183.30.197.184:9999", "user_pass": ""},
    {"ip_port": "113.83.242.22:8088", "user_pass": ""},
    {"ip_port": "106.75.29.63:8118", "user_pass": ""},
    {"ip_port": "116.25.102.165:9797", "user_pass": ""},
    {"ip_port": "121.12.185.133:9797", "user_pass": ""},
    {"ip_port": "183.152.50.207:8118", "user_pass": ""},
    {"ip_port": "123.7.38.31:9999", "user_pass": ""},
    {"ip_port": "14.144.221.151:9999", "user_pass": ""},
    {"ip_port": "49.88.251.238:9999", "user_pass": ""},
    {"ip_port": "120.25.154.32:8080", "user_pass": ""},
    {"ip_port": "180.173.183.255:53281", "user_pass": ""},
    {"ip_port": "110.73.0.223:80", "user_pass": ""},
    {"ip_port": "14.153.52.153:3128", "user_pass": ""},
    {"ip_port": "218.6.145.11:9797", "user_pass": ""},
    {"ip_port": "14.124.116.161:9797", "user_pass": ""},
    {"ip_port": "61.136.79.240:9000", "user_pass": ""},
    {"ip_port": "113.102.213.48:9999", "user_pass": ""},
    {"ip_port": "182.245.197.108:9999", "user_pass": ""},
    {"ip_port": "116.52.52.162:9999", "user_pass": ""},
    {"ip_port": "14.211.32.196:9999", "user_pass": ""},
]

# Every page has 20 data
PAGE_NUM = u'3'
