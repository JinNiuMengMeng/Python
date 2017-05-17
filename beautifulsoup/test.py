#!/usr/bin/python
#--*-- coding:utf-8 --*--

import requests, urllib2
from bs4 import BeautifulSoup
from datetime import datetime

html_sample = '\
        <html> \
        <body> \
        <h1 id="title">Hello world 1</h1>\
        <h1 id="title">Hello world 2</h1>\
        <h1 id="title">Hello world 3</h1>\
        <a href="#" class="link">This is link1</a> \
        <a href="# link2" class="link">This is link2</a> \
        </body> \
        </html>'
soup = BeautifulSoup(html_sample, 'html.parser')
#header = soup.select('h1')
#print soup.text
#print header[0].text
#
#for alink in soup.select('#title'):
#    print alink
#
#for line in soup.select('.link'):
#    print line

#for link in soup.select('a'):
#    #print link['href']
#    print link
#    print link.text
#b = '<a href="#" qoo = 123 abc = 456> i am link</a>'
#soup2 = BeautifulSoup(b)
#print soup2.select('a')
#print soup2.select('a')[0]['qoo']
#print soup2.select('a')[0]['abc']
#print soup2.select('a')[0]['href']
#print soup2.select('a')[0].text
def url_open(url):
    head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
    req = urllib2.Request(url, None, head)
    html = urllib2.urlopen(req).read()
    return html
html = url_open('http://news.sina.com.cn/c/nd/2017-05-02/doc-ifyetwtf9611662.shtml')
soup1 = BeautifulSoup(html, 'html.parser')
header = soup1.select('#artibodyTitle')[0].text
timesource = soup1.select('.time-source')[0].contents[0].strip().encode('utf-8')
from_where = soup1.select('.time-source span a')[0].text
#print timesource, '\t', type(timesource), '\t', len(timesource)
dt = datetime.strptime(timesource, '%Y年%m月%d日%H:%M')
content = []
for p in soup1.select('#artibody p'):
    content.append(p.text.strip())
#print '\n'.join(content)

aut = soup1.select('.article-editor')[0].text.encode('utf8').strip('责任编辑：')
print header, '\t', dt.strftime('%Y-%m-%d %H:%M'), '\t', from_where, '\t', aut
