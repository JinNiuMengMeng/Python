#!/usr/bin/python
#coding:utf-8
import urllib, urllib2
import requests

res = urllib2.Request('http://placekitten.com/g/300/300')
response = urllib2.urlopen(res)

cat_img = response.read()

with open('cat_500_600.jpg', 'wb') as f:
    f.write(cat_img)
print 'end'
