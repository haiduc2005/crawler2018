#coding=utf-8
from selenium import webdriver
from urllib.request import Request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import settings
#Firefox
driver=webdriver.Firefox()
url = settings.URL_VERIFY

driver.get(url)
#get&print all of the link
#for link in driver.find_elements_by_tag_name("a"):
#    print(link.get_attribute("href"))
##click()
#driver.find_element_by_xpath(xpath).click()
# driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/a[9]").click()# select DB
driver.find_element_by_xpath("/html/body/div[1]/header/div/div/div[2]/ul/li[6]/a/b").click()# サインイン/ログインを押下

driver.find_element_by_xpath("//*[@id='login']").clear()
driver.find_element_by_xpath("//*[@id='login']").send_keys(settings.VERIFY_ID)
driver.find_element_by_xpath("//*[@id='password']").clear()
driver.find_element_by_xpath("//*[@id='password']").send_keys(settings.VERIFY_PASS)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#driver.find_element_by_class_name("btn btn-primary").click()# login
driver.find_element_by_xpath("/html/body/div[1]/main/div/form/div[3]/button").click()# login
print(driver.get_cookies())
# ログインの状態で別ページにアクセスすることが可能
url = settings.URL_VERIFY_HOME
driver.get(url)
#driver.quit()