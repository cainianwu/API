#-*- coding:UTF-8 -*-
#import sys
#reload(sys)
#sys.setdefaultencoding("utf8")
# __author__ = 'wudawei'
import unittest
import sys
import time
import os
from API_Shared.HTMLreport import BeautifulReport
from API_Shared.E_mail import E_emai
test_drice = "../API_gather"


file = unittest.defaultTestLoader.discover(test_drice,pattern='test*.py',top_level_dir=None)

begin_time = time.strftime("%Y-%m-%d %H_%M_%S")



if __name__ == '__main__':
    #确定生成报告的路径
    testuin = unittest.TestSuite()
    testuin.addTest(file)
  #  testuin = A.Boolean_assertion("NotEqual",ceshi1("cece"))
#    C.reporterll("eee.html",testuin,u"自动化测试报告",u"自动化测试报告")
    #利用封装好的生产报告
    rets = BeautifulReport(testuin)
    rets.report(filename="{}.html".format(begin_time))
    #发送邮件
    E_emai(filenmail="{}.html".format(begin_time))
    


