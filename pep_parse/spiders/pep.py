import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        for pep in response.css('.num').css('a::attr(href)'):
            yield response.follow(pep, callback=self.parse_pep)

    def parse_pep(self, response):
        data = {

            'number': response.css('dt:contains("PEP") + dd::text').get(),
            'name': response.css('h1.page-title::text').get(),
            'status': response.css('dt:contains("Status") + dd::text').get(),
        }
        yield PepParseItem(data)
