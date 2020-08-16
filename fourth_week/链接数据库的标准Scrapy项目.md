# 创建项目
1. scrapy startproject shiyanlou

# 创建爬虫
1. scrapy genspider <name> <domain>	# name是爬虫的名称，domain是域名

[spider/name.py]
```python
import scrapy

class nameSpider(scrapy.Spider):
	name = 'name'
	start_urls = ['https://www.baidu.com/']
	
	def parse(self,response):
		"""提取器"""
	item = NameItem({
		'name': 
		'description':
		'type':
		})
	yield item
```

## Item

[item.py]
```python
import scrapy
class CourseItem(scrapy.Item):
	"""定义 Item 非常简单，只需要继承 scrapy.Item 类，
	将每个要爬取的数据声明为 scrapy.Field()
   	 下面的代码是我们每个课程要爬取的 4 个数据"""
	name = scrapy.Field()
	description = scrapy.Field()
	type = scrapy.Field()
```

## Item Pipelien
1. 如果把 scrapy 想象成一个产品线，spider 负责从网页上爬取数据，Item 相当于一个包装盒，对爬取的数据进行标准化包装，然后把它们扔到 Pipeline 流水线中。

2. 主要在 Pipeline 对 Item 进行这几项处理：
* 验证爬取到的数据（检查 item 是否有特定的 field ）
* 检查数据是否重复
* 存储到数据库

3. 当创建项目时，scrapy已经在pipelines.py中为项目生成一个pipeline模板：
```python

from sqlalchemy.orm import sessionmaker
from shiyanlou.models import Course, engine

clsaa NamePipeline(object):
	def process_item(self, item, spider):
		item['students'] = int(item['students']
	return item

	def open_spider(self, spider):
		""" 当爬虫被开启的时候调用
        	"""
		Session = sessionmaker(bind=engine)
		self.session = Session()

	def close_spider(self, spider):
		""" 当爬虫被关闭的时候调用
        	"""
		self.session.commit()
		self.session.close()
```

4. 我们编写的这个 ShiyanlouPipeline 默认是关闭的状态，要开启它，需要在settings.py将下面的代码取消注释：
```python
# 默认是被注释的
ITEM_PIPELINES = {
    'shiyanlou.pipelines.ShiyanlouPipeline': 300
}
```

### item过滤
1. 有时候，并不是每个爬取到的 item 都是我们想要，我们希望对 item 做一下过滤，丢弃不需要的数据。比如只希望保留学习人数超过 1000 的课程，那么就可以对 pipeline 做如下修改：
```python
from scrapy.exceptions import DropItem

class ShiyanlouPipeline(object):

    def process_item(self, item, spider):
        item['students'] = int(item['students'])
        if item['students'] < 1000:
            # 对于不需要的 item ，主动触发 DropItem 异常
            raise DropItem('Course students less than 1000.')
        else:
            self.session.add(Course(**item))
```

## 定义Model，创建表
1. [modle.py]
```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer


engine = create_engine('mysql://root@localhost:3306/shiyanlou?charset=utf8')
Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), index=True)
    description = Column(String(1024))
    type = Column(String(64), index=True)
    students = Column(Integer)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
```

2. 运行程序
```shell
python3 model.py
```

# 运行爬虫
1. 在项目目录输入
```shell
scrapy crawl courses
```
