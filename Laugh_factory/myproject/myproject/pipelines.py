# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
# import sqlite3
import mysql.connector

class MyprojectPipeline:
    def __init__(self):
        self.create_database()
        self.create_table()

    def create_database(self):
        self.con = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'mydb'
        )
        self.c = self.con.cursor()

    def create_table(self):
        self.c.execute("""  Drop table if exists tbl_myjokes """)
        self.c.execute(""" create table tbl_myjokes (joke text, likes text, dislikes text)""")

    def store_data(self,item):
        self.c.execute(""" insert into tbl_myjokes values (%s,%s,%s) """,(item['joke'][0], item['likes'][0], item['dislikes'][0] ))
        self.con.commit()
    
    def process_item(self, item, spider):
        self.store_data(item)
        return item
