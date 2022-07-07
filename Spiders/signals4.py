import logging
from scrapy import signals
import scrapy

logger = logging.getLogger(__name__)

class SpiderOpenCloseLogging(scrapy.Spider):

    name = 'log_signals'

    start_urls =  [f'http://quotes.toscrape.com/page/{i}/' for i in range(1, 11)]

    def __init__(self, item_count, stats):
        self.item_count = item_count
        self.items_scraped = stats
        #self.items_scraped = 0

    @classmethod
    def from_crawler(cls, crawler):
        ext = cls(crawler.settings,crawler.stats)

        crawler.signals.connect(ext.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(ext.spider_closed, signal=signals.spider_closed)
        crawler.signals.connect(ext.item_scraped, signal=signals.item_scraped)

        return ext

    def spider_opened(self, spider):
        self.items_scraped = self.items_scraped.get_value('item_scraped_count')
        if self.items_scraped is None:
            self.items_scraped = 0
        self.item_count = self.item_count.getint('MYEXT_ITEMCOUNT', 1000)
        print(f'TEST: {self.items_scraped}, COUNT:{self.item_count}')
        logger.info("opened spider %s", spider.name)

    def spider_closed(self, spider):
        logger.info("closed spider %s", spider.name)

    def item_scraped(self, item, spider):
        logger.info(f"scraped few {self.items_scraped} items")
        self.items_scraped += 1
        if  self.item_count % self.items_scraped == 0:
            #print(f"scraped increments {self.items_scraped} items")
            logger.info(f"scraped increments {self.items_scraped} items")
    
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url=url,
                callback=self.parse
            )
    def parse(self, response):
        content = response.xpath('//div[@class = "row"]//div')
        for items in content:
            yield {
                'some_items_links':items.xpath(".//a//@href").get()
            }