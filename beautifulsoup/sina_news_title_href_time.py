#!/usr/bin/python
#coding:utf-8
import urllib2
from bs4 import BeautifulSoup

def open_url(url):
    head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
    req = urllib2.Request(url, None, head)
    html = urllib2.urlopen(req).read()
    return html

url_1 = 'http://news.sina.com.cn/china/'
url_2 = 'http://news.sina.com.cn/world/'
content_html = open_url(url_2)
soup = BeautifulSoup(content_html, 'html.parser')
#print soup
for news in soup.select('.news-item'):
    if len(news.select('h2')) > 0:
        h2 =  news.select('h2')[0].text
        a = news.select('a')[0]['href']
        time = news.select('.time')[0].text
        print time, h2, a

