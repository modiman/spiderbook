import pymongo
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery as pq
class taobao:
    def __init__(self):
        self.keyword = '羽绒服'
        path ='E:\安装包\chromedriver_win32\chromedriver.exe'
        self.browser = webdriver.Chrome(executable_path=path)
        self.wait = WebDriverWait(self.browser, 10)
    def get_index(self,page,browser,wait):
        """
            抓取索引页
            :param page: 页码
            """
        print(' 正在爬取第 ', page, ' 页 ')
        try:
            url = 'https://s.taobao.com/search?q=' + quote(self.keyword)
            browser.get(url)
            if page > 1:
                input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form> input')))
                submit = wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form> span.btn.J_Submit')))
                input.clear()
                input.send_keys(page)
                submit.click()
            wait.until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active> span'), str(page)))
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
            self.get_products()
        except TimeoutException:
            self.get_index(page+1,t.browser,t.wait)

    def get_products(self):
        """提取商品数据"""
        html = self.browser.page_source
        doc = pq(html)
        items = doc('#mainsrp-itemlist .items .item').items()
        for item in items:
            product = {'image': item.find('.pic .img').attr('data-src'),
                       'price': item.find('.price').text(),
                       'deal': item.find('.deal-cnt').text(),
                       'title': item.find('.title').text(),
                       'shop': item.find('.shop').text(),
                       'location': item.find('.location').text()}
            print(product)
            self.save_to_mongo(product)

    def save_to_mongo(self,result):
        MONGO_URL = 'localhost'
        MONGO_DB = 'taobao'
        MONGO_COLLECTION = 'products'
        client = pymongo.MongoClient(MONGO_URL)
        db = client[MONGO_DB]

        """
        保存至 MongoDB
        :param result: 结果
        """
        try:
            if db[MONGO_COLLECTION].insert(result):
                print(' 存储到 MongoDB 成功 ')
        except Exception:
            print(' 存储到 MongoDB 失败 ')
if __name__ == '__main__':
    t = taobao()
    for i in range(1,100):
        try:
            t.get_index(i,t.browser,t.wait)
        except Exception as e:
            print(e)
