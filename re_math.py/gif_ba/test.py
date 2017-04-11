#!/usr/bin/python
#coding:utf-8
import urllib2, re, sys

def url_open(url):
    head = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) pleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    req = urllib2.Request(url, None, head)
    html = urllib2.urlopen(req).read()
    return html



if __name__ == '__main__':

    url = 'http://tieba.baidu.com/p/4111034728'
    html = url_open(url)

    p = r'src="([^"]+\.jpg)'
    img_list = re.findall(p, html)

    for i in img_list:
        print i