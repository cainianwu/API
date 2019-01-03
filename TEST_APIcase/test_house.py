#-*- coding:UTF-8 -*-
#import sys
#reload(sys)
#sys.setdefaultencoding("utf8")
# __author__ = 'wudawei'
import requests
import unittest
import json
from API_Shared.Rrqusetes_way import Data_requests
from API_Shared.HTMLreport import BeautifulReport
from API_Shared.E_mail import E_emai
from  API_data.Port_date import P_data
A = Data_requests()
T = P_data()
class test_shou(unittest.TestCase):

    def test_editor(self):
        '''
        买卖查询
        :return:
        '''
        data = A.data_data("data", "stu.xls", 2, 5)
        url = A.data_url("stu.xls", 2, 0, "stu.xls", 2, 1, "stu.xls", 2, 2, "stu.xls", 2, 3)
        r = A.type("post", url, data=data)
        a = r.text
        json_test = json.loads(a)
        #return test_url
        print(json_test)
        return json_test
    def test_release(self):
        '''
        租赁查询
        :return:
        '''
        data = A.data_data("data","stu.xls",4,5)
        url = A.data_url("stu.xls", 2, 0, "stu.xls", 4, 1, "stu.xls", 4, 2, "stu.xls", 4, 3)
        r = A.type("post",url,data=data)
        a = r.text
        test_json =json.loads(a)
        print(test_json)
'''

if __name__ == '__main__':
    #确定生成报告的路径
    testuin = unittest.TestSuite()
    testuin.addTest(test_shou("test_editor"))
    testuin.addTest(test_shou("test_release"))
    rete = BeautifulReport(testuin)
    rete.report(filename="aaa.html")
    E_emai(filenmail="aaa.html")


'''



'''
    filename ='../TESTreport/' + '4444.html'
    fp = open(filename,'wb')
    #生成报告的Title,描述C
    runner = HTMLTestRunnerCN.HTMLTestReportCN(
        stream=fp,
        title='自动化测试报告',
        description='详细测试用例结果',
  #      tester='Findyou'
        ).run(testuin)
    #运行测试用例
    # 关闭文件，否则会无法生成文件
    fp.close()
'''












'''
if __name__ =="__main_":
    caselist = ("The_editor","The_editor")
    RegSuite = unittest.TestSuite()
    for tmpCase in caselist:
        RegSuite.addTest(s_house(tmpCase))
    C.reporterll("CCC.html",RegSuite,U"测试报告",U"测试报告")
'''

