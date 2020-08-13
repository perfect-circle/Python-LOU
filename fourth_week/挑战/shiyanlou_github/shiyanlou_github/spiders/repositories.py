import scrapy
from shiyanlou_github.items import RepositoriesItem


class RepositoriesSpider(scrapy.Spider):
    name = 'repositories'

    @property
    def start_urls(self):
        url_list = [
                'https://github.com/shiyanlou?tab=repositories',
                'https://github.com/shiyanlou?after='+
                'Y3Vyc29yOnYyOpK5MjAxNy0wNi0wN1QwODozMzozNyswODow'+
                'MM4FkpMh&tab=repositories',
                'https://github.com/shiyanlou?after='+
                'Y3Vyc29yOnYyOpK5MjAxNy0wNi0wNlQxMzoxNToyMiswO'+
                'DowMM4FkjnP&tab=repositories',
                'https://github.com/shiyanlou?after='+
                'Y3Vyc29yOnYyOpK5MjAxNC0xMi0xNlQxMDo0MTowMi'+
                'swODowMM4BrEWs&tab=repositories',
                'https://github.com/shiyanlou?after='+
                'Y3Vyc29yOnYyOpK5MjAxNC0xMS0wM1QwODo1OTox'+
                'MSswODowMM4BjgTX&tab=repositories'
                ]

        return url_list

    def parse(self, response):
        for repositorie in response.xpath('//li[contains(@itemprop,"owns")]'):
            item = RepositoriesItem(
                    name = repositorie.xpath(
                            './/a[contains(@itemprop,"name codeRepository")]/text()'
                            ).extract_first().strip(),
                    update_time = repositorie.xpath(
                            './/relative-time/@datetime'
                            ).extract_first().strip()
                    )
            yield item

