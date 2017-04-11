#!/usr/bin/python
#coding:utf-8
import urllib, urllib2, random

def url_open(url):
    head = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114Safari/537.36','Cookie':'AspxAutoDetectCookieSupport=1'}
    req = urllib2.Request(url, None, head)
    html = urllib2.urlopen(req).read()
    return html

iplist = ['121.193.143.249:80']

proxy_handler = urllib2.ProxyHandler({'http': random.choice(iplist)})

opener = urllib2.build_opener(proxy_handler)

r = opener.open('http://httpbin.org/ip')

print(r.read())

