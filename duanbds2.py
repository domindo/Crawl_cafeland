from gc import callbacks
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from selenium import webdriver
from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import pandas as pd
import json
import time
import codecs
from selenium.common.exceptions import NoSuchElementException
from scrapy_selenium import SeleniumRequest

from selenium import webdriver

from selenium.webdriver.chrome.options import Options


options = Options()

driver = webdriver.Chrome(
    options=options, executable_path='C:/Users/WW/Downloads/chromedriver_win32 (1)/chromedriver.exe')


# with open("data.json", "w") as f:
#     json.dump([], f)


# def write_json(new_data, filename='data.json'):
#     with open(filename, 'r+') as file:
#         file_data = json.loads(file)
#         file_data.append(new_data)
#         file.seek(0)
#         json.dump(file_data, file, indent=4)


class BooksSpider(Spider):
    name = 'duanbds2'
    allowed_domains = ['cafeland.vn']

    def start_requests(self):

        self.driver = webdriver.Chrome(
            'C:/Users/WW/Downloads/chromedriver_win32 (1)/chromedriver.exe')
        self.driver.get('https://cafeland.vn/du-an/')

        sel = Selector(text=self.driver.page_source)
        path = sel.xpath("//div/h3/a/@href").extract()

        for path1 in path:
            url = path1
            driver.get(url)
            title = "No title"
            size = "No size"
            location = "No location"
            type = "No type"
            investor = "No investor"

          
            try:
                title = driver.find_element(
                    "xpath", "//tbody/tr[1]/td[1]/p[1]/span[1]/span[1]").text.replace('Dự án: ', '')
            except:
                pass
            try:
                size = driver.find_element(
                    "xpath", "//tbody//tr//td[2]//p//span//span").text.replace('Tổng diện tích: ', '')
            except:
                pass
            try:
                location = driver.find_element(
                    "xpath", "//tbody//tr[2]//td//p//span//span").text.replace('Vị trí: ', '')
            except:
                pass
            try:
                type = driver.find_element(
                    "xpath", "//tbody//tr[3]//td//p//span//span").text.replace('Loại hình: ', '')
            except:
                pass
            try:
                investor = driver.find_element(
                    "xpath", "//tbody//tr[4]//td//p//span//span").text.replace('Chủ đầu tư: ', '')
            except:
                pass

            write_json({
                "Tên Dự án": title,
                "Diện tích": size,
                "Vị trí": location,
                "Loại hình": type,
                "Chủ đầu tư": investor
            })
        while True:
            try:

                next_page = self.driver.find_element("xpath",
                                                     "//a[normalize-space()='»']")
                time.sleep(2)
                next_page.click()

                sel = Selector(text=self.driver.page_source)
                path = sel.xpath("//div/h3/a/@href").extract()

                for path1 in path:
                    url = path1
                    driver.get(url)
                    title = "No title"
                    size = "No size"
                    location = "No location"
                    type = "No type"
                    investor = "No investor"

                    try:
                        title = driver.find_element(
                            "xpath", "//tbody/tr[1]/td[1]/p[1]/span[1]/span[1]").text.replace('Dự án: ', '')
                    except:
                        pass
                    try:
                        size = driver.find_element(
                            "xpath", "//tbody//tr//td[2]//p//span//span").text.replace('Tổng diện tích: ', '')
                    except:
                        pass
                    try:
                        location = driver.find_element(
                            "xpath", "//tbody//tr[2]//td//p//span//span").text.replace('Vị trí: ', '')
                    except:
                        pass
                    try:
                        type = driver.find_element(
                            "xpath", "//tbody//tr[3]//td//p//span//span").text.replace('Loại hình: ', '')
                    except:
                        pass
                    try:
                        investor = driver.find_element(
                            "xpath", "//tbody//tr[4]//td//p//span//span").text.replace('Chủ đầu tư: ', '')
                    except:
                        pass

                    write_json({
                        "Tên Dự án": title,
                        "Diện tích": size,
                        "Vị trí": location,
                        "Loại hình": type,
                        "Chủ đầu tư": investor
                    })
            except NoSuchElementException:
                self.driver.quit()
                break


with open("data3.json", "w", encoding='utf8') as f:
    json.dump([], f, ensure_ascii=False)


def write_json(new_data, filename='data3.json'):
    with open(filename, 'r+', encoding='utf8') as file:
        file_data = json.load(file)
        file_data.append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4, ensure_ascii=False)
