# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 02:26:46 2019

@author: pengz
"""

##########Some funcs for string##############
str1 = 'www.baidu.com'
list1 = str1.split('.')

str2 = '***www.baidu.com***'
str3 = str2.strip('*')

str4 = 'www.baidu.com'
str5 = str4.replace('baidu','google')

str6 = '{} is my love'.format('google')

#import lxml
import requests
from bs4 import BeautifulSoup
kv = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
##kv用来模拟浏览器的头部
#res = requests.get('http://bj.xiaozhu.com/',timeout = 60, headers = kv)
#print(res)  ##如果成功返回200,不成功就是404，400之类的
#print(res.raise_for_status())
#print(res.text)

##用try的方式
url = 'http://bj.xiaozhu.com/'
try:
    #修改headers参数可以让爬虫模拟人操作浏览器的行为进行数据读取
    r = requests.get(url, timeout = 60,headers = kv)#timeout时间是60s,如果是那种禁止爬虫的就可以这也模拟人用浏览器登录
#    r = requests.get(url, timeout = 60)
    r.raise_for_status()#看信息有没有获得，如果返回值是404就转到except
    soup = BeautifulSoup(r.text,'html.parser')   ##对通过requests库返回的内容进行html解析，符合正常格式
                                                    ##当前用的就是html解析器，还有别的解析器
#    print(soup.prettify())  ##prettify函数还能针对标签使用
    print(soup.find_all('div',"pop_column"))   ##用的是函数的两个参数，一个是tag：div,一个是tag的attribute:pop_column
#    r.encoding = r.apparent_encoding#用内容的编码方式取代头部猜测的编码方式
#        print(r.request.headers,'\n')#属性是request，库是requests
#    print(r.text)#返回内容 如果返回头部内容是r.headers
except:
     print("Something wrong")
     
     
#page_list > ul > li:nth-child(1) > div.result_btm_con.lodgeunitname > div:nth-child(1) > span > i