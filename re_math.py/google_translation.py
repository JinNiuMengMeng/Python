#!/usr/bin/python
#coding:UTF-8
import urllib, json, urllib2, urlparse

content = raw_input('please input str:')
url = 'http://translate.google.cn/'
#url = 'http://translate.google.cn/translate_a/single?client=t&sl=zh-CN&tl=en&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&source=bh&ssel=0&tsel=0&kc=1&tk=741980.851996&q=%E6%88%91%E4%B8%8D%E7%9F%A5%E9%81%93'
data = {}
data['client'] = 't'
data['sl'] = 'zh-CN'
data['tl'] = 'en'
data['hl'] = 'zh-CN'
data['dt'] = 'at'
data['dt'] = 'bd'
data['dt'] = 'ex'
data['dt'] = 'ld'
data['dt'] = 'md'
data['dt'] = 'qca'
data['dt'] = 'rw'
data['dt'] = 'rm'
data['dt'] = 'ss'
data['dt'] = 't'
data['ie'] = 'UTF-8'
data['oe'] = 'UTF-8'
data['source'] = 'bh'
data['ssel'] = '0'
data['tsel'] = '0'
data['kc'] = '1'
data['tk'] = '741980.851996'
data['q'] = content

data = urllib.urlencode(data).encode('utf-8')
response = urllib.urlopen(url, data)
html = response.read().decode('utf-8')
print html
#此时html为字符串, 所以不能用字典的形式进行索引
#print '翻译结果为:%s' %(html['translateResult'][0][0]['tgt'])
target = eval(html)#将字典型字符串直接转换成字典格式
print '翻译结果为:%s' %(target['translateResult'][0][0]['tgt'])


