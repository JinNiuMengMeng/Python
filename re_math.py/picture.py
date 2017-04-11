#!/usr/bin/python
#coding:utf-8
import urllib, urllib2, os

def url_open(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:52.0) Gecko/20100101 Firefox/52.0')
    response = urllib2.request.urlopen(url)
    html = response.read()
    return html

def get_page(url):
    url_content = url_open(url)
    a = url_content.find('"current-comment-page">[') + len('"current-comment-page">[')
    b = url_content.find(']', a)
    return url_content[a:b]
    
def find_imgs(page_url):
    page_content = url_open(page_url)
    img_list = []
    a = page_content.find('img src="')
    while a!= -1:
        b = page_content.find('"', a+15, a+255)
        if b != -1:
            img_list.append(page_content[a+9:b])
        else:
            b = a + 9
        a = page_content.find('img src="', b)
    for i in img_list:
        print i
    return img_list

def save_addrs(folder, img_addrs):
    for eath in img_addrs:
        filename = eath.split('/')[-1]
        with open(filename, 'wb') as fd:
            img = url_open(eath)
            f.write(img)

def download_mm(folder = 'OOXX', pages = 10):
    os.mkdir(folder)
    os.chdir(folder)

    url = 'http://jandan.net/ooxx'
    page = int(get_page(url))
    for i in range(pages):
        page -= i
        page_url = url + '/page-' + str(page) + '#comments'
        img_addrs = find_imgs(page_url)

#        save_addrs(folder, img_addrs)

if __name__ == '__main__':
    download_mm()
