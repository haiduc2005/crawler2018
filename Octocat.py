import urllib.request
import requests
from bs4 import BeautifulSoup
import os
# サイト上の写真をキャッチしてローカルに保存する。

basic_url = "https://octodex.github.com"


def open_url(url):
    # r=urllib.request.urlopen(url)
    r = requests.get(url)
    print('start!')
    code = r.status_code
    if code != 200:
        print(u"リクエスト失敗")
    else:
        print(u"リクエスト成功")
        # html=r.content.decode('utf-8')
        return r.content


def get_image_list(content):
    list = []
    bs = BeautifulSoup(content, 'html.parser')
    cont = bs.find('div', 'content')
    imgs = cont.find_all('div', 'item-shell')
    # print(imgs)
    num = 0
    for img in imgs:
        img_find = img.find("img")
        img_src = img_find["data-src"]
        img_full_url = basic_url+img_src
        img_name = img_find["alt"]
        # print(img_name,img_full_url)
        # print(img_info)
        img_info = {}
        img_info['name']=img_name
        img_info['url'] = img_full_url

        list.append(img_info)
        # num+=1
        # print("index=",num)
        # print(img)
    return list


def download_images(img_list):
    basePath = os.path.join(os.getcwd(), r'octocat')  # カレントのパスを取得
    filename = os.path.join(basePath, 'octocat_img')
    if not os.path.exists(filename):
        os.makedirs(filename)
    os.chdir(filename)
    print(u'保存する:',filename)
    # 写真ダウンロード
    for img in img_list:
        print(u"ダウンロード中...", img["name"])
        pic = requests.get(img["url"])
        fp = open(img["name"] + '.png', 'wb')  # pngフォーマットに設定する
        fp.write(pic.content)
        fp.close()


if __name__ == '__main__':
    html = open_url(basic_url)
    img_list = get_image_list(html)
    # print(img_list)
    download_images(img_list)

    # print(html)
    # get_image_list(html)
