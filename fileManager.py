#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/9 16:27
# @Author  : Wayne
# @Site    : 
# @File    : fileManager.py
# @Software: PyCharm
import glob
import os
import shutil
import searchUtils as searchTools
import logger
import mainUI
import threading
class FileManager:
    def __init__(self):
        self.counter = 0
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

    def move_file_by_index(self,search_str, workdir):
        image_counter = 0
        file_info_array = searchTools.get_filename_array(search_str)
        file_array = file_info_array[0]
        self.counter = file_info_array[1]
        if len(file_array) > 0:
            os.chdir(workdir)
            if not os.path.exists(search_str):
                os.mkdir(search_str)
            current_path = os.getcwd()
            dist_path = current_path + '\\' + search_str
            logger.info(dist_path)
            month_list = FileManager.traversalDir_FirstDir(current_path)
            for month in month_list:
                os.chdir(month)
                fileNameList = FileManager.traversalDir_FirstDir(os.getcwd())
                for item in file_array:
                    sql_path = os.getcwd() + "\\" + item
                    if sql_path in fileNameList:
                        try:
                            image_counter = image_counter + 1
                            threading.Thread(target=shutil.copytree(sql_path, dist_path + '\\' + item), name='LoopThread')
                            self.counter = self.counter - 1
                            logger.info("copy to"+dist_path)
                        except FileExistsError:
                            logger.info("file already exist")
                            break
        logger.info('Get '+str(image_counter)+' file(s)')
        logger.info('done!')
