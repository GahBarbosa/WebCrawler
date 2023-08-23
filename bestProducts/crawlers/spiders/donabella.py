import scrapy

class TitamsSpider(scrapy.Spider):
    name = "donabella"
    start_urls = [
        'https://donabella-store.com/collections/all',
    ]

    def parse(self, response):
        for quote in response.css('.product-item'):
            yield {
                'name': quote.css('.product-item__title::text').get(),
                'img_url': quote.css('.product-item__primary-image::attr(data-src)').get(),
                'img_w': quote.css('.product-item__primary-image::attr(data-widths)').get(),
                'url': quote.css('a::attr(href)').get(),
            } 