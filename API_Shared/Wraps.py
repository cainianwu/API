"""
@Version: 1.0
@Project: doraemon_recode
@Author: Raymond
@Data: 2018/1/30 下午1:20
@File: Wraps.py
@License: MIT
"""
import builtins
import json
from functools import wraps

from API_Shared.CreateCases import CreateCase
from API_Shared.HttpHandler import HttpHandler
from API_Shared.LogHandler import LogHandler
from API_Shared.Recursion import GetDictParam

logger = LogHandler(__name__)


def test_case_runner(func):
    """ test case runner """
    @wraps(func)
    def wrap(*args: tuple):
        for item in iter(CreateCase()):
            for key, value in item.items():
                if value == func.__name__:
                    logger.info("{} ===> {}".format(item.get('body'), value))
                    client = HttpHandler(item.get('body'))
                    result = client.make_request_template()
                    logger.info("Result: {}".format(result))
                    return func(
                        *args,
                        response=result,
                        kwassert=item.get('body').get('assert')
                    )
    return wrap


def test_case_parse(func):
    """ test case reponse parse """
    @wraps(func)
    def wrap(*args: tuple, **kwargs: dict):
        """ parse wrap """
        response = kwargs.get('response')
        kwassert = kwargs.get('kwassert')
        tmp = tuple(kwassert.keys())
        result = GetDictParam.list_for_key_to_dict(*tmp, my_dict=response)
        for key, value in kwassert.items():
            if isinstance(value, list):
                tp, _value = value
                if tp == "type" and key == "ResponseType":
                    result[key] = [tp, repr(getattr(builtins, tp)(response)).split("'")[1]]
                elif tp == "type":
                    result[key] = [tp, repr(getattr(builtins, tp)(result.get(key))).split("'")[1]]
                else:
                    result[key] = [tp, getattr(builtins, tp)(result.get(key))]

        assert_resp_values = json.dumps(
            result,
            ensure_ascii=False,
            sort_keys=True,
        )
        kwassert_values = json.dumps(
            kwassert, ensure_ascii=False, sort_keys=True
        )
        exec_info = "self.assertEqual({}, {})".format(assert_resp_values, kwassert_values).replace("null", "None")
        return func(*args, response=response, exec_text=exec_info)
    return wrap
