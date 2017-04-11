#!/usr/bin/python
#coding:utf-8
b = [23, 45, 22, 44, 25, 66, 78]
"第一题"
print [m for m in b if m % 2 == 1] 
#for后面的循环是寻找列表b中奇数,然后再把这些数据放在表达式m中
"第二题"
print ["the content %s" % n for n in b[0:2]]
"第三题"
print [m + 2 for m in b]
