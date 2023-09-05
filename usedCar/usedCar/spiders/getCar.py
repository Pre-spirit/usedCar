import scrapy
from usedCar.items import UsedcarItem


class GetcarSpider(scrapy.Spider):
    name = "getCar"
    allowed_domains = ["www.renrenche.com"]
    start_urls = ["https://www.renrenche.com/cd/ershouche/"]

    def parse(self, response):
        # 获取当前页面二手车信息
        car_list = response.xpath("//ul[@class='row-fluid list-row js-car-list']/li")

        for li in car_list:
            item = UsedcarItem()
            # 提取品牌
            brand = li.xpath("./a/h3/text()").extract_first()
            if brand is None:
                continue
            brand = brand.split(" ")[0].split("-")[0]
            price = li.xpath(".//div[@class='price']/text()").extract_first().strip()
            tags = li.xpath(".//div[@class='mileage-tag-box']/span")
            tag_list = []
            for tag in tags:
                tag_str = tag.xpath("./text()").extract_first().strip()
                tag_list.append(tag_str)

            # 填充数据到 item
            item['brand'] = brand
            item['price'] = price
            item['tag'] = "、".join(tag_list)
            # 推送至管道，pipelines脚本进行处理
            yield item

        # 获取下页地址
        next_url = response.xpath("//ul[@class='pagination js-pagination']/li[last()]/a/@href").extract_first()

        # 判断不为最后一页继续请求数据
        if next_url != "javascript:void(0);":
            next_url = "https://www.renrenche.com" + next_url
            # 发送请求并设置回调函数
            yield scrapy.Request(next_url, callback=self.parse)



"""
import scrapy
from usedCar.items import UsedcarItem


class GetcarSpider(scrapy.Spider):
    name = "getCar"
    allowed_domains = ["www.renrenche.com"]
    start_urls = ["https://www.renrenche.com"]

    # def __init__(self):
    #     self.driver = webdriver.Chrome()

    def parse(self, response):
        file = open("test.txt", "a", newline="", encoding="utf-8")

        # 使用Selenium来加载页面
        # self.driver.get(response.url)
        with file:
            file.write(response.text)


        # 提取当前页面二手车信息
        # car_list = self.driver.find_elements(By.XPATH, "//ul[@class='row-fluid list-row js-car-list']/li")
        car_list = response.xpath("//ul[@class='row-fluid list-row js-car-list']/li")
        with file:
            file.write(car_list)

        for li in car_list:
            # item = UsedcarItem()
            # 品牌
            brand = li.xpath("./a/h3/text()").extract_first()  # 提取品牌数据
            # 如果爬取不到品牌（例如当前li是一个广告），则进行下一次循环
            if brand is None:
                continue

            brand = brand.split(" ")[0].split("-")[0]  # 品牌
            price = li.xpath(".//div[@class='price']/text()").extract_first().strip()  # 价格
            # 当前汽车的span标签
            tags = li.xpath(".//div[@class='mileage-tag-box']/span")
            tag_list = []
            # 遍历当前汽车的每个标签，并添加到列表中
            for tag in tags:
                tag_str = tag.xpath("./text()").extract_first().strip()
                tag_list.append(tag_str)

            # 填充数据到Item
            # item["brand"] = brand
            # item["price"] = price
            # item["tag"] = "_".join(tag_list)
            # yield item  # 交给Item Pipeline处理
            with file:
                file.write("brand: " + brand + "    price: " + price + "    tag: " + "、".join(tag_list))

        # 找到“下一页”按钮的URL地址
        next_url = response.xpath("//ul[@class='pagination js-pagination']/li[last()]/a/@href").extract_first()
        with file:
            file.write(next_url)

        # 如果不是最后一页
        if next_url != "javascript:void(0);":
            next_url = "https://www.renrenche.com" + next_url  # 补充完整下一页的URL
            # 向下一页发送请求，并设置回调函数为parse方法，因为下一页的解析方法与当前页相同
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )
"""

