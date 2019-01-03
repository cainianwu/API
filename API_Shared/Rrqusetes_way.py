#-*- coding:UTF-8 -*-
#import sys
#reload(sys)
#sys.setdefaultencoding("utf8")
# __author__ = 'wudawei'

import requests
import json
from API_data.Port_date import P_data
import json
import time
import unittest

b = P_data()

class Data_requests(unittest.TestCase):

    def __init__(self,methodName='runTest'):

        super(Data_requests,self).__init__(methodName)

    def type(self, revtest1, revtest2, params=None, data=None, json=None, **kwargs ):
        global r,a
        r = requests
       # a = Tset_requests()
        if revtest1 == "get":
            return r.get(revtest2, params=params, **kwargs)

        elif revtest1 == "post":

            return  r.post(revtest2, data=data, json=json, **kwargs)
        elif revtest1 == "put":

            return r.put(revtest2, data=data, **kwargs)
        elif revtest1 == "delete":

            return r.delete(revtest2, **kwargs)
        elif revtest1 == "head":

            return r.head(revtest2, **kwargs)
        elif revtest1 == "options":

            return r.options(revtest2, **kwargs)

# 布尔断言
    def Boolean_assertion(self,devbool,devbool1,devbool2, msg=None):
        if devbool == "Equal":
            #验证adevbool1=devbool2，不等则fail
             return self.assertEqual(devbool1,devbool2,msg=msg)

        elif devbool == "NotEqual":
            # 验证adevbool1！=devbool2，不等则fail
            return self.assertNotEqual(devbool1,devbool2,msg=msg)

        elif devbool == "True":
            #验证devbool1是true，如果为false，则fail
            return  self.assertTrue(devbool1,msg=msg)

        elif devbool == "False":
            # 验证devbool1是false，如果为false，则fail
            return self.assertFalse(devbool1,msg=msg)

        elif devbool == "Is":
            #验证devbool1跟devbool2是同一个对象，不是则fail
            return self.assertIs(devbool1,devbool2,msg=msg)

        elif devbool == "IsNot":
            # 验证devbool1跟devbool2不是同一个对象，不是则fail
            return self.assertIsNot(devbool1,msg=msg)

        elif devbool == "IsNone":
            # 验证devbool1是None，不是则fail
            return self.assertIsNone(devbool1,msg=msg)

        elif devbool == "IsNotNone":
            # 验证devbool1不是None，不是则fail
            return self.assertIsNotNone(devbool1,msg=msg)

        elif devbool == "In":
            # 验证devbool1是devbool2的子串，不是则fail
            return self.assertIn(devbool1,devbool2,msg=msg)

        elif devbool == "NotI":
            #验证devbool1不是devbool2的子串，不是则fail
            return self.assertNotIn(devbool1,devbool2,msg=msg)

        elif devbool == "IsInstance":
            #验证devbool1是devbool2的实例，不是则fail
            return self.assertIsInstance(devbool1,devbool2,msg=msg)

        elif devbool == "NotIsInstance":
            # 验证devbool1不是devbool2的实例，不是则fail
            return self.assertNotIsInstance(devbool1,devbool2,msg=msg)


    # 比较断言
    def Compare_assert(self,devcompare,devcompare1,devcompare2,places=None, msg=None,delta=None):
        if devcompare == "AlmostEqual":
            #验证devcompare1约等于devcompare2，palces: 指定精确到小数点后多少位，默认为7
            return self.assertAlmostEqual(devcompare1, devcompare2, places=places, msg=msg, delta=delta)

        elif devcompare == "NotAlmostEqual":
            # 验证devcompare1不约等于devcompare2，palces: 指定精确到小数点后多少位，默认为7
            return self.assertNotAlmostEqual(devcompare1,devcompare2,places=places, msg=msg, delta=delta)

        elif devcompare == "Greater":
            # 验证devcompare1大于devcompare2，否则fail
            return self.assertGreater(devcompare1,devcompare2,msg=msg)

        elif devcompare == "GreaterEqual":
            # 验证devcompare1大于等于devcompare2，否则fail
            return self.assertGreaterEqual(devcompare1,devcompare2,msg=msg)

        elif devcompare == "Less":
            # 验证devcompare1小于devcompare2，否则fail
            return self.assertLess(devcompare1,devcompare2,msg=msg)

        elif devcompare == "LessEqual":
            # 验证devcompare1小于等于devcompare2，否则fail
            return self.assertLessEqual(devcompare1,devcompare2,msg=msg)

        elif devcompare == "RegexpMatches":
            #验证正则表达式devcompare2搜索匹配的文本devcompare1. regexp：通常使用re.search()
            return self.assertRegexpMatches(devcompare1,devcompare2,msg=msg)

        elif devcompare == "NotRegexpMatches":
            # 验证正则表达式devcompare2搜索不匹配的文本devcompare1. regexp：通常使用re.search()
            return self.assertNotRegexpMatches(devcompare1,devcompare2,msg=msg)


