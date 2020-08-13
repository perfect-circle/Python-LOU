# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from shiyanlou_github.models import Repositories, engine
from sqlalchemy.orm import sessionmaker
from shiyanlou_github.items import RepositoriesItem
from datetime import datetime


class ShiyanlouGithubPipeline:
    def process_item(self, item, spider):
        if isinstance(item, RepositoriesItem):
            self._process_repositories_item(item)
        return item

    def _process_repositories_item(self, item):
        item['update_time'] = datetime.strptime(item['update_time'],
                '%Y-%m-%dT%H:%M:%SZ')
        self.session.add(Repositories(**item))

    def open_spider(self, spider):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def close_spider(self, spider):
        self.session.commit()
        self.session.close()
