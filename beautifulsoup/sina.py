#!/usr/bin/python
#coding:utf-8
import urllib2
from bs4 import BeautifulSoup
from lxml import etree as ET
url = 'http://money.163.com/special/pinglun/'
rel = []

'打开链接'
def url_open(url):
    head = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    req = urllib2.Request(url, None, head)
    html = urllib2.urlopen(req).read()
    return html.decode('gbk')


html = url_open(url)
soup = BeautifulSoup(html, "lxml")
for eath in soup.find_all('div', attrs = {'class':'item_top'}):
    for i in eath.h2.children:
        url = i.get('href')
        title = eath.a.string
        creat_at = eath.span.string
        rel.append({'title':title, 'creat_at':creat_at, 'url':url})
for result in rel:
    for key in result:
        print result[key],
    print ''
'''
<div class="item_top">
<h2><a href="http://money.163.com/15/1219/12/BB6SGNBI002551G6.html">宝能作为门
口野蛮人是坏人吗</a></h2>
<a class="newsimg" href="http://money.163.com/15/1219/12/BB6SGNBI002551G6.html"
lang="http://img1.cache.netease.com/stock/2015/12
/19/20151219123414d634a_550.jpg" title="宝能作为门口野蛮人是坏人吗"><img alt="
宝能作为门口野蛮人是坏人吗"
src="http://s.cimg.163.com/stock/2015/12/19/20151219123414d634a_550.jpg.119x83.jpg"/></a>
<p>[摘要：目前来说，宝能系只不过玩了发达国家几十年来一直在玩的游戏，也就是”恶
意”+”杠杆”的并购。宝能系如此看重“控制”万科，是否
在打万科现金的主意？]原标题：[亦观察] No.671 宝能作为门口的野蛮人，是坏人吗?
“谁的万科”，这几天不知道有多少新闻写过这个  ...<br/>
<span class="time">2015-12-19 12:31:57</span>
</p>
</div>
'''


#    print eath
#    result = eath.get_text().split('|')
#    for item in result:
#        print item
#    print type(eath.a.string), type(eath.span.string)
#    rel2['title'] = eath.a.string.encode('gbk')
#    rel2['creat_at'] = eath.span.string
#    print rel2
#    for i in eath.h2.children:
#        rel.append({'title':eath.a.string, 'creat_at':eath.span.string.encode('gbk'), 'url':i.get('href')})
#    for i in rel:
#        print i

