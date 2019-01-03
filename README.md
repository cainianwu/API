# API
自己玩的接口自动化
傻瓜式接口测试.
纯属娱乐
测试报告的生成利用mock哥的第三方封装.https://github.com/cainianwu/BeautifulReport
unittest.TESTcase中不可以初始化__init__是重写了父类的初始化方法，父类的def __init__(self, methodName='runTest'):是传了2个参数，你传2个值，修改方式：

    def __init__(self,methodName='runTest'):
        super(Tset_requests,self).__init__(methodName)
文章地址：https://bbs.csdn.net/topics/392377857?page=1

case命名全部得以test开头.