#!/usr/bin/python
#coding:utf-8

import MySQLdb

'打开数据库链接, connect(主机, 数据库登录名, 数据库密码, 要链接的数据库名称)'
db = MySQLdb.connect("localhost", "root", "123456", "08day5")
'使用cursor()方法获取操作游标'
cursor = db.cursor()

'首先执行下面语句, 如果EMPLOYEE数据库表存在,则删除'
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

'创建数据库表'
sql_1 = """CREATE TABLE EMPLOYEE(
    FIRST_NAME CHAR(20) NOT NULL,
    LAST_NAME CHAR(20),
    AGE INT,
    SEX CHAR(1),
    INCOME FLOAT)"""

'在数据表中插入数据'
sql_2 = """INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES('MAC', 'MOhan', 20, 'M', 2000)"""
sql_2_1 = """INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)VALUES('Tom', 'limei', 40, 'w', 4000)"""

'查询INCOME大于1000的信息'
sql_3 = """SELECT * FROM EMPLOYEE WHERE INCOME > 1000"""

'数据库更新操作, 将EMPLOYEE表中的SEX字段为M的AGE字段递增1'
sql_4 = """UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = 'm'"""

'删除操作'
sql_5 = """DELETE FROM EMPLOYEE WHERE AGE > 20"""

'分别执行语句sql_1, sql_2, sql_3'
cursor.execute(sql_1)
cursor.execute(sql_2_1)
cursor.execute(sql_4)
cursor.execute(sql_2)
cursor.execute(sql_5)
cursor.execute(sql_3)

'''
python查询Mysql使用fetchone()方法获取单条数据, 使用fetchall()获取多条数据
fetchone():该方法获取下一个查询结果集, 结果集是一个对象
fetchall():接收全部的返回结果行
rowcount():这是一个只读属性, 并返回执行execute()方法后影响的行数
'''

'接收全部的返回结果行'
results = cursor.fetchall()

#results_1 = cursor.fetchone()
#print '%s' % results_1

db.commit()
db.rollback()

'fetcall将查询到的每一条结果封装成一个元组返回'
for row in results:
    fname = row[0]
    lname = row[1]
    age = row[2]
    sex = row[3]
    income = row[4]
    print 'fname = %s, lname = %s, age = %d, sex = %s, income = %d' %(fname, lname, age, sex, income)

'关闭数据库链接'
db.close()