# 复杂断言
    def Complex_asser(self,devcomplex,devcomplex1,devcomplex2,msg=None):
        if devcomplex == "ListEqual":
            # 验证列表devcomplex1与devcomplex2相等，不等则fail，同时报错信息返回具体的不同的地方
            return self.assertListEqual(devcomplex1,devcomplex2,msg=msg)

        elif devcomplex == "TupleEqual":
            # 验证元组devcomplex1与devcomplex2相等，不等则fail，同时报错信息返回具体的不同的地方
            return  self.assertTupleEqual(devcomplex1,devcomplex2,msg=msg)

        elif devcomplex == "SetEqual":
            # 验证集合devcomplex1与devcomplex2相等，不等则fail，同时报错信息返回具体的不同的地方
            return  self.assertSetEqual(devcomplex1,devcomplex2,msg=msg)

        elif devcomplex == "DictEqual":
            # 验证字典devcomplex1与devcomplex2相等，不等则fail，同时报错信息返回具体的不同的地方
            return  self.assertDictEqual(devcomplex1,devcomplex2)



#切片取值封装
    def slice_Type(
            self,r_type,value,
               value1=None,
               value2=None,
               value3=None,
               value4=None,
               value5=None,
               value6=None
    ):
        if value1 == None and value2 == None and value3 == None \
                and value4 ==None and value5 == None and value6 == None:
            return r_type[value]

        elif value2 == None and value3 == None and value4 ==None and value5 == None and value6 == None:
            return r_type[value][value1]

        elif value3 == None and value4 ==None and value5 == None and value6 == None:
            return r_type[value][value1][value2]

        elif value4 == None and value5 == None and value6 == None:
            return r_type[value][value1][value2][value3]

        elif value5 == None and value6 == None:
            return r_type[value][value1][value2][value3][value4]

        elif value6 == None:
            return  r_type[value][value1][value2][value3][value4][value5][value6]



#接口参数请求获取表格数据封装.
    def data_data(self,data,The_data,value,value2):
        if data == "data":
            test_data = b.deta1(The_data,value,value2)
            return json.loads(test_data)

    def data_params(self,params,The_path,value,value2):
        if params == "params":
            tsst_params = b.deta1(The_path,value,value2)
            return json.loads(tsst_params)

    def data_json(sself,json,The_path,value,value2):
        if json == "json":
            test_json = b.deta1(The_path,value,value2)
            return json.loads(test_json)

    def data_kwargs(self,kwargs,The_path,value,value2):
        if kwargs == "kwargs":
            test_kwargs = b.deta1(The_path,value,value2)
            return json.loads(test_kwargs)


#url 地址拆分拼接封装
    def data_url(self,The_path1,value1,index1,
                 The_path2, value2, index2,
                 The_path3, value3, index3,
                 The_path4, value4, index4,
                 ):
        type = b.deta1(The_path1,value1,index1)
        type2 = b.deta1(The_path2, value2, index2)
        type3 = b.deta1(The_path3, value3, index3)
        type4 = b.deta1(The_path4, value4, index4)
        faname = type + type2 + type3 + type4
        return faname



    def Post_tset(self,key,value,valueL):
        if key == 200:
            print(value)
        else:
            print(value)


