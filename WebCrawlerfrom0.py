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
kv = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
##kv用来模拟浏览器的头部
res = requests.get('http://bj.xiaozhu.com/',timeout = 60, headers = kv)
print(res)  ##如果成功返回200,不成功就是404，400之类的
print(res.raise_for_status())
print(res.text)

