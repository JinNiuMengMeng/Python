#!/usr/bin/python
#coding:utf-8
import urllib2, re
def url_open(url):
    head = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) pleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    req = urllib2.Request(url, None, head)
    html = urllib2.urlopen(req)
    return html

def get_article_url(html):
    p = r'a title="" target="_blank" href="([^"]+\.html)'
    art_list = re.findall(p, html, None)

    for eath in art_list:
    	print eath
    
def save_article_file(article_list):
    pass

if __name__ == '__main__':
   url = 'http://blog.sina.com.cn/s/articlelist_1191258123_0_1.html'
   article_list =  get_article_url(url_open(url))
#   save_article_file(article_list)

