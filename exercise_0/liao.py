#!/usr/bin/python
#-*- coding:utf-8 -*-
import urllib
import cstring

domain = 'http://www.liaoxuefeng.com'      #��ѩ�������
path = r'D:\share\\'  #htmlҪ�����·��

# һ��html��ͷ�ļ�
input = open(r'D:\share\0.html', 'r')
head = input.read()

# ��python�̳�������
f = urllib.urlopen("http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000")
home = f.read()
f.close()

# �滻���пո�س����������׺û�ȡurl��
geturl = home.replace("\n", "")
geturl = geturl.replace(" ", "")

# �õ�����url���ַ���
list = geturl.split(r'em;"><ahref="')[1:]

# ǿ��֢���ˣ�һ��Ҫ�ѵ�һ��ҳ��Ҳ�ӽ�ȥ������
list.insert(0, '/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000">')

# ��ʼ����url List
for li in list:
  url = li.split(r'">')[0]
  url = domain + url       #ƴ��url
  print url
  f = urllib.urlopen(url)
  html = f.read()

  # ���titleΪ��д�ļ���
  title = html.split("<title>")[1]
  title = title.split(" - ��ѩ��Ĺٷ���վ</title>")[0]

  # Ҫתһ���룬��Ȼ�ӵ�·����ͱ�����
  title = title.decode('utf-8').replace("/", " ")

  # ��ȡ����
  html = html.split(r'<!-- block main -->')[1]
  html = html.split(r'<h4>����֧��������д�����Ķ�����</h4>')[0]
  html = html.replace(r'src="', 'src="' + domain)

  # ����ͷ��β���������html
  html = head + html+"</body></html>"

  # ����ļ�
  output = open(path + "%d" % list.index(li) + title + '.html', 'w')
  output.write(html)
  output.close()
