import scrapy
from shiyanlou.items import UserItem


class UsersSpider(scrapy.Spider):
    name = 'users'

    @property
    def start_urls(self):
        url_tmp = 'https://www.lanqiao.cn/users/{}/'
        return (url_tmp.format(i) for i in range(525000,524800,-10))

    def parse(self,response):
        item = UserItem(
                name = response.xpath(
                    '//div[contains(@class,"user-meta")]/span/text()'
                    ).extract_first().strip(),
                level = response.xpath(
                    '//div[contains(@class,"user-meta")]/span/text()'
                    ).extract()[1].strip(),
                status = response.xpath(
                    '//div[contains(@class,"user-status")]/span/text()'
                    ).extract_first(default='无').strip(),
                school_job = response.xpath(
                    '//div[contains(@class,"user-status")]/span[2]/text()'
                    ).extract_first(default='无').strip(),
                learn_courses_num = response.xpath(
                    '//div[contains(@class,"tabs-left")]/span/text()'
                    ).re_first('\D+(\d+)\D+'),
                join_date = response.xpath(
                    '//span[contains(@class,"user-join-date")]/text()'
                    ).extract_first().strip()
                )
        if response.xpath('//div[contains(@class,"avatar-container")]/a/div/img/@src').extract():
            item['is_vip'] = True

        yield item
