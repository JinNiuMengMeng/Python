#!/usr/bin/python
#coding:utf-8
import hashlib   

def make_md5(timesamp):
    m2 = hashlib.md5()   
    m2.update(timesamp)   
    return m2.hexdigest()   
