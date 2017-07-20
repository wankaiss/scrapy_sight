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
    {'ip_port': '127.0.0.1:1080', 'user_pass': ''},
    {'ip_port': '119.23.129.24:3128', 'user_pass': ''},
    {'ip_port': '61.143.228.162:3128', 'user_pass': ''},
    {'ip_port': '118.178.124.33:3128', 'user_pass': ''},
    {'ip_port': '119.90.63.3:3128', 'user_pass': ''},
    {'ip_port': '139.215.214.61:8080', 'user_pass': ''},
    {'ip_port': '113.108.141.98:9797', 'user_pass': ''},
    {'ip_port': '183.185.209.18:9797', 'user_pass': ''},
    {'ip_port': '222.52.142.242:8080', 'user_pass': ''},
    {'ip_port': '120.69.83.21:8088', 'user_pass': ''},
    {'ip_port': '221.221.213.231:9999', 'user_pass': ''},
    {'ip_port': '58.59.68.91:9797', 'user_pass': ''},
    {'ip_port': '124.93.49.7:8080', 'user_pass': ''},
    {'ip_port': '221.206.5.183:53281', 'user_pass': ''},
    {'ip_port': '61.152.81.193:9100', 'user_pass': ''},
    {'ip_port': '60.174.237.43:9999', 'user_pass': ''},
    {'ip_port': '1.196.161.124:9999', 'user_pass': ''},
    {'ip_port': '113.74.115.15:9797', 'user_pass': ''},
    {'ip_port': '119.90.248.245:9999', 'user_pass': ''},
    {'ip_port': '58.56.92.18:8888', 'user_pass': ''},
    {'ip_port': '27.46.32.84:9797', 'user_pass': ''},
    {'ip_port': '180.140.165.141:9999', 'user_pass': ''},
    {'ip_port': '114.115.218.40:3128', 'user_pass': ''},
    {'ip_port': '111.195.70.246:8123', 'user_pass': ''},
    {'ip_port': '101.66.199.173:80', 'user_pass': ''},
    {'ip_port': '61.159.209.97:9999', 'user_pass': ''},
    {'ip_port': '182.44.148.80:9000', 'user_pass': ''},
    {'ip_port': '218.6.145.11:9797', 'user_pass': ''},
    {'ip_port': '116.22.104.20:9797', 'user_pass': ''},
    {'ip_port': '162.105.17.69:8118', 'user_pass': ''},
    {'ip_port': '222.132.145.122:53281', 'user_pass': ''},
    {'ip_port': '124.239.177.85:8080', 'user_pass': ''},
    {'ip_port': '114.115.210.154:3128', 'user_pass': ''},
    {'ip_port': '113.79.75.153:9797', 'user_pass': ''},
    {'ip_port': '210.44.213.63:1080', 'user_pass': ''},
    {'ip_port': '125.88.25.223:808', 'user_pass': ''},
    {'ip_port': '221.205.110.229:9797', 'user_pass': ''},
    {'ip_port': '125.33.243.203:9000', 'user_pass': ''},
    {'ip_port': '123.138.216.90:9999', 'user_pass': ''},
    {'ip_port': '112.243.115.51:9999', 'user_pass': ''},
    {'ip_port': '101.5.177.62:8123', 'user_pass': ''},
    {'ip_port': '125.45.87.12:9999', 'user_pass': ''},
    {'ip_port': '163.125.19.61:8888', 'user_pass': ''},
    {'ip_port': '61.52.157.100:53281', 'user_pass': ''},
    {'ip_port': '163.125.18.48:8888', 'user_pass': ''},
    {'ip_port': '60.9.173.129:9000', 'user_pass': ''},
    {'ip_port': '163.125.19.51:8888', 'user_pass': ''},
    {'ip_port': '113.92.35.217:9000', 'user_pass': ''},
    {'ip_port': '60.9.173.155:9000', 'user_pass': ''},
    {'ip_port': '123.123.141.241:9000', 'user_pass': ''},
    {'ip_port': '58.250.92.155:9000', 'user_pass': ''},
    {'ip_port': '14.211.122.157:9797', 'user_pass': ''},
    {'ip_port': '180.170.237.40:9000', 'user_pass': ''},
    {'ip_port': '60.10.218.49:9000', 'user_pass': ''},
    {'ip_port': '124.193.85.88:8080', 'user_pass': ''},
    {'ip_port': '118.119.168.172:9999', 'user_pass': ''},
    {'ip_port': '180.97.235.30:80', 'user_pass': ''},
    {'ip_port': '49.88.219.61:9999', 'user_pass': ''},
    {'ip_port': '121.69.3.102:8080', 'user_pass': ''},
    {'ip_port': '175.167.22.208:8080', 'user_pass': ''},
    {'ip_port': '121.31.102.127:80', 'user_pass': ''},
    {'ip_port': '119.123.179.160:9000', 'user_pass': ''},
    {'ip_port': '218.56.132.154:8080', 'user_pass': ''},
    {'ip_port': '183.56.177.130:808', 'user_pass': ''},
    {'ip_port': '163.125.200.247:9000', 'user_pass': ''},
    {'ip_port': '119.36.92.41:80', 'user_pass': ''},
    {'ip_port': '60.28.39.226:8080', 'user_pass': ''},
    {'ip_port': '14.211.123.218:9797', 'user_pass': ''},
    {'ip_port': '183.184.113.151:9797', 'user_pass': ''},
    {'ip_port': '180.76.134.106:3128', 'user_pass': ''},
    {'ip_port': '180.169.59.222:8080', 'user_pass': ''},
    {'ip_port': '101.251.234.254:51238', 'user_pass': ''},
    {'ip_port': '115.183.11.158:9999', 'user_pass': ''},
    {'ip_port': '123.207.159.149:3128', 'user_pass': ''},
    {'ip_port': '60.13.31.160:7895', 'user_pass': ''},
    {'ip_port': '124.152.5.205:7895', 'user_pass': ''},
    {'ip_port': '183.39.157.20:9797', 'user_pass': ''},
    {'ip_port': '183.14.79.136:9797', 'user_pass': ''},
    {'ip_port': '61.183.71.66:808', 'user_pass': ''},
    {'ip_port': '27.46.37.235:9797', 'user_pass': ''},
    {'ip_port': '42.196.254.7:8080', 'user_pass': ''},
    {'ip_port': '116.62.233.76:3128', 'user_pass': ''},
    {'ip_port': '58.61.4.34:9797', 'user_pass': ''},
    {'ip_port': '218.56.132.157:8080', 'user_pass': ''},
    {'ip_port': '218.75.144.25:9000', 'user_pass': ''},
    {'ip_port': '218.56.132.156:8080', 'user_pass': ''},
    {'ip_port': '123.101.163.44:9000', 'user_pass': ''},
    {'ip_port': '114.115.210.105:3128', 'user_pass': ''},
    {'ip_port': '121.13.84.143:808', 'user_pass': ''},
]
