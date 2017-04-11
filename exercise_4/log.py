#!/usr/bin/python
#coding:utf-8
import logging

logger = logging.getLogger()

hdlr = logging.FileHandler('/home/heng/Git_store/Python/exercise_4/log.txt')

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

hdlr.setFormatter(formatter)

logger.addHandler(hdlr)

logger.setLevel(logging.NOTSET)

logger.debug('this is a debug message')

logger.error('this is an error message')
