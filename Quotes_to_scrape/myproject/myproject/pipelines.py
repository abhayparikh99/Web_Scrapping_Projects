# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class MyprojectPipeline:
    def __init__(self):
        self.create_database()
        self.create_table()

    def create_database(self):
        self.con = sqlite3.connect("myquotes.db")
        self.c = self.con.cursor()

    def create_table(self):
        self.c.execute(""" Drop table if exists tbl_quotes """)
        self.c.execute(""" create table tbl_quotes (title text, author text, tags text) """)

    def store_data(self,item):
        self.c.execute(""" insert into tbl_quotes values (?,?,?) """,(item['title'][0] , item['author'][0] , item['tags'][0] ))
        self.con.commit()

    def process_item(self, item, spider):
        self.store_data(item)
        return item
