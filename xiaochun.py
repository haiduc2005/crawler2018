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


downloadDir = 'E:\\Down\\text\\sns\\'#下载后存放目录

class xiaochun():
    
    #搜索
    def search():
        driver = webdriver.Firefox()
        base_url = "https://www.incnjp.com/forum-92-1.html"
        driver.get(base_url)
        #login_url = "https://www.incnjp.com/member.php?mod=logging&action=login"
        #driver.get(login_url)
        #driver.find_element_by_xpath("//*[@id='username_LUyc9']").send_keys("id")
        #driver.find_element_by_xpath("//*[@id='password3_LUyc9']").send_keys("pass")
        #driver.find_element_by_xpath("/html/body/div[6]/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/form/div/div[6]/table/tbody/tr/td[1]/button").click()  # login

        a_s = driver.find_elements_by_xpath("/html/body/div[6]/div[4]/div/div/div[4]/div[2]/form/table/tbody[*]/tr/th/a[2]")#获取帖子链接列表所在的标签a
        #driver.implicitly_wait(20)
        urls = [] #保存本页面所有帖子链接列表
        for a in a_s:
            chapter_href = a.get_attribute("href")#帖子链接            
            
            if -1 != chapter_href.rfind('http'):
                urls.append(chapter_href)           
        print("贴子总数：",len(urls))
        return urls
        
    #按帖子链接爬取内容
    def get_name_content(urls):       
        chapters = []
        for url in urls:
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