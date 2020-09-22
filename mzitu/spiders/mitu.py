import scrapy


class MituSpider(scrapy.Spider):
    name = 'mitu'
    allowed_domains = ['mzitu.com']
    start_urls = ['http://mzitu.com/']

    def parse(self, response):
        pass
