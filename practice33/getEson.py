import requests
import json
from pyecharts import Bar
from wordcloud import WordCloud
import matplotlib.pyplot as plt

url = 'https://music.163.com/weapi/v1/resource/comments/R_SO_4_551816010?csrf_token=5eb4c5c298d62d5428d29089f49d70d1'
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
'Referer': 'https://music.163.com/song?id=551816010',
'Origin': 'https://music.163.com',
'Host': 'music.163.com'
    }

#数据加密
user_data={
'params': 'KNPWyk7WLKrbiVJacAXcO/fCIB7TBqBnwirtIZEzGL24VGy1JkoN6otUVxcgKHIAh1/hK45GqQkkdA6/5GiyHN5/k5GUgEDgdjyUFFkFwv7TOgi9LSYJORSwbmExoKnRKmmNXgFIHIuXd/fC7HfXuxUbJ7LsL/wjASpXglHPVx+76dn9BoXOJMKsErvb3JD57bIwr8OwbxKoYK2DPjlJOBE++tDkIvkfibkBG+IT6Tw=',
'encSecKey': '602b575fd78f9be963f0795e8058254e9a5a78dc824f10c117be4df67364c746b4cc0999112f2d6f2572ae94cbd58646e0442ca541fdd6d52e5f197efdb743afc66b5367095e221caf26be0fc49d18d0b25c3edace6cd49fc17f5813ad09165df67828abc8672d44877a180e17fe0c82a23be619088f2abea33ac025b2ccb57a'
    }

response = requests.post(url,headers=headers,data=user_data)

data = json.loads(response.text)
hotcomments = []
for hotcomment in data['hotComments']:
    item = {
        'nickname':hotcomment['user']['nickname'],
        'content':hotcomment['content'],
        'likedCount':hotcomment['likedCount']
        }
    hotcomments.append(item)

#获取用户点赞数和评论
content_list = [content['content'] for content in hotcomments]
nickname = [content['nickname'] for content in hotcomments]
liked_count = [content['likedCount'] for content in hotcomments]


#使用pyecharts绘制图表
bar = Bar("热评中点赞数实例图")
bar.add("评论",nickname,liked_count,is_more_utils=True,is_stack=True,mark_line=["min","max"],mark_point=["average"])
bar.render()

'''#制作词云图展示
content_text = "".join(content_list)
wordcloud = WordCloud(font_path=r"simhei.ttf",max_words=200).generate(content_text)
plt.figure()
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis('off')
plt.show()'''