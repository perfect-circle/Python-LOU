# -*- coding: utf-8 -*-

import scrapy

class GithubShiyanlouSpider(scrapy.Spider):
    name = 'github_shiyanlou'

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
        for repositories in response.xpath(
                '//ul[@data-filterable-for="your-repos-filter"]'
                ):
            for repositorie in repositories.xpath(
                    '//li[@class="col-12 d-flex width-full py-4 border-bottom public source"]'
                    ):
                yield {
                        "name": repositorie.xpath(
                            './/a[@itemprop="name codeRepository"]/text()'
                            ).extract_first().strip(),

                        "update_time": repositorie.xpath(
                            './/relative-time/@datetime'
                            ).extract_first().strip()
                        }
