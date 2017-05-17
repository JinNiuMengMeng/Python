#!/usr/bin/python
#coding:utf-8
import urllib2, urllib, re, os
import time
from bs4 import BeautifulSoup

'已浏览器的方式打开连接,防止服务器屏蔽爬虫'
def url_open(url):
    head = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) pleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    req = urllib2.Request(url, None, head)
    html = urllib2.urlopen(req).read()
    return html

# '获取每一页博客的网址'
# def get_page_url(url):
#     '这是第一页'
#     url = 'http://blog.sina.com.cn/s/articlelist_1191258123_0_1.html'
#     content = url_open(url)

'获取每一页博客中所有文章的链接,将连接以列表的形式返回'
def get_article_url(html):
    p = r'a title="" target="_blank" href="([^"]+\.html)'
    art_list = re.findall(p, html)

    return art_list

'获取每篇文章的标题'
def art_title(url):
    art_content = url_open(url)
    a = art_content.find('titName SG_txta">') + len('titName SG_txta">')
    b = art_content.find('</h2>', a)
    return art_content[a:b]

'获取每篇文章的内容   ----   未完成,待处理'
def art_content(url):
    art_content = url_open(url)
    soup = BeautifulSoup(art_content, 'html')
    title = []
    title.append(soup.select('#articlebody div  h2')[0].text)
    for i in soup.select('#sina_keyword_ad_area2 div div'):
        a = i.text.strip()
        title.append(a)
    return ('\n'.join(title)).encode('utf-8')

'保存文章'
def save_article_file(page):
    j = 0
    for i in range(page):
        i += 1
        pwd = (os.getcwd()).split('\\')[-1]
        folder = '%d' %i
        print folder, 'Start'
        os.mkdir(folder)
        os.chdir(folder)

        url = 'http://blog.sina.com.cn/s/articlelist_1191258123_0_' + str(i) + '.html'
        html = url_open(url)
        article_list =  get_article_url(html)

        for eath_url in article_list:
            j += 1
            title = art_title(eath_url) 
            '只是文章题目,文件名需要在题目后面添加".txt"'
            Title = title + '.txt'
            content = art_content(eath_url)
            with open(Title, 'w') as fd:
                fd.write(content)
            print eath_url + '----%d' % j
            time.sleep(0.2)
        os.chdir(pwd)

if __name__ == '__main__':

   save_article_file(7)
#    url = 'http://blog.sina.com.cn/s/blog_4701280b0102eo83.html'
#    art_content(url)
