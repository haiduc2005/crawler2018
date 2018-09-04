#coding=utf-8
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import Request
import re
import os
from lxml import etree
import urllib2

url = 'http://zwopper.deviantart.com/gallery/8930983/Linux-Mint?offset=0'
# driver=webdriver.Firefox()
# driver.get(url)
# items = driver.find_elements_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div/table/tbody/tr/td[2]/div/div[1]/div/div/div/div[2]/div/div/div[2]/div[2]/span[*]/a/img")
# items = driver.find_elements_by_xpath("//*[@id='gmi-']/span[*]/a")
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36"}
req1 = urllib2.Request(URL, headers=headers)
rep1 = urllib2.urlopen(req1)
text = rep1.read()
html=etree.HTML(text)
path="//*[@id='gmi-']/span[*]/a"
html_data = html.xpath(path)
folder_path = './photo/'
if os.path.exists(folder_path) == False:  # 判断文件夹是否已经存在
    os.makedirs(folder_path)  # 创建文件夹
for index, item in enumerate(items):
    # html = requests.get(item.get('src'))
    req = Request(item.get_attribute("href"), headers={'User-Agent': 'Mozilla/5.0'})
    # req = Request(item.get('src'), headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(req)
    html = response.read()
    soup = BeautifulSoup(html,"html5lib")    
    item = soup.find_all('png')[0]
    
    html = requests.get(item.get('src'))   # get函数获取图片链接地址，requests发送访问请求
    img_name = folder_path + str(index + 1) +'.png'
    with open(img_name, 'wb') as file:  # 以byte形式将图片数据写入
        file.write(html.content)
        file.flush()
    file.close()  # 关闭文件
print('抓取完成')