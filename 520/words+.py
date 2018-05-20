# -*- coding:UTF-8 -*-
from __future__ import unicode_literals
from threading import Timer
from wxpy import *
import requests

bot = Bot(console_qr=2,cache_path="botoo.pkl")

def get_news():
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    contents = r.json()['content']
    translation = r.json()['translation']
    return contents,translation

def send_news():
    try:
        my_friend = bot.friends().search(u'文涛')[0]
        my_friend.send(get_news()[0])
        my_friend.send(get_news()[1][5:])
        my_friend.send(u"来自你的朋友!")
        t = Timer(86400,send_news)
        t.start()
    except:
        my_friend = bot.friends().search('文鑫龙')[0]
        my_friend.send(u"发送失败")

if __name__ == "__main__":
    send_news()
