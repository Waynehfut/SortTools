#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/9 2121asd:06
# @Author  : Wayne
# @Site    : 
# @File    : SearchTools1009.py
# @Software: PyCharm
import re

import DBConnect


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
    select_str = "SELECT * FROM mri WHERE mri.detect LIKE \"%" + search_str + "%\""
    search_array = DBConnect.select_sql(select_str)
    return search_array

def get_filename_array(search_array):
    array = []
    for item in search_handler(search_array):
        print(item[4])
        print(item[0])
        array.append(item[4]+'-'+item[0])
    return array
