#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/9 2121asd:06
# @Author  : Wayne
# @Site    : 
# @File    : dbConnect.py
# @Software: PyCharm
import pymysql.cursors
import logger


class DBConnect:
    _instance = None

    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(DBConnect, cls).__new__(cls, *args, **kw)
        return cls._instance

    def setUpDB(self, host="localhost", port=3306, dbname="lab_db", schema="mri", schemaTable="detect"):
        self.conn = pymysql.connect(host=host, port=port, user='root', passwd='', db=dbname, charset='utf8')
        self.cur = self.conn.cursor()
        self.schema = schema
        self.schemaTable = schemaTable
        logger.info(
            "connect as " + str(host) + ":" + str(port) + " at " + str(dbname) + "." + str(schema) + "." + str(schemaTable))

    def disconnect(self):
        '''
        完全断开链接
        :return:
        '''
        self.cur.close()
        self.conn.commit()
        self.conn.close()

    def select_sql(self, search_str):
        select_str = "SELECT * FROM " + self.schema + " WHERE " + self.schema + "." + self.schemaTable + " LIKE"+" \"%" + search_str + "%\""
        select_array = []
        self.cur.execute(select_str)
        info = self.cur.fetchall()
        for index in info:
            select_array.append(index)
        return select_array