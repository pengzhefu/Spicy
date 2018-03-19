# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 15:39:23 2018

爬取中国大学排名

@author: pengz
"""

import requests
import bs4
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        #修改headers参数可以让爬虫模拟人操作浏览器的行为进行数据读取
#        r = requests.get(url, timeout = 60,headers = kv)#timeout时间是60s,如果是那种禁止爬虫的就可以这也模拟人用浏览器登录
        r = requests.get(url, timeout = 60)
        r.raise_for_status()#看信息有没有获得，如果返回值是404就转到except
        r.encoding = r.apparent_encoding#用内容的编码方式取代头部猜测的编码方式
#        print(r.request.headers,'\n')#属性是request，库是requests
        return r.text#返回内容 如果返回头部内容是r.headers
    except:
        return ""
    

#ulist是拿来存储大学名称和信息的二维列表，html是html页面的内容
def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:#tbody包含了所有大学的所有信息，然后每一个tr是一所大学的所有信息，用children进行下行遍历就是把每一个tr的所有内容看一遍
        if isinstance(tr, bs4.element.Tag):#isinstance函数用来判断类型的
            tds = tr('td')#tr里面的每个td都存了一种信息
            ulist.append([tds[0].string, tds[1].string, tds[2].string, tds[3].string, tds[4].string]) #用.stirng是为了获得每个tag里面的navigable string
    return ulist

#num是说想打印出哪几个学校信息
def printUnivList(ulist, num):
    print("{:^10}\t{:^10}\t{:^10}\t{:^10}\t{:^10}".format('排名','名称','省市','总分','指导得分'))
    for i in range(num):
        u = ulist[i]
        print("{:^10}\t{:^10}\t{:^10}\t{:^10}\t{:^10}".format(u[0],u[1],u[2],u[3],u[4]))
#    print('Suc' + str(num))
    
def main():
    uinfo = []#相当于初始化ulist，存储大学信息的二维列表
    url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
    html = getHTMLText(url)
    u_full_list = fillUnivList(uinfo, html)
    printUnivList(u_full_list,10)
    
if __name__ == '__main__':
    main()
    