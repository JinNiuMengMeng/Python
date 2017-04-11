#!/usr/bin/python
#coding:utf-8
'''
第一页   http://tieba.baidu.com/f?kw=gif&ie=utf-8&pn=0
    |
    |帖子1------|第一页http://tieba.baidu.com    /p/4111034728?pn=1
    |帖子2      |第二页http://tieba.baidu.com    /p/4111034728?pn=2
    |帖子3      |第三页
    |帖子4
    |帖子5
    |帖子6
    |帖子7
    ...
第二页  http://tieba.baidu.com/f?kw=gif&ie=utf-8&pn=50
    |
    |帖子8------|第一页
    |帖子9      |第二页
    |帖子10     |第三页
    |帖子11
    |帖子12
    |帖子13
    |帖子14
    ...
第二页  http://tieba.baidu.com/f?kw=gif&ie=utf-8&pn=100
    |
    |帖子15------|第一页
    |帖子16      |第二页
    |帖子17      |第三页
    |帖子18
    |帖子19
    |帖子20
    |帖子21
    ...
'''
import urllib2, urllib, re, os

'已浏览器的方式打开连接,防止服务器屏蔽爬虫'
def url_open(url):
    head = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) pleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    req = urllib2.Request(url, None, head)
    html = urllib2.urlopen(req).read()
    return html

'获取gif吧每一页中所有帖子的链接,将以列表的形式返回'
def get_picture_url(url):
    html = url_open(url)
    p = r'/\w/\d{10}'
    pic_list = re.findall(p, html)
    list = []
    for i in pic_list:
        list.append('http://tieba.baidu.com' + i + '?pn=' + str(pic_list.index(i)+1))
    return list


'获取每一个帖子中所有子页的链接'
def get_Post_include_url(url):
    html = url_open(url)
    p = r'/\w/\d{10}.{4}\d'
    list_1 = re.findall(p, html)
    list_2 = list(set(list_1))#'去除相同的页码'
    list_2.sort()#'排序'
    list_2.insert(0, list_2[0][0:13])
    list_3 = []
    for i in list_2:
        list_3.append('http://tieba.baidu.com' + i)
    return list_3

'保存图片'
a = 1
totle = 1
def save_picture_file(url_list, folder, folder_1):
    p = r'height="\d{3}" src="([^"]+\.jpg)'

    global a, totle
    os.mkdir(str(a))
    os.chdir(str(a))
    for i in url_list:
        post_url_list = get_Post_include_url(i)
        for j in post_url_list:
            html = url_open(j)
            jpg_list = re.findall(p, html)

            for eath in jpg_list:
                print eath + '  ' + folder_1 + '  ' + str(a) +  '  ' + '下载中......%d' % totle
                totle += 1
                filename = eath.split('/')[-1]
                urllib.urlretrieve(eath, filename, None)
        totle = 1
    	a += 1
    	os.chdir('../')
    	os.mkdir(str(a))
    	os.chdir(str(a))
    os.chdir('../../')

if __name__ == '__main__':
    os.mkdir('gif_tieba_picture')
    os.chdir('gif_tieba_picture')
    for page in range(2):
        url = 'http://tieba.baidu.com/f?kw=gif&ie=utf-8&pn=' + str(page*50)

        pwd = (os.getcwd()).split('/')[-1]
        folder_1 = '第%s页' % str(page+1)
        print folder_1 + '下载中......'
        os.mkdir(folder_1)
        os.chdir(folder_1)

        post_url_list = get_picture_url(url)
        save_picture_file(post_url_list, pwd, folder_1)
