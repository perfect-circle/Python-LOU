import json
import time
from selenium import webdriver
from scrapy.http import HtmlResponse
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

results = []
def parse(response):
    for comment in response.xpath('//div[@class="row comment-item"]'):
        result = dict(
            username=comment.xpath(
                './/a[@class="name"]/text()'
                ).extract_first().strip(),
            conten=comment.xpath(
                './/div[@class="comment-body content"]/text()'
                ).extract_first().strip()
            )
        print("comment: {}".format(result))
        results.append(result)

def has_next_page(response):
    has_page = response.xpath(
            '//ul[@class="pagination"]/li[2]/@class'
            ).extract_first().strip()
    return "disabled" not in has_page

def goto_next_page(driver):
    next_page = driver.find_element_by_xpath(
            '//ul[@class="pagination"]/li[2]')
    time.sleep(3)
    next_page.click()

def spider():
    driver = webdriver.Firefox()
    url = 'https://www.lanqiao.cn/courses/427'
    driver.get(url)
    while True:
        driver.implicitly_wait(5)
        html = driver.page_source
        reponse = HtmlResponse(url=url, body=html.encode())
        results.append(parse(reponse))
        if has_next_page(reponse):
            goto_next_page(driver)
        else:
            break
    driver.quit()

    with open('comments.json','w') as f:
        json.dump(results, f)

if __name__ == "__main__":
    start = time.time()
    spider()
    print('耗时 : {:.2f}s'.format(time.time()-start))
