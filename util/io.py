#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

import csv

'''
description: io 完成数据文件读写
'''


def read_csv_file(path: str) -> list[list[str]]:
    """ 读取固定路径下 csv 文件转换文本格式 """
    arr = []
    with open(path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            arr.append(row)
    return arr


def write_csv_file(path: str, data: list[list[str]]):
    """ csv 文件内容写入 """
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print('文件写入完成')
