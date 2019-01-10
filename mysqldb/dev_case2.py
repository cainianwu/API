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
sql = "SELECT * FROM test_api cs WHERE cs.id = 1"
#sql = "SELECT %s FROM broker_info bk WHERE bk.brokerid =  95742" % "bk.bname"
# 使用 execute()  方法执行 SQL 查询
cursor.execute(sql)

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
data1 = str(data)
aa=data[1]
cc = data[2]
bb = aa + cc
print(bb)
print(type(data1))
#print("Database version : %s " % data)

# 关闭数据库连接
db.close()




tr = "asdasdaa\?asd\?asd\?asd"
cc = tr.split("\?")
print(tr)
print(cc)




import string
alphas = string.ascii_letters + '_'
nums = string.digits

print('欢迎使用标识符检查器v1.0')
print('受试者必须至少长2个字符。')
inp = input('要测试的标识符？ ')
print(len(inp))
print(inp[0])
print(inp[1:])
myint = len(inp)
alphase = alphas + nums
if myint > 1:
    if inp[0] not in alphas:
        print('''无效：第一个符号必须为字母或者下划线''')
    else:
        for otherChar in inp[1:]:
            if otherChar not in alphase:
                print('''无效：剩余符号必须是字母数字下划线''')
                break
        else:
            print("可以作为标识符")




cc ="sadadasd123"

print("cc.upprer:",cc.upper())






'''

#coding=utf-8
#Python3.x
import urllib.request
import urllib.parse
import json
def traslate(words):
    #目标URL
    targetURL = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
    #用户自定义表单，words表示的是用户要翻译的内容。这里使用的是dict类型，也可以使用元组列表（已经试过的）。
    data = {}
    data['type'] = 'AUTO'
    data['i'] = words
    data['doctype'] = 'json'
    data['xmlVersion'] = '1.8'
    data['keyfrom'] = 'fanyi.web'
    data['ue'] = 'UTF-8'
    data['action'] = 'FY_BY_CLICKBUTTON'
    data['typoResult'] = 'true'
    #将自定义data转换成标准格式
    data = urllib.parse.urlencode(data).encode('utf-8')
    #发送用户请求
    html = urllib.request.urlopen(targetURL, data)
    #读取并解码内容
    rst = html.read().decode("utf-8")
    rst_dict = json.loads(rst)
    return rst_dict['translateResult'][0][0]['tgt']
if __name__ == "__main__":
    print("输入字母q表示退出")
    while True:
        words = input("请输入要查询的单词或句子:\n")
        if words == 'q':
            break
        result = traslate(words)
        print("翻译结果是：%s"%result)

'''
import urllib.request
import urllib.parse
import json
#目标URL
targetURL = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
#用户自定义表单，words表示的是用户要翻译的内容。这里使用的是dict类型，也可以使用元组列表（已经试过的）。
data = {}
data['type'] = 'AUTO'
data['i'] = "words"
data['doctype'] = 'json'
data['xmlVersion'] = '1.8'
data['keyfrom'] = 'fanyi.web'
data['ue'] = 'UTF-8'
data['action'] = 'FY_BY_CLICKBUTTON'
data['typoResult'] = 'true'
#将自定义data转换成标准格式
data = urllib.parse.urlencode(data).encode('utf-8')
#发送用户请求
html = urllib.request.urlopen(targetURL, data)
#读取并解码内容
rst = html.read().decode("utf-8")
rst_dict = json.loads(rst)
print(rst_dict)