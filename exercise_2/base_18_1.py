#!/usr/bin/python
#coding:utf-8
import os
a = os.popen('python -m this').read()
a = a.replace('\n', ' ')
print '-'*20
print a
l = a.split(' ')
print '-'*20
print l
b = ['be', 'is', 'than']
print [(b_num, l.count(b_num)) for b_num in b]
