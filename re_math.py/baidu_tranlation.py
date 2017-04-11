#!/usr/bin/python
#coding:UTF-8
import urllib, json, urllib2, urlparse

content = raw_input('please input str:')

url = 'http://fanyi.baidu.com/pcnewcollection?req=check'
data = {}
data['fanyi_src'] = content 
data['direction'] = 'zh2en'
data = urllib.urlencode(data).encode('utf-8')
response = urllib.urlopen(url, data)
html = response.read().decode('utf-8')
print html
#此时html为字符串, 所以不能用字典的形式进行索引
#print '翻译结果为:%s' %(html['translateResult'][0][0]['tgt'])
target = eval(html)#将字典型字符串直接转换成字典格式
print '翻译结果为:%s' %(target['translateResult'][0][0]['tgt'])
