#!/usr/bin/python
#coding:utf-8
import threading
import time

b_time = time.time()
def a():
    print 'a begin'
    time.sleep(1)
    print 'a end'
def b():
    print 'b begin'
    time.sleep(1)
    print 'b end'
a_thread = threading.Thread(target = a)
b_thread = threading.Thread(target = b)
a_thread.start()
b_thread.start()
a_thread.join()
b_thread.join()
print time.time() - b_time
