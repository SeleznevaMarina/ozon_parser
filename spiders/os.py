import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
# from scrapy.loader.processors import TakeFirst, Identity
# from scrapy.loader import ItemLoader
# from scrapy.selector import HtmlXPathSelector, Selector
from ozon_parser.items import DataItem
from selenium import webdriver
 
driver = webdriver.Chrome()

driver.get("https://www.ozon.ru/category/smartfony-15502/?sorting=rating")



class SmartphoneSpider(CrawlSpider):

    name = "os"
    allowed_domains = ["www.ozon.ru"]
    start_urls = ["https://www.ozon.ru/category/smartfony-15502/?sorting=rating"]

    rules = (
            #  Rule(SgmlLinkExtractor(allow=('search\.php\?.+')), follow=True),
             Rule(LinkExtractor(allow=('vuz_detail\.php\?.+')), callback='parse_item'),
             )


    def parse_item(self):

        
        # for item in range(100):
        Item = DataItem()
        button = driver.find_element_by_class("tile-hover-target ai8 ia8")
        button.click()
        os = driver.find_element_by_name("Операционная система")
        version = driver.find_element_by_name(f"Версия {os}")


        driver.quit()