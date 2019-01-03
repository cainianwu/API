#-*- coding:UTF-8 -*-

from mysqldb import setting

cc = setting.DATABASE

aa = cc.get("HOST")


print(aa)