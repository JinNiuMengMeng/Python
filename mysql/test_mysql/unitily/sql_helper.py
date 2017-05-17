#!/usr/bin/env python
#coding:utf-8

import MySQLdb
import config

class MysqlHelper(object):
    def __init__(self):
        self.__connect_dict = config.con_dict
    def Get_Dict(self, sql, params):

        db = MySQLdb.connect(**self.__connect_dict)
        cursor = db.cursor(cursorclass = MySQLdb.cursors.DictCursor)

        recount = cursor.execute(sql, params)
        data = cursor.fetchall()

        cursor.close()
        db.close()
        return data
    def Get_one(self, sql, params):
        print self.__connect_dict
        db = MySQLdb.connect(**self.__connect_dict)
        cursor = db.cursor(cursorclass = MySQLdb.cursors.DictCursor)

        recount = cursor.execute(sql, params)
        data = cursor.fetchone()

        cursor.close()
        db.close()
        return data
if __name__ == "__main__":
    helper = MysqlHelper()
    sql = "select * from test1 where id > %s"
    params = (10,)
    print helper.Get_one(sql, params)
    for i in  helper.Get_Dict(sql, params):
        print i
