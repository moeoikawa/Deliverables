import requests
import urllib.request
from bs4 import BeautifulSoup
import lxml


#スクリプトを実行する前に
#・Python3系をインストールする
#・importに書かれているモジュールをインストールする（pip install XXXX）


#ファイル名
name = "aaa.txt"

#保存先
path = "C:/Users/moeoi/Desktop/python/test/" + name

#キーワードの指定
list_keyword = ['プロジェクションマッピング', '広告']


if list_keyword:
    #Google検索の実施
    search_url = 'https://www.google.co.jp/search?hl=ja&num=100&q=' + ' '.join(list_keyword)
    res_google = requests.get(search_url,timeout = 1)
    res_google.raise_for_status()

    #BeautifulSoupで掲載サイトのURLを取得
    bs4_google = BeautifulSoup(res_google.text, 'lxml')
    for url in bs4_google.find_all("a"):
        tag = url.get("href")
        #余計な文字を消す
        link = tag.replace('/url?q=', '')
        link2 = link[:-88]
        if 'https://' in link2 or 'http://' in link2:
            link3 = link2

            #書き込み
            #modeは「w」ではなく「a」にする。w:上書き、a:追記
            with open(path, mode='a', encoding='UTF-8') as f:
                f.write(link3 + '\n'+'\n')

print("検索結果を" + name + "に書き込みました")
