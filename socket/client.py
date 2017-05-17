#!/usr/bin/python
#coding:utf-8
import socket

client = socket.socket()

ip_port = ("localhost", 9999)
a = client.connect_ex(ip_port)
print a
while True:
	data = client.recv(1024)
	print data
	send_data = raw_input('please input data:')
	client.send(send_data)
	if send_data == 'exit':
		break

