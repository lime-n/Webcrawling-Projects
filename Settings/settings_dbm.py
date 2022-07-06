"""
Use this setting to download the cache from the website; 
The caches could be used to scrape complex aspects of a site
i.e. scrapy playwright integration.
"""

BOT_NAME = 'scrapy_exercises'
from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent
SPIDER_MODULES = ['scrapy_exercises.spiders']
NEWSPIDER_MODULE = 'scrapy_exercises.spiders'

ROBOTSTXT_OBEY = False

from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent
IMAGES_STORE = os.path.join(BASE_DIR, 'images_test')
IMAGES_URLS_FIELD = 'images'
IMAGES_RESULT_FIELD = 'results'

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
HTTPCACHE_DBM_MODULE = 'dbm'
#HTTPCACHE_GZIP = True