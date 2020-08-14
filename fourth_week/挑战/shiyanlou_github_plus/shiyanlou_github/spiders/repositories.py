import scrapy
from shiyanlou_github.items import RepositoriesItem


class RepositoriesSpider(scrapy.Spider):
    name = 'repositories'
    strart_urls = [
            'https://github.com/shiyanlou?tab=repositories']

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

            # 构造仓库详情页，爬取的链接是相对链接，调用urljoin方法构造全链接
            repositorie_url =repositorie.xpath(
                    './/a/@href').extract_first()
            full_repositorie_url = response.urljoin(repositorie_url)
            request = scrapy.Request(full_repositorie_url,self.parse_more)
            request.meta['item'] = item
            yield request

        for url in response.xpath(
                '//div[@class="paginate-container"]/div/a/@href'
                ):
            yield response.follow(url,callback=self.parse)

    def parse_more(self, response):
        item = response.meta['item']
        item['commits'] = response.xpath(
                '//span[@class="d-none d-sm-inline"]/strong/text()'
                ).extract_first().strip()
        item['branches'] = response.xpath(
                '//a[contains(@class,"link-gray-dark no-underline")]/strong/text()'
                ).extract_first().strip()
        item['tags'] = response.xpath(
                '//a[contains(@class,"ml-3 link-gray-dark no-underline")]/strong/text()'
                ).extract_first().strip()
        yield item
