# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 02:10:55 2018

@author: pengz
"""
import requests
from bs4 import BeautifulSoup
import urllib
import re
import bs4
##定义爬取框架
#kv = {'User-Agent': 'Mozilla/5.0'}
#def getHTMLText(url):
#    try:
#        #修改headers参数可以让爬虫模拟人操作浏览器的行为进行数据读取
##        r = requests.get(url, timeout = 60,headers = kv)#timeout时间是60s,如果是那种禁止爬虫的就可以这也模拟人用浏览器登录
#        r = requests.get(url, timeout = 60)
#        r.raise_for_status()#看信息有没有获得，如果返回值是404就转到except
#        r.encoding = r.apparent_encoding#用内容的编码方式取代头部猜测的编码方式
#        print(r.request.headers,'\n')#属性是request，库是requests
#        return r.text#返回内容 如果返回头部内容是r.headers
#    except:
#        return "产生异常"
#
#url = "http://www.baidu.com"
#content = getHTMLText(url)
#print(content)

##构造url链接（相当于往搜索页面题交请求）这个的前提条件是知道网站的搜索接口
#def searchSth(keyword):
#    try:
#        kv = {'wd':keyword}#百度的搜索keyword格式是wd=blablabla
#        r = requests.get("http://www.baidu.com/s", timeout = 60,params = kv)#修改params参数可以往url链接对应页面提交请求
#        r.raise_for_status()
#        r.encoding = r.apparent_encoding
#        r.encoding = r.apparent_encoding
#        print(r.request.url)
#        print(len(r.text))
#    except:
#        print("爬取失败")
#keyword = 'Python'
#searchSth(keyword)

##爬取和存储图片
#path = 'D:/abc.jpg'
#url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1520165244244&di=bec16ee0bb7422fb32a21ba0e9b0d569&imgtype=0&src=http%3A%2F%2Fwww.th7.cn%2Fd%2Ffile%2Fp%2F2016%2F07%2F27%2F18c93c6ce20fd36483cca9e6fc99caa1.jpg'
#def searchPic(url):
#    try:
#        #这一步爬取
#        r = requests.get(url)
#        r.raise_for_status()
#        print(r.status_code)
#        #这一步存储
#        with open(path, 'wb') as f:
#            f.write(r.content)#response对象的r.content表示response内容的二进制形式,写进我们path的文件
#            f.close()
#    except:
#        print("Faliure")
#searchPic(url)

##BS库的使用
r = requests.get("https://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo, "html.parser")#html.parser是一个解释器，对demo进行html的解析，转成utf-8编码
#print(soup.prettify())
#print(soup.find_all(['a','b']))
#for link in soup.find_all('a'):
#    print(link.get('href'))#遍历整个a标签找到对应href里面的内容
#for tag in  soup.find_all(re.compile('b')):#用到正则表达式re库，表示以b开头的tag
#    print(tag.get_text())
#print(soup.find_all('a','py1'))

#title = soup.find('b').span #？还不知道span是干嘛的
#title = soup.find('b').get_text()#用find找相应标签和标签里内容,加上.get_text()可以去掉tag的名字,显示navigablestring
#print(title)
#print(soup.a.attrs)#attrs显示标签里的属性
#print(soup.a.string)#string显示一个标签对之间的navigablestring
#print(soup.p.comment)#显示标签里面的comment<! 开头的

#print(soup.prettify())#prettify函数能让解析后的html页面更友好的展示，其实就是在每个tag后加了个\n，也可以针对标签用
#print(soup.a.prettify())

##下行遍历
#print(soup.head.contents)
uo = []
for child in soup.find('body').children:
    if isinstance(child, bs4.element.Tag):
        print(child('b'))

#print("{:^10}\t{:^10}\t{:^10}".format(1,'b','c'))

##上行遍历
#print(soup.a.parent)
#for fujiedian in soup.a.parents:
#    ##因为soup本身也有parent，但是是空的，也就没有名字
#    if fujiedian is None:
#        continue
#    else:
#        print(fujiedian.name)
        
##平行遍历
#print(soup.a.next_sibling)
#print(soup.a.previous_sibling)
#for pingxing in soup.a.previous_sibling:
#    print(pingxing)
        











