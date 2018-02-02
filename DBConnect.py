#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/9 2121asd:06
# @Author  : Wayne
# @Site    : 
# @File    : DBConnect.py
# @Software: PyCharm
import pymysql.cursors

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='lab_db', charset='utf8')
cur = conn.cursor()


def disconnect():
    '''
    完全断开链接
    :return:
    '''
    cur.close()
    conn.commit()
    conn.close()


def select_sql(sql):
    select_array = []
    cur.execute(sql)
    info = cur.fetchall()
    for index in info:
        select_array.append(index)
    return select_array
