#!/usr/bin/python
#coding:utf-8
a = "aAsmr3idd4bgs7Dlsf9eAF"
a_list = list(a)
print a_list
b = [(m, a_list.count(m)) for m in a_list]
b.sort(key = lambda k:k[1], reverse = True)
print b
bint = 102324123499123
kb = bint >> 10
mb = bint >> 20
print "%s" %kb
print mb
a =  [1,2,3,6,8,9,10,14,17]
c = str(a)[1:-1].replace(', ', '')
print c
