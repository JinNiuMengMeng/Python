#!/usr/bin/python
#coding:UTF-8

import threading, time
rlock = threading.RLock()
wlock = threading.RLock()

def write_file():
    fp = open('thread.txt', 'w')
    for i in range(0, 10):
        fp.write(str(i) + '\n')
        time.sleep(0.5)
    fp.close

def read_file():
    fd = open('thread.txt', 'r')
    for j in range(0, 10):
        print fd.read()
        time.sleep(0.5)
    fd.close()

wlock.acquire() #加锁
write_thread = threading.Thread(target = write_file)
write_thread.start()
wlock.release() #释放锁
time.sleep(1)
rlock.acquire() #加锁
read_thread = threading.Thread(target = read_file)
read_thread.start()
rlock.release() #释放锁
write_thread.join()
read_thread.join()
