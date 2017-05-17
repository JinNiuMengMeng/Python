#!/usr/bin/env python
#coding:utf-8

from model.test import Test

def main():
    user = raw_input('usrname:')
    pwd = raw_input('pasword:')
    test2 = Test()
    result = test2.checkValidate(user, pwd)
    if not result:
    	print 'username or password is wrong!!'
    else:
    	print 'In system'
    	print result

if __name__ == "__main__":
    main()
