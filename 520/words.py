# -*- coding:UTF-8 -*-
from __future__ import unicode_literals
import requests
import itchat
import time

def get_news():
    url = "http://open.iciba.com/dsapi"
    r = requests.get(url)
    contents = r.json()['content']
    translation = r.json()['translation']
    return contents,translation

def send_news():
    try:
        itchat.auto_login(hotReload=True)
        my_friend = itchat.search_friends(name=u'文涛')
        WenTao = my_friend[0]["UserName"]
        message1 = str(get_news()[0])
        content = str(get_news()[1][17:])
        message2 = str(content)
        message3 = "来自你的好友"
        itchat.send(message1,toUserName=WenTao)
        itchat.send(message2,toUserName=WenTao)
        itchat.send(message3,toUserName=WenTao)
        t = time(86400,send_news())
        t.start()
    except:
        message4 = u"oh bug /(ToT)/~~"
        itchat.send(message4,toUserName=WenTao)


if __name__ == '__main__':
    send_news()

