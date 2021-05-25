# coding=utf-8
import csv
from selenium import webdriver
import os

downloadDir = './sns/'  # ダウンロード後の保存場所
if os.path.exists(downloadDir) == False:  # フォルダ有り無しチェック
    os.makedirs(downloadDir)  # 创建文件夹


class xiaochun():

    # 搜索
    def search():
        driver = webdriver.Firefox()
        base_url = "http://www.tokyocn.com/activity.php?upid=1&page="
        # c = open("test-01.csv", "wb")  # ファイル書き込み
        with open(downloadDir + 'act.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(["番号", "活动内容", "場所"])

            for i in range(40, 59):
                url = base_url + str(i)
                driver.get(url)
                hiking_list = driver.find_elements_by_xpath("/html/body/div[4]/div[2]/div[1]/div[2]/div[1]/ul/li[*]/div[3]/a/h4")  # 活动内容
                address_list = driver.find_elements_by_xpath("/html/body/div[4]/div[2]/div[1]/div[2]/div[1]/ul/li[*]/div[3]/p[2]")  # 場所
                for j in range(10):
                    tlist = []
                    tlist.append(10 * (i - 1) + j + 1)
                    tlist.append(hiking_list[j].text)
                    tlist.append(address_list[j].text)
                    writer.writerow(tlist)
        f.close()

if __name__ == "__main__":
    chapter_urls = xiaochun.search()
