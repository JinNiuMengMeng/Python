#!/usr/bin/python
#coding:utf-8
import sys
a = "中文编码"
print sys.getrefcount('中文编程')
b = a
c = a
a = "python编程"
b = u'%s' % a.decode('utf-8')
d = "中文编程"
e = a
c = b
b2 = a.replace('中', '中')
print sys.getrefcount('中文编程')

print sys.getrefcount('Python编程')
