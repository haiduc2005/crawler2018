#coding=utf-8
from selenium import webdriver
from urllib.request import Request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import settings

#Firefox
driver=webdriver.Firefox()
url = settings.URL_VERIFY
url_my_home = settings.URL_VERIFY_HOME

driver.get(url)
driver.find_element_by_xpath("/html/body/div[1]/header/div/div/div[2]/ul/li[6]/a/b").click()# サインイン/ログインを押下

driver.find_element_by_xpath("//*[@id='login']").clear()
driver.find_element_by_xpath("//*[@id='login']").send_keys(settings.VERIFY_ID)
driver.find_element_by_xpath("//*[@id='password']").clear()
driver.find_element_by_xpath("//*[@id='password']").send_keys(settings.VERIFY_PASS)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#driver.find_element_by_class_name("btn btn-primary").click()# login
driver.find_element_by_xpath("/html/body/div[1]/main/div/form/div[3]/button").click()# login

# クッキー取得
cookies = driver.get_cookies()
print(cookies)
# session_value = [x['value'] for x in cookies if x['name'] == 'session_id']
# print(session_value)
# cookie = [x for x in cookies if x['name'] == 'session_id']
# print(cookie)

# 取得したクッキーをセッションに保持するように
s = requests.Session()
for cookie in cookies:
    s.cookies.set(cookie['name'], cookie['value'])

req = s.get(url_my_home, headers={'User-Agent': 'Mozilla/5.0'})
# req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
print(req.text)
# response = urlopen(req)
# html = response.read()
soup = BeautifulSoup(req.text,"html5lib")
title = soup.findAll('title')[0].text
# title = soup.findAll('h1')[0].text
print("title：" + title)
#driver.quit()