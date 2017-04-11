#!/usr/bin/python
#coding:utf-8
import logging

logger = logging.getLogger()
hdlr = logging.FileHandler('/home/heng/Git_store/Python/exercise_4/file.txt')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.NOTSET)

def func(filename):
    try:
        file_fp = open(filename, 'r')
        content = file_fp.read()
    except IOError:
        print ('read finame is failed \'%s\'') % filename
        logger.error(('read finame is failed \"%s\"') % filename)
    else:
        print 'read filename succeed'
        return content
    finally:
        file_fp.close()

print func('abc.txt')
