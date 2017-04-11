#!/usr/bin/python
#coding:utf-8
class myException(Exception):
    def __init__(self, error, msg):
        self.args = (error, msg)
        self.error = error
        self.msg = msg
try:
    raise myException(1, 'my exception')
except Exception as e:
    print str(e)


print 'end'
