#!/usr/bin/python
#coding:utf-8

#用于测试linecache模块,可使用help(linecache)查看具体信息

import linecache

a = ['1\n', '2\n', '3\n', '4\n', '5\n', '6\n']
fp = open('./text.txt', 'w+')
fp.writelines(a)
fp.close()

print linecache.getline('text.txt', 2)

