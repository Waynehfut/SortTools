#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/9 2121asd:06
# @Author  : Wayne
# @Site    : 
# @File    : searchUtils.py
# @Software: PyCharm
import re

import dbConnect
import logger
def parse_str(str_sql):
    '''
    替换所有括号的内容为“%”
    :param str_sql: 传入的语句
    :return:处理完的字符串
    '''
    pattern = '\(.*?\)|\（.*?\）'
    out = re.sub(pattern, '%', str_sql)
    return out


def search_handler(search_str):
    '''
    处理搜索语句
    :param search_str:
    :return: 搜索后的序列
    '''
    search_str = parse_str(search_str)
    dbHandler = dbConnect.DBConnect()
    search_array = dbHandler.select_sql(search_str)
    return search_array

def get_filename_array(search_array):
    array = []
    record_counter = 0
    for item in search_handler(search_array):
        print(item[6])
        record_counter = record_counter + 1
        array.append(item[6])
    logger.info("Get " + str(record_counter) + " record(s)")
    return array,record_counter

