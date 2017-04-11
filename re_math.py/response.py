#!/usr/bin/python
#coding:utf-8

import urllib

html = urllib.urlopen("http://www.baidu.com")
response = html.read()
print response.decode('utf-8')
