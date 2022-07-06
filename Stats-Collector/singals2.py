import scrapy
from scrapy import signals
from scrapy import crawler
import jsonlines

class TestSpider(scrapy.Spider):
    name = 'stats'

    start_urls = ['http://quotes.toscrape.com']

    def __init__(self, stats):
       self.stats = stats

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        #spider = super(TestSpider, cls).from_crawler(crawler, *args, **kwargs)
        stat = cls(crawler.stats)
        crawler.signals.connect(stat.spider_closed, signals.spider_closed)
        return stat

    def spider_closed(self):
        #self.stats = stat
        txt_file = 'some_text.jl'
        with jsonlines.open(txt_file, 'w') as f:
            f.write(f'{self.stats.get_stats()}')
        

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url=url,
                callback=self.parse
            )
    def parse(self, response):
        content = response.xpath('//div[@class = "row"]')
        for items in content:
            yield {
                'some_items_links':items.xpath(".//a//@href").get()
            }