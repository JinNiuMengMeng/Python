#!/usr/bin/python
#coding:utf-8

b = [1, 2, 3, 4, 5]
"方法1"
b.append(6)
b.append(7)
b.append(8)
print b
"方法2"
b = [1, 2, 3, 4, 5]
a = [6, 7, 8]
b.extend(a)
print b

b = [1, 2, 3, 4, 5]
"方法1"
print b[-1:-3:-1]
"方法2"
print b[:2:-1]

if 2 in b:
    print b.index(2)
