#coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import settings

#Firefox
driver=webdriver.Firefox()
url = 'https://www.microsoft.com/ja-jp/events/decode/2018/'
#url2 = 'https://www.event-marketing.jp/events/decode/2018/register/change/MyPage.aspx'

driver.get(url)

first_windows=driver.current_window_handle
driver.find_element_by_xpath("/html/body/div[1]/div/div/span[2]/section/div/div/header/div[1]/div/div[2]/div/div/div/div[1]").click()

#all_handles=driver.window_handles
#for handle in all_handles:
#    if handle!=first_windows:
#        driver.switch_to_window(handle)
#w = driver.window_handles
#driver.switch_to_window(w[0])

driver.find_element_by_css_selector("#i0116").send_keys(settings.MS_ID)
time.sleep(3)
#Create = driver.find_element_by_css_selector("#idSIButton9")
#WebDriverWait(driver, 10).until_not(EC.visibility_of_element_located((By.CLASS_NAME, "inline-block")))
#Create.click()

#wait = WebDriverWait(driver, 10)
#element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='idSIButton9']")))
#element.click()

driver.find_element_by_xpath("//*[@id='idSIButton9']").click()# login
driver.find_element_by_xpath("//*[@id='i0118']").clear()
driver.find_element_by_xpath("//*[@id='i0118']").send_keys(settings.MS_PASS)
time.sleep(3)
driver.find_element_by_xpath("//*[@id='idSIButton9']").click()# login
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[2]/div/div[4]/nav/ul/li[8]/a").click()# my page

time.sleep(4)
all_handles=driver.window_handles
for handle in all_handles:
    if handle!=first_windows:
        driver.switch_to_window(handle)

#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#link = driver.find_element_by_xpath("//*[@id='ContentPlaceHolder1_lbtnDownloadAft']").click()
#driver.execute_script('arguments[0].click();', link)

for link in driver.find_elements_by_tag_name("a"):
    print(link.get_attribute("href"))
driver.find_element_by_xpath("//*[@id='ContentPlaceHolder1_lbtnDownloadAft']").click()
#driver.find_element_by_css_selector("#ContentPlaceHolder1_lbtnDownloadAft").click()
#ブレイクアウトセッション
target = driver.find_element_by_xpath("/html/body/div/main/form/article/div[2]/div/div/div/table/tbody/tr[3]/td/h2")
#ある場所までスクロールする
driver.execute_script("arguments[0].scrollIntoView();", target)
#driver.quit()