#!/usr/bin/python
#coding:utf-8
import os, urllib
import platform, logging
import subprocess
domainlist = ['xx.com', 'www.baidu.com', 'www.126.com']
def ping_url(url_list):
    for url in domainlist:
        system_name = platform.system()
        print system_name
        if system_name == 'Windows':
            command = 'ping -n 4 %s' % url
        elif system_name == 'Linux':
            command = 'ping -c 4 %s' % url
        else:
            logger.error('unexpected platfrom')
            raise TypeError, 'I do not know how to do it in other platform'
        pingUrl = subprocess.Popen(args = command, shell = True, stdout = subprocess.PIPE)
        pingUrl.wait()
        x = pingUrl.stdout.read()
        if (x.find('100')+1):
            logging.error(url)
ping_url(domainlist)
