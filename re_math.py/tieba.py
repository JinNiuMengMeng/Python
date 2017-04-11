#!/usr/bin/python
#coding:utf-8
import urllib2, urllib, re

def url_open(url):
    head = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    req = urllib2.Request(url, None, head)
    html = urllib2.urlopen(req).read()
    return html

def get_jpg(html):
    p = r'img class="BDE_Image" src="([^"]+\.jpg)'
    imglist = re.findall(p, html)

    for eath in imglist:
        filename = eath.split('/')[-1]
        urllib.urlretrieve(eath, filename, None)
    print 'Done'

if __name__ == '__main__':
    url = 'https://tieba.baidu.com/p/5042355028'
    get_jpg(url_open(url))

