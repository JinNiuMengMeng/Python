#!/usr/bin/python
#coding:utf-8
import socket

server = socket.socket()
ip_port = ("localhost", 9999)
server.bind(ip_port)
server.listen(5)

while True:
	conn, address = server.accept()
	conn.send('hello')
	flag = True
	while flag:
		data = conn.recv(1024)
		print data
		if data == 'exit':
			flag = False
		conn.send('hahaha')
	conn.close()
