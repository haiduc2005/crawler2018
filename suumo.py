#coding=utf-8

from selenium import webdriver
import selenium.webdriver.support.ui as ui
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import Request
import re

downloadDir = 'E:\\Down\\text\\suumo\\'#下载后存放目录
class xiaochun():
    
    #搜索
    def search():
        driver = webdriver.Firefox()
        base_url = "https://suumo.jp/jj/bukken/ichiran/JJ012FC002/?ar=030&bknh_listmodeflg=2&bs=021&sc=13105&ta=13&po=0&pj=1&pc=100"
        driver.get(base_url)
        title_list = driver.find_elements_by_xpath("/html/body/div[5]/div[1]/div[2]/div[2]/form[4]/div/div[*]/div[2]/div[1]/h2/a")#获取title列表所在的标签a
        detail_list = driver.find_elements_by_xpath("/html/body/div[5]/div[1]/div[2]/div[2]/form[4]/div/div[*]/div[2]/div[2]/div[1]/div[2]/div/div[1]/table/tbody/tr/td")#获取詳細列表所在的标签a
        price_list = driver.find_elements_by_xpath("/html/body/div[5]/div[1]/div[2]/div[2]/form[4]/div/div[*]/div[2]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr/td[1]/dl/dd/span")#获取価格列表所在的标签a
        address_list = driver.find_elements_by_xpath("/html/body/div[5]/div[1]/div[2]/div[2]/form[4]/div/div[*]/div[2]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr/td[1]/dl/dd")#获取住所列表所在的标签a
        station_list = driver.find_elements_by_xpath("/html/body/div[5]/div[1]/div[2]/div[2]/form[4]/div/div[*]/div[2]/div[2]/div[1]/div[2]/div/div[4]/table/tbody/tr/td[1]/dl/dd")#获取沿線・駅列表所在的标签a
        area_list = driver.find_elements_by_xpath("/html/body/div[5]/div[1]/div[2]/div[2]/form[4]/div/div[*]/div[2]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr/td[2]/dl/dd")#获取土地面積列表所在的标签a
        building_area_list = driver.find_elements_by_xpath("/html/body/div[5]/div[1]/div[2]/div[2]/form[4]/div/div[*]/div[2]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr/td[2]/dl/dd")#获取建物面積列表所在的标签a
        layout_list = driver.find_elements_by_xpath("/html/body/div[5]/div[1]/div[2]/div[2]/form[4]/div/div[*]/div[2]/div[2]/div[1]/div[2]/div/div[4]/table/tbody/tr/td[2]/dl/dd")#获取間取り列表所在的标签a
        building_date_list = driver.find_elements_by_xpath("/html/body/div[5]/div[1]/div[2]/div[2]/form[4]/div/div[*]/div[2]/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr/td[2]/dl/dd")#获取建物面積列表所在的标签a
        h_list = [] #保存列表
        for a in title_s:
            chapter_href = a.get_attribute("href")#帖子链接            
            
            if -1 != chapter_href.rfind('http'):
                h_list.append(chapter_href)           
        print("贴子总数：",len(h_list))
        return h_list
        
    #按帖子链接爬取内容
    def get_name_content(h_list):       
        chapters = []
        for url in h_list:
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            response = urlopen(req)
            html = response.read()
            soup = BeautifulSoup(html,"html5lib")
            title = soup.findAll('h1')[0].text          
            print("贴子title：" + title)
            chapters.append(title)
            content = soup.findAll(id=re.compile("postmessage.*"))[0]
            
            for string in content:
                st = str(string)
                if -1 != st.rfind('<br/>'):
                    continue
                else:
                    chapters.append(st)
                    #print(st)
            xiaochun.save_book(title,chapters)
            chapters = []
    
    #清洗文本格式，一次性写入txt文件：关键是调整格式
    def save_book(bookName,chapters):
        bookName = bookName.replace("\n","")
        bookname = downloadDir  + bookName + '.txt'       
        file = open(bookname, 'w+', encoding='utf-8')
        for i in chapters:        
            #file.write('\t')
            for ii in i:
                if ii.startswith('<div'):#去掉每章开头多余的<div……></div>
                    ii = ""
                file.write(ii)
            #file.write('\n')  #每写完一句，换行，控制文本格式
               
if __name__ == "__main__":
    chapter_urls = xiaochun.search()
    xiaochun.get_name_content(chapter_urls)