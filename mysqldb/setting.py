# -*- coding: utf-8 -*-
# Created on 2018年1月20日
# @author: LuMingJie
# 数据库配置，支持MYSQL
from API_data import Port_date
ty_pe = Port_date.P_data()




DATABASE = {
    "ENGINE": ty_pe.detal("stu.xls","mysqldb",0,0),
    "host": ty_pe.detal("stu.xls","mysqldb",0,0),
    "port": 3306,
    "user": "root",
    "password": "1q2w3e4r",
    "db": "5i5j_broker"
}

REDIS = {
    "HOST": "localhost",
    "PORT": 6379,
    "DB": "0"
}


print(DATABASE)


import os
path1=os.path.abspath('.')   # 表示当前所处的文件夹的绝对路径
print(path1)
path2=os.path.abspath('..')  # 表示当前所处的文件夹上一级文件夹的绝对路径
print(path2)

prd = '../API_data/' + "stu.xls"

print(prd)

