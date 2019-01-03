#-*- coding:UTF-8 -*-
#import sys
#reload(sys)
#sys.setdefaultencoding("utf8")
# __author__ = 'wudawei'
import unittest
import json
from API_Shared.Rrqusetes_way import Data_requests
from API_Shared.HTMLreport import BeautifulReport
from API_Shared.E_mail import E_emai
from  API_data.Port_date import P_data
A = Data_requests()
T = P_data()






''''
A = comprehensive()
asdasd = {"asd":"a345sd","aasd":"123"}
class ceshi(unittest.TestCase):

    def cc(self):
        A.type("get","https://www.baidu.com/",date=asdasd)

print(ceshi.cc())
'''
'''
asdasd = {"asd":"a345sd","aasd":"123"}
date = {"aa":1}
json = {"aa":1}
headers = {"aa":"1"}
cookie = {"aa":"1"}
data = T.deta1("stu.xls",0,0)
A=requests.get(url =data,params = asdasd)
print(A.url)
# A = requests.post("https://www.baidu.com/",data =date ,json=json ,headers =headers)
# print(A.url)



print(T.chengji(5,6))



try:
    year = int(input("请输入年份:"))
    if year % 4 == 0 and year % 100 != 0:
        print("%d是闰年." %year)
    elif year % 400 == 0:
        print("%d是闰年." %year)
    else:
        print("%d不是闰年." %year)

except:
        print("你必须输入一个数字。")







from math import pi
def square(length):
    area = length ** 2
    print("正方形的面积是 %0.2f" %area)

def cube(length):
    volume = length ** 3
    print("立方体的体积是 %0.2f" %volume)

def circle(radius):
    area = pi * radius ** 2
    print("圆的面积是 %0.2f" %area)

def sphere(radius):
    volume = 4 * pi * radius ** 2
    print("球的体积是 %0.2f" %volume)

if __name__ == "__main__":
    try:
        print("*****直接执行*****")
        num = float(input("进入num:"))
        square(num)
        cube(num)
        circle(num)
        sphere(num)
    except:
            print(" 输入一个完整的数字 !")

if __name__ == "test":
    try:
        print("*****模块称为*****")
        num = float(input("进入num:"))
        square(num)
        cube(num)
        circle(num)
        sphere(num)
    except:
        print(" 输入一个完整的数字 !")


#############################################
print("输入的表达式")
expression = input('>')

if len(expression.split('+')) == 2:
        try:
                splitExpression = expression.split('+')
                m = float(splitExpression[0])
                n = float(splitExpression[1])
                print("=",m + n)
        except:
                print("Input ValueError !")
elif len(expression.split('-')) == 2:
        try:
                splitExpression = expression.split('+')
                m = float(splitExpression[0])
                n = float(splitExpression[1])
                print("=",m - n)
        except:
                print("Input ValueError !")
elif len(expression.split('*')) == 2:
        try:
                splitExpression = expression.split('*')
                m = float(splitExpression[0])
                n = float(splitExpression[1])
                print("=",m * n)
        except:
                print("Input ValueError !")
elif len(expression.split('/')) == 2:
        try:
                splitExpression = expression.split('/')
                m = float(splitExpression[0])
                n = float(splitExpression[1])
                print("=",m / n)
        except:
                print("Input ValueError !")
elif len(expression.split('%')) == 2:
        try:
                splitExpression = expression.split('%')
                m = float(splitExpression[0])
                n = float(splitExpression[1])
                print("=",m % n)
        except:
                print("Input ValueError !")
elif len(expression.split('**')) == 2:
        try:
                splitExpression = expression.split('**')
                m = float(splitExpression[0])
                n = float(splitExpression[1])
                print("=",m ** n)
        except:
                print("Input ValueError !")
else:
        print("Input Error !")




##################################
def common_divisor(a, b):
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i ==0:
            m = i
    print("公约数是 %d" %m)
def common_mutiple(i, j):
    maxnum = max(i, j)
    while True:
        if maxnum % i == 0 and maxnum % j ==0:
            print("公倍数是 %d" %maxnum)
            break
        else:
            maxnum = maxnum + 1
if __name__ == '__main__':
    try:
        num1 = int(input("Enter num1:"))
        num2 = int(input("Enter num2:"))
        common_divisor(num1, num2)
        common_mutiple(num1, num2)
    except ValueError:
        print("输入无效的num!")

'''
class test_test(unittest.TestCase):
    def test_test1(self):
        '''
        123走不走.
        '''
        try:
            data = A.data_data("data", "stu.xls", 2, 5)
            url = A.data_url("stu.xls", 2, 0, "stu.xls", 2, 1, "stu.xls", 2, 2, "stu.xls", 2, 3)
            r = A.type("post", url, data=data)
            a = r.text
            json_test = json.loads(a)
            if r.status_code == 200:
                print(" 接口响应时间:{}S\n"
                      "状态码:{}\n"
                      "响应数据【json】:{}\n"
                      "获取的数据：{},\n"
                      "请求头:{},\n"
                      "token:{}".
                      format(r.elapsed.total_seconds(),
                             r.status_code,
                             r.text,
                             json_test["data"]["list"][0]["housesid"],
                             r.headers,
                             r.cookies))
            else:
                print("都失败了你还想要啥？")
        except:
            pass


if __name__ == '__main__':
    #确定生成报告的路径
    testuin = unittest.TestSuite()
    testuin.addTest(test_test("test_test1"))
#    testuin.addTest(s_house("release"))
  #  testuin = A.Boolean_assertion("NotEqual",ceshi1("cece"))
#    C.reporterll("eee.html",testuin,u"自动化测试报告",u"自动化测试报告")
    #利用封装好的生产报告
    rets = BeautifulReport(testuin)
    rets.report(filename="ccc.html")
    #发送邮件
    E_emai(filenmail="ccc.html")


