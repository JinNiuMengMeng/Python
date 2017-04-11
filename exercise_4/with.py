#!/usr/bin/python
#coding:utf-8
'''普通打开文件的方法'''
fp = open('a.txt', 'r')
fp.read()
fp.close()

'''用with关键字打开文件'''
with open('b.txt', 'r') as fd:
    fd.read()
