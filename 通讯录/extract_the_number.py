#!/usr/bin/python
#coding:utf-8
import os, re

fp = open('haoma.txt', 'r')
content_1 = fp.read()
fp2 = open('2.txt', 'r')
pinyin_list = fp2.readlines()

'提取名字'
def extract_name(content):
    name_list = []
    p = r'N;CHARSET=UTF8:;\S+;;;'
    _list = re.findall(p, content)
    for i in _list:
        name_list.append(i.split(';')[-4])
    return name_list
name_list = extract_name(content_1)

'提取号码'
def extract_num(content):
    num_list= []
    p = r'TEL;CELL:\d{11}'
    haoma_list = []
    haoma = re.findall(p, content)
    for k in haoma:
        num_list.append(k.split(':')[-1])
    return num_list
num_list = extract_num(content_1)

print '*' * 50
for a in range(0, len(name_list)):
    print "'" + pinyin_list[a].replace(' \r\n', '\t') + name_list[a]
    print "'" + pinyin_list[a].replace('\r\n', 'hao ma \t') + num_list[a]
#for j in fp2.readlines():
#    print j
print 'end'
fp.close()
