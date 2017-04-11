#!/usr/bin/python
#coding:utf-8
a = (1, 4, 5, 6, 7)
if 4 in a:
    print '4 in a:', a.index(4)

"元组a是不可变对象,不能直接修改, 下面通过列表的方式转换"
b = list(a) #将元组a转换为列表b
b[b.index(5)] = 8 #找到5的位置,将其赋值为8
a = tuple(b) #再将列表b转换成元组a
print a
