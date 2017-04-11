#!/usr/bin/python
#coding:utf-8
import webbrowser as web
import time, os, random
count = random.randint(2, 4)
j = 0
while j < count:
    i = 0
    while i <= 9:
        web.open_new_tab('https://www.baidu.com/')
        i += 1
        time.sleep(0.8)
    else:
        os.system('taskkill /F /IM chrome.exe')
        print j, 'times closing Brower!'
    j += 1
