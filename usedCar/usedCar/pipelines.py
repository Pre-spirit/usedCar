# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv
from itemadapter import ItemAdapter


class UsedcarPipeline:
    def __init__(self):
        file = open("data.csv", "w", newline="", encoding="utf-8")
        # 创建一个csv文件的写入器对象
        self.writer = csv.writer(file)
        self.writer.writerow(["brand", "price", "tag"])

    def process_item(self, item, spider):
        self.writer.writerow([item['brand'], item['price'], item['tag']])
