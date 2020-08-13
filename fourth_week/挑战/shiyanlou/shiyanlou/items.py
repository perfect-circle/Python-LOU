# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ShiyanlouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class CourseItem(scrapy.Item):
    """
    定义 Item 非常简单，只需要继承 scrapy.Item 类，将每个要爬取的数据声明为 scrapy.Field()
    下面的代码是我们每个课程要爬取的 4 个数据
    """
    name = scrapy.Field()
    description = scrapy.Field()
    type = scrapy.Field()
    students = scrapy.Field()

class UserItem(scrapy.Item):
    name = scrapy.Field()
    is_vip = scrapy.Field()
    status = scrapy.Field()
    school_job = scrapy.Field()
    level = scrapy.Field()
    join_date = scrapy.Field()
    learn_courses_num = scrapy.Field()
