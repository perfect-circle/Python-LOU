# 简介
1. 本节内容运用前两节学到的知识，爬取实验楼的用户数据，主要是为了练习、巩固前面学习到的知识。
知识点

* Scrapy 项目框架
* 分析网页元素字段
* SQLAlchemy 定义数据模型
* 创建 Item
* 解析数据

## 定义数据模型
[models.py]
```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Inteage
from sqlalchemy import Date, Boolean

engine = create_engine('mysql://root@password@localhost/database')
Base = declarative_base()

class User(Base):
	__tablename__ = "users"
	id = Column(Inteage, primary_key=True)
	name = Column(String(64), index=True)
	is_vip = Column(Boolean, default=False)
	status = Column(String(64), index=True)
	level = Column(String(64))
	join_date = Column(Date)
	learn_courses_num = Column(Integer)
```

** 创建数据模型 **
```shell
python3 models.py	SQLAlchemy 默认不会重新创建已经存在的表，所以不用担心 create_all 会重新创建 course 表造成数据丢失。

```

## 创建Item
```python
import scrapy

class UserItem(scrapy.Item):
	name = scrapy.Field()
	is_vip = scrapy.Field()
	status = scrapy.Field()
	school_job = scrapy.Field()
	level = scrapy.Field()
	join_date = scrapy.Field()
	learn_courses_num = scrapy.Field()
```

## 创建爬虫

1. 创建爬虫命令

```shell
scrapy genspider users lanqiao.cn
```

2. 解析数据
[spiders/users.py]
```python
import scrapy

class UsersSpider(scrapy.Spider):
	name = 'user'
	url_temp = 'https://www.lanqiao.cn/users/{}'
	for x in range(525000, 534000, -10):
		start_urls = ['https://www.lanqiao.cn/users/{}'.format(x)]

	def parse(self, response):
		item = UserItem(
			name = response.css('div.user-meta span::text').extract()[0].strip(),
            		level = response.css('div.user-meta span::text').extract()[1].strip(),
			status = response.css('div.user-status span::text').extract_first(default='无').strip(),
			school_job = response.xpath('//div[@class="user-status"]/span[2]/text()').extract_first(default='无').strip(),
			join_date = response.css('span.user-join-date::text').extract_first().strip(),
			learn_courses_num = response.css('span.tab-item::text').re_first('\D+(\d+)\D+')
		)
        	if len(response.css('div.user-avatar img').extract()) == 2:
            		item['is_vip'] = True

	yield item
```

## pipeline
1. 因为 pipeline 会作用在每个 item 上，当和课程爬虫共存时候，需要根据 item 类型使用不同的处理函数。
[pipeline.py]
```python
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from shiyanlou.models import Course, User, engine
from shiyanlou.items import CourseItem, UserItem


class ShiyanlouPipeline(object):

    def process_item(self, item, spider):
        """ 对不同的 item 使用不同的处理函数
        """
        if isinstance(item, CourseItem):
            self._process_course_item(item)
        else:
            self._process_user_item(item)
        return item

    def _process_course_item(self, item):
        item['students'] = int(item['students'])
        self.session.add(Course(**item))

    def _process_user_item(self, item):
        # 抓取到的数据类似 'L100'，需要去掉 'L' 然后转化为 int
        item['level'] = int(item['level'][1:])
        # 抓取到的数据类似 '2017-01-01 加入实验楼'，把其中的日期字符串转换为 date 对象
        item['join_date'] = datetime.strptime(item['join_date'].split()[0], '%Y-%m-%d')
        # 学习课程数目转化为 int
        item['learn_courses_num'] = int(item['learn_courses_num'])
        # 添加到 session
        self.session.add(User(**item))

    def open_spider(self, spider):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def close_spider(self, spider):
        self.session.commit()
        self.session.close()

```

## 运行
```shell
scrapy crawl users
```
