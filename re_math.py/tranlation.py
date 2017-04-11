#!/usr/bin/python
#coding:utf-8
import urllib, json, urllib2, urlparse, time
i = 0
while True:
#    content = raw_input('请输入要翻译的语句或单词(输入"q!"退出):')
    content = '请输入要翻译的语句或单词(输入"q!"退出):'
    i += 1
    if content == "q!":
        break
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=dict2.index'
    #添加head的信息, 防止服务器自动屏蔽该爬虫程序, head可以将程序伪装成浏览器访问服务器
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    data = {}
    data['type'] = 'AUTO'
    data['i'] = content
    data['doctype'] = 'json'
    data['xmlVersion'] = '1.8'
    data['keyfrom'] = 'fanyi.web'
    data['ue'] = 'UTF-8'
    data['action'] = 'FY_BY_CLICKBUTTON'
    data['typoResult'] = 'true'
    data = urllib.urlencode(data).encode('utf-8')
    
    response = urllib.urlopen(url, data, head)
    html = response.read().decode('utf-8')
    #此时html为字符串, 所以不能用字典的形式进行索引
    #print '翻译结果为:%s' %(html['translateResult'][0][0]['tgt'])
    target = eval(html)#将字典型字符串直接转换成字典格式
    print '翻译结果为:%s -- %d' %(target['translateResult'][0][0]['tgt'], i)
#    time.sleep(0.1)
