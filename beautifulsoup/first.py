#!/usr/bin/python
#coding:utf-8
import urllib

from bs4 import BeautifulSoup

a = urllib.urlopen('http://www.baidu.com/').read()
#soup = BeautifulSoup(open('index.html'))
soup = BeautifulSoup(a)
print soup
print soup.title.string
print soup.p.string
print soup.script.string
