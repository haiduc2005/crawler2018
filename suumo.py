# coding=utf-8

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

downloadDir = 'E:\\Down\\text\\suumo\\'  # ダウンロード場所


class Xiaochun():
    
    # 検索
    def search():
        driver = webdriver.Firefox()
        base_url = "https://suumo.jp/jj/bukken/ichiran/JJ012FC002/?ar=030&bknh_listmodeflg=2&bs=021&sc=13105&ta=13&po=0&pj=1&pc=100"
        driver.get(base_url)
        title_list = driver.find_elements_by_xpath("/html/body/div[5]/div[1]/div[2]/div[2]/form[4]/div/div[*]/div[2]/div[1]/h2/a")  # titleリストのタグa
        detail_list = driver.find_elements_by_xpath("/html/body/div[5]/div[1]/div[2]/div[2]/form[4]/div/div[*]/div[2]/div[2]/div[1]/div[2]/div/div[1]/table/tbody/tr/td")  # 詳細リストのタグa
        price_list = driver.find_elements_by_xpath("/html/body/div[5]/div[1]/div[2]/div[2]/form[4]/div/div[*]/div[2]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr/td[1]/dl/dd/span")  # 価格リストのタグa
        address_list = driver.find_elements_by_xpath("/html/body/div[5]/div[1]/div[2]/div[2]/form[4]/div/div[*]/div[2]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr/td[1]/dl/dd")  # 住所リストのタグa
        station_list = driver.find_elements_by_xpath("/html/body/div[5]/div[1]/div[2]/div[2]/form[4]/div/div[*]/div[2]/div[2]/div[1]/div[2]/div/div[4]/table/tbody/tr/td[1]/dl/dd")  # 沿線・駅リストのタグa
        area_list = driver.find_elements_by_xpath("/html/body/div[5]/div[1]/div[2]/div[2]/form[4]/div/div[*]/div[2]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr/td[2]/dl/dd")  # 土地面積リストのタグa
        building_area_list = driver.find_elements_by_xpath("/html/body/div[5]/div[1]/div[2]/div[2]/form[4]/div/div[*]/div[2]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr/td[2]/dl/dd")  # 建物面積リストのタグa
        layout_list = driver.find_elements_by_xpath("/html/body/div[5]/div[1]/div[2]/div[2]/form[4]/div/div[*]/div[2]/div[2]/div[1]/div[2]/div/div[4]/table/tbody/tr/td[2]/dl/dd")  # 間取りリストのタグa
        building_date_list = driver.find_elements_by_xpath("/html/body/div[5]/div[1]/div[2]/div[2]/form[4]/div/div[*]/div[2]/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr/td[2]/dl/dd")  # 建物面積リストのタグa
        h_list = []  # リストの保存
        for a in title_s:
            chapter_href = a.get_attribute("href")  # 物件ページのURL
            
            if -1 != chapter_href.rfind('http'):
                h_list.append(chapter_href)           
        print("物件の数：",len(h_list))
        return h_list
        
    # 物件ページのURLにより内容を取得
    def get_name_content(h_list):       
        chapters = []
        for url in h_list:
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            response = urlopen(req)
            html = response.read()
            soup = BeautifulSoup(html,"html5lib")
            title = soup.findAll('h1')[0].text          
            print("物件title：" + title)
            chapters.append(title)
            content = soup.findAll(id=re.compile("postmessage.*"))[0]
            
            for string in content:
                st = str(string)
                if -1 != st.rfind('<br/>'):
                    continue
                else:
                    chapters.append(st)
                    #print(st)
            Xiaochun.save_book(title, chapters)
            chapters = []
    
    # txt文件書き込み
    def save_book(bookName, chapters):
        bookName = bookName.replace("\n","")
        bookname = downloadDir  + bookName + '.txt'       
        file = open(bookname, 'w+', encoding='utf-8')
        for i in chapters:        
            # file.write('\t')
            for ii in i:
                if ii.startswith('<div'):  # 不要な<div……></div>を除く
                    ii = ""
                file.write(ii)
            # file.write('\n')  #改行


if __name__ == "__main__":
    chapter_urls = Xiaochun.search()
    Xiaochun.get_name_content(chapter_urls)
