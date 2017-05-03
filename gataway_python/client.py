#!/usr/bin/python
#coding:utf-8

import time
from md5 import make_md5
from GetPublicIp import get_public_ip
import socket
import uuid #用于获取mac地址

def get_key():
    now_time = time.time()
    timesamp = str(int(now_time))
    key = timesamp + make_md5(timesamp)[0:14]
    return key

def get_mac_address(): 
    mac_1 = uuid.UUID(int = uuid.getnode()).hex[-12:] 
    mac_2 = ''.join([mac_1[e:e+2] for e in range(0,11,2)])
    mac = mac_2.zfill(16).upper() #获取到的mac地址不足16位, 用零填充
    return mac
print get_public_ip()
