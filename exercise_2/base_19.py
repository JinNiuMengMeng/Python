#!/usr/bin/python
#coding:utf-8
a = {'a':'value1', 'b':'value2', 'c':'value3', 'd':'value4'}
key_list = a.keys()
key_list.sort()
for x in key_list:
    print x, a[x]
