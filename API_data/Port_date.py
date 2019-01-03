#-*- coding:UTF-8 -*-
#import sys
#reload(sys)
#sys.setdefaultencoding("utf8")
# __author__ = 'wudawei'

import xlwt
import xlrd
A = xlrd
B = xlwt

# book = xlrd.open_workbook('stu.xls') #打开一个excel
# sheet = book.sheet_by_index(0) #根据顺序获取sheet
# sheet2 = book.sheet_by_name('sheet1') #根据sheet页名字获取sheet
# print(sheet.cell(0,2).value) #指定行和列获取数据
# print("行数：%s"% sheet.ncols) #获取excel里面有多少列
# print("列数：%s"% sheet.nrows) #获取excel里面有多少行
# print(sheet.row_values(2))#取第几行的数据
# print(sheet.col_values(2)) #取第几列的数据
# for i in range(sheet.nrows): # 0 1 2 3 4 5
#     print(sheet.row_values(i)) #取第几行的数据


class P_data(object):
    '''

    '''

    def deta1(self,devdata,devdata1,devdata2):
        '''

        :param :
        :param :
        :param :
        :return:
        '''
        filename = '../API_data/' + devdata
        book = xlrd.open_workbook(filename)#打开一个excel
        sheet = book.sheet_by_index(0)
        result = sheet.cell(devdata1,devdata2).value
        return result

    def detal(self,devdata,devdata2,devdata1,devdata3):
        '''

        :param :
        :param :
        :param :
        :param :
        :return:
        '''
        filename = '../API_data/' + devdata
        book = xlrd.open_workbook(filename)  # 打开一个excel
        sheet = book.sheet_by_index(0)
        sheet2 = book.sheet_by_name(devdata2)
        result = sheet2.cell(devdata1, devdata3).value
        return result
