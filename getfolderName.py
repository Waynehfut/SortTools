#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/9 21:44
# @Author  : Wayne
# @Site    : 
# @File    : getfolderName.py
# @Software: PyCharm

import glob
import os
from  PyQt4 import *
def traversalDir_FirstDir(path):
    list = []
    if (os.path.exists(path)):
        # 获取该目录下的所有文件或文件夹目录路径
        files = glob.glob(path + r'/*')
        for file in files:
            # 判断该路径下是否是文件夹
            if (os.path.isdir(file)):
                list.append(file.split(r'/', -1)[-1])
        return list

list = traversalDir_FirstDir(os.getcwd())
finalName = []
result = []
for month in list:
    fileNameListList = []
    os.chdir(month)
    fileNameList = traversalDir_FirstDir(os.getcwd())
    for item in fileNameList:
        strsss = item.split("\\")[-1]
        fileNameListList.append(strsss)
    file = open('list.txt', 'w')
    file.write(str(fileNameListList))
    file.close()
os.chdir('..')
