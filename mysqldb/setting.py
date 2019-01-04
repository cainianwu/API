# -*- coding: utf-8 -*-
# Created on 2018年1月20日
# @author: LuMingJie
# 数据库配置，支持MYSQL



from API_data import Port_date
ty_pe = Port_date.P_data()




DATABASE = {
    "ENGINE": ty_pe.detal("stu.xls","mysqldb",1,0),
    "host": ty_pe.detal("stu.xls","mysqldb",1,1),
    "port": int(ty_pe.detal("stu.xls","mysqldb",1,2)),
    "user": ty_pe.detal("stu.xls","mysqldb",1,3),
    "password": ty_pe.detal("stu.xls","mysqldb",1,4),
    "db": ty_pe.detal("stu.xls","mysqldb",1,5),
    "charset":ty_pe.detal("stu.xls","mysqldb",1,6)
}


