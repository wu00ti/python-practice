#!/usr/bin/python
#coding:utf-8

from urllib import request
import urllib
import re

def get_html(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def get_img(html):
    reg = r'src="(.*?\.jpg)" bdwater='
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html.decode())
    i = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg'%i)
        i+=1
html = get_html('http://tieba.baidu.com/p/5664377714')
print (get_img(html))
