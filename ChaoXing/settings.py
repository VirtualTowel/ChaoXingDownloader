# -*- coding: utf-8 -*-

# Scrapy settings for ChaoXing project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'ChaoXing'

SPIDER_MODULES = ['ChaoXing.spiders']
NEWSPIDER_MODULE = 'ChaoXing.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 2

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Cookie': 'k8s-ed=efa577abc4d2b69fb1210c27bfb282a6487f6f08; jrose=5AFFFF5C9D428C469D60E1BF3EB167A9.html-editor-a-3952264778-3xgkg; k8s=407f4a8cf583ea36e5c5858e6cf11e0e7c5f1ded; jrose=AEAE919993737DB51EE7DA0553D2707D.mooc-803768169-bds5m; route=f537d772be8122bff9ae56a564b98ff6; thirdRegist=0; uname=18240737; fid=1860; _uid=82230081; uf=b2d2c93beefa90dcfb9c117d6a0b9a804461ef35109dffb33c741913a3fba8d09327e3db275dfd696c6a67cabcf4fcf9c49d67c0c30ca5047c5a963e85f11099066968bd22bfc0d2ce71fc6e59483dd3aaece5e46c58b7a923c8850a242d46e931b766465b6de9aa; _d=1582280384109; UID=82230081; vc=210A92949C677AFF5A9AE3343227243A; vc2=2D70375C73CB7CA90C4F2CA2727F759B; vc3=F1lFilKYGmMfd0Oeze4nysyWZlpJFKzYrIQH7uobuoc5F2TD4RAPgoUe5XAh6UMenF96FfKEQQnLnc6f2leBQzz9yh%2BdC7DLKiqJzSugZ8PmhvEbN%2BSKzZVur6besKVUa3QQJrZ9VygAVGkqA82D4VXrLiVOEjvansDnv3sg8IE%3Da865487c357bd5d270388e76ae18a93e; xxtenc=79d9575f335aaaa1ccee0e4879fbf4bc; DSSTASH_LOG=C_38-UN_139-US_82230081-T_1582280384110; source=""; rt=-1; tl=0; fanyamoocs=074727C503C4651211401F839C536D9E; isfyportal=1; videojs_id=364087'
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'ChaoXing.middlewares.ChaoxingSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'ChaoXing.middlewares.ChaoxingDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'ChaoXing.pipelines.ChaoxingPipeline': 300,
# }
ITEM_PIPELINES = {
    # 'scrapy.pipelines.files.FilesPipeline':1,
    'ChaoXing.pipelines.MyFilesPipeline':1,
}
FILES_STORE = 'Downloads'
DOWNLOAD_TIMEOUT = 1800
MEDIA_ALLOW_REDIRECTS = True

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
