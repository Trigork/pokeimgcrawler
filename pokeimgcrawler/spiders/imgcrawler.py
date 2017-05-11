import scrapy
import re

stop_number = "#802"


class PokeImgSpider(scrapy.Spider):
    name = "imgcrawler"
    start_urls = [
        'http://bulbapedia.bulbagarden.net/wiki/Bulbasaur_(Pok%C3%A9mon)'
    ]

    def parse(self, response):
        imgs = response.css('#mw-content-text table:nth-child(2) table:nth-child(1) tr > td > a > img')
        number = response.css('#mw-content-text table:nth-child(2) table:nth-child(1) tr > th a > span::text').extract_first()
        for im in imgs:
            final_im = im.xpath('@src').extract_first()
            final_im = '/'.join(final_im.replace('thumb/', '').split('/')[:-1])
            name = im.xpath('@alt').extract_first()
            yield {'file_urls': [final_im]}

        next_poke = response.css('#mw-content-text > table:nth-child(1) tr:nth-child(1) > td:nth-child(3)')[-1]
        next_page = next_poke.css('a::attr(href)').extract_first()

        if number != stop_number:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(next_page_url, callback=self.parse)

