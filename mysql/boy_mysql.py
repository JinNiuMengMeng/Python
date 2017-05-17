#!/usr/bin/python
#coding:utf-8

import MySQLdb

db = MySQLdb.connect("localhost", "root", "123456", "08day5")

'以元组的形式返回数据'
#cursor = db.cursor()

"以字典的形式返回数据, 包括格式为{'字段名':'数据'}"
cursor = db.cursor(cursorclass = MySQLdb.cursors.DictCursor)

'增加数据'
sql_1 = "insert into test1(name, addr) values(%s, %s)"
params = ('zhang', 'fujian')
cursor.execute(sql_1, params)

'删除数据表中id = 1的一项'
sql_2 = "delete from test1 where id = 1"
cursor.execute(sql_2)

'修改数据'
sql_3 = "update test1 set name = %s where id = 21"
params = ('ZHANGasdf',)
cursor.execute(sql_3, params)

'打开一次数据库,插入多条数据'
li = [('alex', 'usa'), ('sb', 'haha'),]
sql_4 = "insert into test1(name, addr) values(%s, %s)"
params = (li)
cursor.executemany(sql_4, params)

'查询数据'
recount = cursor.execute("select * from test1 where id > 1")

'返回查到的所有数据行'
#data = cursor.fetchall()

'返回一条查到的数据'
data = cursor.fetchone()
print data

'绝对定位, 回到找到的第一条数据前的位置'
cursor.scroll(0, mode = 'absolute')

data = cursor.fetchone()
print data

'相对定位, 回到上一条前的位置'
cursor.scroll(-1, mode = 'relative')

data = cursor.fetchone()
print data

'提交以上数据库操作,将数据写入到本机数据库'
db.commit()

'获取自增id当前的值'
print cursor.lastrowid

cursor.close()
db.close()

#print recount
#for i in data:
#    print i
