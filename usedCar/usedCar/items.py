# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UsedcarItem(scrapy.Item):
    # 品牌
    brand = scrapy.Field()
    # 价格
    price = scrapy.Field()
    # 标签
    tag = scrapy.Field()

