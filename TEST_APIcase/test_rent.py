#-*- coding:UTF-8 -*-
#import sys
#reload(sys)
#sys.setdefaultencoding("utf8")
# __author__ = 'wudawei'


import unittest
import requests
from API_data.Port_date import P_data
from API_Shared.Rrqusetes_way import Data_requests
from API_Shared.HTMLreport import BeautifulReport
from TEST_APIcase.test_house import test_shou
A = P_data()
B = Data_requests()
C = test_shou()

class test_dome(unittest.TestCase):
    '''
    我的天
    '''
    def test_test3(self):
        '''

        :return:
        '''
        dev_a = C.test_editor()
        dev_b = C.test_release()
        B.Boolean_assertion("NotEqual",dev_a,dev_b)
  #      print ("测试通过",test_a,test_b)





if __name__ == '__main__':
    #确定生成报告的路径
    testuin = unittest.TestSuite()
    testuin.addTest(test_dome("test_test3"))
    test_case = BeautifulReport(testuin)
    test_case.report(filename="ccc.html")

