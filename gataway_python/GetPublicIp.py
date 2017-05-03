#!/usr/bin/python
#coding:utf-8
import urllib2

url_1 = 'http://210.72.224.34:21532/SelectService/servlet/PowerBoxSelectIpPort'
url_2 = 'http://210.72.224.35:21532/SelectService/servlet/PowerBoxSelectIpPort'

def url_open(url):
    head = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}   
    req = urllib2.Request(url, None, head)
    html = urllib2.urlopen(req).read()
    return html

def get_public_ip(url1 = url_1, url2 = url_2):
    try:
        return  url_open(url1)
    except:
        print '获取IP失败,再次尝试获取'
        return  url_open(url2)
if __name__ == '__main__':
    print get_public_ip()
'''
http://210.72.224.34:21532/SelectService/servlet/PowerBoxSelectIpPort
http://210.72.224.35:21532/SelectService/servlet/PowerBoxSelectIpPort
'''
