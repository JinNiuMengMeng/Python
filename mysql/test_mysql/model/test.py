#!/usr/bin/env python
#coding:utf-8

from unitily.sql_helper import MysqlHelper

class Test(object):
    def __init__(self):
        self.__helper = MysqlHelper()

    def get_one(self, id):
        sql = "select * from test1 where id = %s"
        params = (id,)
        return self.__helper.Get_one(sql, params)

    def checkValidate(self, username, password):
    	sql = "select * from test1 where name = %s and password = %s"
    	params = (username, password,)
    	return self.__helper.Get_one(sql, params)