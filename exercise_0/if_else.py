#!/usr/bin/python
# -*-coding:UTF-8 -*-
a = 0
num = 0
j = 0
for num in range(10, 20): #迭代10到20支之间的所有数字
    for i in range(2, num):
        print 'a:%2d\tnum:%d\ti:%2d\tj:%2d' %(a, num, i, j)
        #帮助理解代码用的
        a += 1 #python中没有 i++或者++i
        if num % i == 0:
             j = num / i
             print '%d = %d * %d' % (num, j, i)
             a = 0
             break #break跳出的是第二个for循环
    else:#break循环跳出后
        print '%d 是质数' % num
        a = 0

