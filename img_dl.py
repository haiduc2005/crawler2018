# coding=utf-8
import time
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import Request
import re
import os
# from lxml import etree

url = 'https://www.deviantart.com/jernau/gallery/2835881/Linux-Mint'
# url = 'http://zwopper.deviantart.com/gallery/8930983/Linux-Mint?offset=0'
driver = webdriver.Firefox()
driver.maximize_window()
driver.get(url)
time.sleep(3)
# 模拟滚动窗口以浏览下载更多图片  
pos = 0
for i in range(10):
    pos += i*200 # 每次下滚200
    driver.execute_script("window.scrollTo(0, " + str(pos) + ");")
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
# items = driver.find_elements_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div/table/tbody/tr/td[2]/div/div[1]/div/div/div/div[2]/div/div/div[2]/div[2]/span[*]/a/img")
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36"}
# req1 = Request(url, headers=headers)
# rep1 = urlopen(req1)
# text = rep1.read()
# html = etree.HTML(text)
html = driver.page_source.encode('utf-8')
soup1 = BeautifulSoup(html, 'lxml')
items = soup1.find_all("a", class_="torpedo-thumb-link")
# path = "//*[@id='gmi-']/span[*]/a"
# items = html.xpath(path)
folder_path = './wallpaper/'
if os.path.exists(folder_path) == False:  # 判断文件夹是否已经存在
    os.makedirs(folder_path)  # 创建文件夹
for index, item in enumerate(items):
    # html = requests.get(item.get('src'))
    url = item.get("href")
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    # req = Request(item.get('src'), headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(req)
    html = response.read()
    soup = BeautifulSoup(html, "lxml")
    item = soup.find_all('img')[0]
    
    html = requests.get(item.get('src'))   # get函数获取图片链接地址，requests发送访问请求
    file_name = url.split("/")[-1]
    img_name = folder_path + file_name + '.png'
    print('第%d张图片开始下载' % (index + 1))
    if os.path.exists(img_name) == True:  # 判断文件是否已经存在
        print('图片已经存在:' + file_name)
        continue
    with open(img_name, 'wb') as file:  # 以byte形式将图片数据写入
        file.write(html.content)
        file.flush()
    file.close()  # 关闭文件
    print('下载完成图片:' + file_name)
print('抓取完成')
