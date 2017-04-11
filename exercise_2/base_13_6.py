#!/usr/bin/python
#coding:utf-8
setinfo = set('acbdfem')
finfo = set('sabcdef')
"第一题"
setinfo.add('adc')
"第二题"
setinfo.remove('m')
"第三题"
print setinfo & finfo
print setinfo | finfo

print setinfo
