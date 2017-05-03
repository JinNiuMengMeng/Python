#!/usr/bin/python
#coding:utf-8
import time

def time_counter(func):
    def wrap():
        first = time.time()
        func()
        print '运行 %s() 程序所花的时间为 %f'%(func.__name__, time.time() - first)
    return wrap

@time_counter
def say():
    print 'hello world'
    time.sleep(1)
    print 'hello world'
    time.sleep(1)
    print 'End...'
#say = time_counter(say)
say()
