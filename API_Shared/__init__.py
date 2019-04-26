# arr = [88,0,1,2,8,3,4,5,11,10,15,54,64]
# print(arr)
#
# def mappao(arr):
#     coun = len(arr)
#     for i in range(0,coun):
#         for j in range(i+1,coun):
#             if arr[i] > arr[j]:
#                 arr[i],arr[j] = arr[j],arr[i]
#    #     print(arr)
#     return arr
# print(mappao(arr))

# #
# CASE_PATH = "../API_case"
# import os
# print(os.path.abspath(CASE_PATH))
# print(os.path.normpath(CASE_PATH))
# print(os.listdir(CASE_PATH))
#
#




# class TestCaseLoader(GetDictParam, CasesManager):
#     """ TestCase Loader"""
#     __slots__ = "tags"
#
#     # if DEBUG_INFO is 1:
#     #     logger = LogHandler(__name__)
#     # else:
#     #     logger = LogHandler(__name__, level=30)
#
#     def __init__(self):
#         """ init class"""
#         super(TestCaseLoader, self).__init__()
#         self.files = os.listdir(os.path.abspath(CASE_PATH))
#         self.data = {}
#         self.tags = self.make_cases_info()
#         print("1:",self.tags)
