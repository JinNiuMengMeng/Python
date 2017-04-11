#!/usr/bin/python
#coding:utf-8
fp = open('test.txt', 'r')
content = fp.read()
content = content.decode('utf-8')
print content
content = content.replace('2012', '2013')
print content
print len(content)
print content[len(content)/2:len(content)/2 + 5].decode('utf-8')
fp.close()
