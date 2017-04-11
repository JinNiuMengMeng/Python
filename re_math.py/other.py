#!/usr/bin/python
#coding:utf-8
import urllib, os
import urllib2


def url_open(url):
    
    head = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36','Cookie':'AspxAutoDetectCookieSupport=1'}
    req = urllib2.Request(url, None, head)
    html = urllib2.urlopen(req).read()
    return html


def get_page(url):
    url_content = url_open(url) 
    a = url_content.find('current-comment-page') + 23
    b = url_content.find(']', a)
    return url_content[a:b]
t = 1
p = 0
def find_imgs(page_url):
    global t
    global p
    p += 1
    print '第  %d  页' %p
    page_content = url_open(page_url)
    img_list = []
    all_img_list = []
    a = page_content.find('img src="')
    print 'a', a
    while a != -1:
        b = page_content.find('.jpg', a+15, a+255)
        if b != -1:
            img_list.append(page_content[a+9:b+4])
        else:
            b = a + 9
        a = page_content.find('img src="', b)
    for i in img_list:
        if i[0:3] != 'http':
            j = 'http:' + i
        else:
            j = i
        print j, '---', t
        t += 1
        all_img_list.append(j)
    return all_img_list


def save_addrs(folder, img_addrs):
    for eath in img_addrs:
        filename = eath.split('/')[-1]
        requs = url_open(eath)
        with open(filename, 'w') as fd:
            fd.write(requs)

def download_mm(folder = 'OOXX', pages = 10):
    os.mkdir(folder)
    os.chdir(folder)

    url = 'http://jandan.net/ooxx/'
    page = int(get_page(url))
    print page
    for i in range(pages):
        page -= i
        page_url = url + 'page-' + str(page) + '#comments'
        print page_url
        img_addrs = find_imgs(page_url)
        save_addrs(folder, img_addrs)

if __name__ == '__main__':
    download_mm('xxxxx', 20)
