#!/usr/bin/python
# -*-coding:UTF-8 -*-
a = 0
num = 0
j = 0
for num in range(10, 20):
    for i in range(2, num):
        print 'a:%2d\tnum:%d\ti:%2d\tj:%2d' %(a, num, i, j)
        a += 1
        if num % i == 0:
            j = num / i
            print '%d = %d * %d' %(num, j, i)
            a = 0
            break
    else:
        print '%d 是质数' %num
        a = 0
        print 'a:%2d\tnum:%d\ti:%2d\tj:%2d' %(a, num, i, j)
        print '*' * num
    print 'last'
