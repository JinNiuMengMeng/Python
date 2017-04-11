#!/usr/bin/python
#coding:utf-8

'''
1.用for迭代num元素，用if判断num中的元素是否都是整型
2.当m迭代到最后一个元素时，使用max与min内置方法找到最大与最小值并返回
'''
def func(*num):
    for m in num:
        if isinstance(m, int):
            if m == num[-1]:
                return max(num), min(num)
        else:
            return '输入的参数必须为整型！'
print func(1, 2, 3, 23, 3, 345)
assert func(3, 4, 5, 56) == (56, 3)#验证函数func是否正确

'''
1.使用for循环迭代lstr中每一个字符串，判断是否都是字符串
2.使用if判断是否迭代到最后一个元素，当迭代到最后一个元素时，给元组lstr按照长度
排序，最后返回最后一个字符串
'''
str1 = 'abc'
str2 = 'abcd'
str3 = 'abcsadfgasdfgde'
def func_str(*lstr):
    for m in lstr:
        if isinstance(m, str):
            if m == lstr[-1]:
                str_list = sorted(lstr, key = lambda k:len(k))
                return str_list[-1]
            pass
        else:
            return '输入的参数必须为字符串'
print func_str(str1, str2, str3)

'''
第一种方法,使用pydoc,再使用os的popen方法执行字符串拼接的命令a
'''
import os
def get_doc(module):
    a = 'pydoc %s' % module
    txt = os.popen(a).read()
    return txt
print get_doc('urllib')
