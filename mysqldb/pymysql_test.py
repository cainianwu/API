# -*- coding: utf-8 -*-
# Created on 2018年10月20日

import logging

import pymysql

from mysqldb import setting

# 连接数据库
# 执行Mysql
logger = logging.getLogger(__name__)
table_name = ''
config = setting.DATABASE
conn = pymysql.connect(
    host=config.get("HOST"),
    port=config.get("PORT"),
    user=config.get("USER"),
    passwd=config.get("PWD"),
    db=config.get("DATABASE"),
    charset='utf8')


def connect():
    con = conn.cursor(cursor=pymysql.cursors.DictCursor)
    return con

cur = connect()


def exec_mysql(sql):
    try:
        if cur:
            cur.execute(sql)
    except Exception as e:
        conn.rollback()  # 事务回滚
        print('事务处理失败', e)
    else:
        conn.commit()  # 事务提交
        print('事务成功处理', cur.rowcount, '条数据')


# 关闭连接
def db_close():
    conn.close()

# from database import mysql_driver
# mysql_driver.table_name = 'trade'
# field = '(name, account, saving)'
# field1 = 'name'
# # 插入
# # 要插入的字段
# field = '(name, account, saving)'
# # 要插入的数据
# data = ('张三', '13512345678', '10000')
# mysql_driver.insert_mysql(field, data)
# # 更新
# data1 = ('张三', data[0])
# mysql_driver.update_mysql(field1, field1, data1)
# 删除
# mysql_driver.delete_mysql(field1, str(data1[0]))
# 清空
# mysql_driver.truncate_mysql()
# 查询
# 查询的字段
# field = 'id, name, account'
# # 条件字段和值
# data2 = ('id', 1)
# a = mysql_driver.select_mysql(field, data2)
# print(a)


def show_tables():
    sql = "SHOW TABLES "
    cur.execute(sql)
    result = cur.fetchall()
    print('共查找出', cur.rowcount, '条数据')
    table_list = []
    for i in result:
        table_list.append(i['Tables_in_cetms'])
    conn.commit()
    return table_list


def show_index():
    sql = "SHOW INDEX FROM " + table_name
    cur.execute(sql)
    result = cur.fetchall()
    print('共查找出', cur.rowcount, '条数据')
    index = []
    if len(result) == 0:
        print("获取索引失败，或无索引")
    else:
        for i in range(len(result)):
            index.append(result[i]['Column_name'])
    conn.commit()
    return index


def drop_mysql():
    sql = "DROP TABLE IF EXISTS " + table_name
    exec_mysql(sql)
    print('成功删除数据库', table_name)
# 修改数据


def update_mysql(field, field1, data):
    sql = "UPDATE " + table_name + " SET " + field + " = '%s' WHERE " + field1 + " = '%s'"
    print(sql % data)
    exec_mysql(sql % data)
    print('成功修改', cur.rowcount, '条数据')

# 查询数据


def select_mysql(field, data=''):
    sql = "SELECT " + field + " FROM " + table_name + " WHERE %s;"
    if data == '':
        sql = "SELECT " + field + " FROM " + table_name + " limit 0,1000"
        cur.execute(sql)
    else:
        print((sql % data))
        cur.execute(sql % data)
    result = cur.fetchall()
    for row in result:
        print(row)
    print('共查找出', cur.rowcount, '条数据')
    conn.commit()
    return result
# 删除数据


def delete_mysql(field, data):
    sql = "DELETE FROM " + table_name + " WHERE " + field + "= '%s'"
    exec_mysql(sql % data)
    print('成功删除', cur.rowcount, '条数据')
# # 清空表


def truncate_mysql():
    sql = "truncate table " + table_name
    exec_mysql(sql)
    print('成功清空表',table_name)
# 插入数据


def insert_mysql(field, params):
    arg_list = "','".join(['%s'] * len(params))
    sql = "INSERT INTO " + table_name + ' ' + str(field) + " VALUES ('%s')" % arg_list
    print(sql)
    print(params)
    print(sql % params)
    exec_mysql(sql % params)
    print('成功插入', cur.rowcount, '条数据')

# 获取数据方法


def get_data():
    list1 = []
    rows = cur.fetchall()
    # 遍历数据（比上一个更直接一点）
    if rows is not None:
        for row in rows:
            list1.append(row)
    return list1


