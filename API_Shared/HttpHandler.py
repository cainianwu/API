#-*- coding:UTF-8 -*-
#import sys
#reload(sys)
#sys.setdefaultencoding("utf8")
# __author__ = 'wudawei'


import json
from urllib import parse

from requests import Session

from API_Shared.LogHandler import LogHandler
from API_Shared.Recursion import GetDictParam

logger = LogHandler(__name__)
SESSION = Session()


class HttpHandler(GetDictParam):
    """
            公用的请求类接口
    @param : 需要请求的接口地址
    @param : kwargs
        @member methods -> http methods
        @member data -> post data
        @member json -> post json
        @member headers -> headers
        @member cookies -> cookies
    @return: Response<status_code>
    """
    def __init__(self, request_bodys: dict):
        self.session = SESSION
        self.body = request_bodys

    def make_request_template(self) -> dict:
        """
            make request body headers cookies and methods
        :return:
        """
        logger.info(self.body)
        logger.info("接受到 Func: {}, 参数为: {}".format(
            self.body.get('methods_name'), json.dumps(self.body, indent=4, ensure_ascii=False))
        )
        method = self.body.get('method')
        if method in ['get', 'GET']:
            tmp = ("url", "params", "headers", "cookies")
            body = self.list_for_key_to_dict(*tmp, my_dict=self.body)
            if body.get('params'):
                if "&" in body.get('params') and "=" in body.get('params'):
                    body["params"] = dict(parse.parse_qsl(body["params"]))
            logger.info("GET *TMP: {}".format(self.list_for_key_to_dict(*tmp, my_dict=self.body)))
            return self.get(**body)
        """
        put['put','PUT  ']
        patch['patch','PATCH']
        delete['delete','DELETE']
        head['head','HEAD']
        options['options','OPTIONS']
        """
        if method in ['post', 'POST']:
            tmp = ("url", "data", "json", "headers", "cookies")
            body = self.list_for_key_to_dict(*tmp, my_dict=self.body)
            body = {key: value for key, value in body.items() if value is not None}
            return self.post(**body)
        else:
            raise AttributeError("错误的请求方法, 请检查配置文件中的请求方法, 目前只支持['GET', 'POST']")

    def post(self, **kwargs: dict) -> dict:
        return self.session.post(**kwargs).json()

    def get(self, **kwargs: dict) -> dict:
        return self.session.get(**kwargs).json()
