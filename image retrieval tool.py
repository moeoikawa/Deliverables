import requests
import urllib.request
from bs4 import BeautifulSoup
import lxml
import os , sys

word = sys.argv[1]

URL = "https://search.yahoo.co.jp/image/search?p={0}&oq=&ei=UTF-8&save=0".format(word)
res = requests.get(URL,timeout = 1)

soup = BeautifulSoup(res.text,'lxml')
body = soup.find_all("body")

img = soup.find_all(alt = "「{0}」の画像検索結果".format(word))

for i in range(len(img)):
    dir_name = "./{0}/".format(word)
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    filepath = "./{0}/{0}_{1}.jpg".format(word,i)
    urllib.request.urlretrieve(img[i]["src"],filepath)