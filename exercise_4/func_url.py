#!/usr/bin/python
#coding:utf-8
__author__ = 'xie'
import urllib, logging

'''用于将日志输出到文件'''
#第一步:创建一个logger
logger = logging.getLogger()

#第二步:创建一个handler,用于写入日志文件
logfile = './log/logger.txt'
fh = logging.FileHandler(logfile, mode = 'a+')
#设置hangdler的输出格式
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
fh.setFormatter(formatter)

#第三步:将logger添加到handler里面
logger.addHandler(fh)
logger.setLevel(logging.NOTSET)

'''用于日志输出到屏幕'''
ch = logging.StreamHandler()#创建一个handler,用于将日志文件输出到控制台
ch.setLevel(logging.NOTSET)#输出到控制台的log等级
ch.setFormatter(formatter)
logger.addHandler(ch)#将logger添加到handler里面

io = ['http://www.baidu.com/', 'http://www.126.com/', 'htt/asdfasd.com',
'http://www.taobao.com/', 'http://www.3245543456.com/']
def func(urrlist):
    print urrlist
    for lis in urrlist:
        try:
            fp = urllib.urlopen(lis)
        except IOError:
            logging.error(('打开此链接失败: %s')%lis)
        else:
            print 'open succeed: %s' % lis
            print '*' * 50
        finally:
            fp.close()
    return None

func(io)
