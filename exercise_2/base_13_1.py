#!/usr/bin/python
#coding:utf-8
import sys
import string

buf = [11, 22, 24, 29, 30, 32]
buf.append(28) #将28加到列表的末端
num = buf.index(29) #找到29的位置
buf.insert(num+1, 57)  #在29后面插入元素57
buf[0] = 6  #将元素11修改成6
del buf[buf.index(32)] #找到32所在的位置,并删除
buf = sorted(buf)#将buf从小到大进行排序后,再复制给buf(不能使用sort,注意区别)
print buf



