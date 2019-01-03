#-*- coding:UTF-8 -*-
#import sys
#reload(sys)
#sys.setdefaultencoding("utf8")
# __author__ = 'wudawei'

from mysqldb import setting
import urllib3
import pymysql



adb = setting.DATABASE
# 打开数据库连接
db  = pymysql.connect(host= adb.get("host"),
                    port=adb.get("port"),
                    user=adb.get("user"),
                    password=adb.get("password"),
                    db=adb.get("db"),
                    charset=adb.get("charset")
                    )

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
sql = "SELECT %s FROM broker_info bk WHERE bk.brokerid =  95742" % "bk.bname"
# 使用 execute()  方法执行 SQL 查询
cursor.execute(sql)

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
data1 = cursor.fetchall()
print(data[0])
print(type(data))
#print("Database version : %s " % data)

# 关闭数据库连接
db.close()




tr = "asdasdaa\?asd\?asd\?asd"
cc = tr.split("\?")[0]
print(cc)