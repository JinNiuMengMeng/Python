#!/usr/bin/python
#coding:utf-8

studentinfo = {'liming':{'name':'李明', 'age':25,'score':{'chinese':80,'math':75, 'english':85}}}
studentinfo['zhangqiang'] = {'name':'张强', 'age':23, 'score':{'chinese':75,'math':82, 'english':78}}
studentinfo['liming']['score']['python'] = 60
studentinfo['zhangqiang']['score']['python'] = 60
studentinfo['zhangqiang']['score']['math'] = 100
del studentinfo['liming']['age']
a = studentinfo['zhangqiang']['score'].values()
print studentinfo
a.sort()
print a
