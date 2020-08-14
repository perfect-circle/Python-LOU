# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ShiyanlouGithubItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class RepositoriesItem(scrapy.Item):
    name = scrapy.Field()
    update_time = scrapy.Field()
    commits = scrapy.Field()
    branch = scrapy.Field()
    tags = scrapy.Field()
