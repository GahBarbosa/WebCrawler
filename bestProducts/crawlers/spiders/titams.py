import scrapy


class TitamsSpider(scrapy.Spider):
    name = "titams"
    start_urls = [
        'https://titams.com/collections/all?sort_by=best-selling',
    ]

    def parse(self, response):
        for quote in response.css('.product-item'):
            yield {
                'name': quote.css('.link::text').get(),
                'price': quote.css('.price::text').get(),
                'link': quote.css('a::attr(href)').get(),
            } 