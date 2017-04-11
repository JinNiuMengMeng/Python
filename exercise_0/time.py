#!/usr/bin/python
#-*- coding:UTF-8 -*-

import time
ticks = time.time()
print 'Now timestamp is:', ticks

localtimes = time.localtime(time.time())
print 'localtime is:', localtimes

localtimes = time.asctime(time.localtime(time.time()))
print 'localtime is', localtimes

print time.strftime("Year:" + "%Y-%m-%d\n" + "time:" + "%H:%M:%S", time.localtime())
