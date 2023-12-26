import os
import sys
from pathlib import Path

import django
import dotenv

dotenv.load_dotenv()

DJANGO_PROJECT_PATH = f"{os.path.abspath(Path(__file__).parents[2])}"
sys.path.insert(0, DJANGO_PROJECT_PATH)
os.environ['DJANGO_SETTINGS_MODULE'] = 'configs.settings'
django.setup()

BOT_NAME = "scraper"
LOG_ENABLED = False

SPIDER_MODULES = ["scraper.spiders"]
NEWSPIDER_MODULE = "scraper.spiders"

ROBOTSTXT_OBEY = True

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
FEED_EXPORT_ENCODING = "utf-8"

BROWSER_LAUNCH_ARGS = [
    "--ignore-certificate-errors=True",
    "--ignoreHTTPSErrors=True",
    "--disable-blink-features=AutomationControlled",
    # "--headless=True"
]

# SPIDER_MIDDLEWARES = {
#    "scraper.middlewares.ScraperSpiderMiddleware": 543,
# }

# DOWNLOADER_MIDDLEWARES = {
#     "scraper.middlewares.ScraperDownloaderMiddleware": 543,
# }

# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }
#
# ITEM_PIPELINES = {
#     "scraper.pipelines.ScraperPipeline": 300,
# }


# AUTOTHROTTLE_ENABLED = True
# AUTOTHROTTLE_START_DELAY = 5
# AUTOTHROTTLE_MAX_DELAY = 60
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# AUTOTHROTTLE_DEBUG = False
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

def main():
    pass
    # print(DJANGO_PROJECT_PATH)


if __name__ == "__main__":
    main()
