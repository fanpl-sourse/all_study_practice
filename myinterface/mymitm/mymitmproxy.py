# -*- coding: utf-8 -*-
# @Time    : 2020/11/22 14:34
# @Author  : 饭盆里
# @File    : mymitmproxy.py
# @Software: PyCharm
# @desc    :

# from mitmproxy import http
#
#
# def request(flow: http.HTTPFlow) -> None:
#     if "baidu.com" in flow.request.pretty_url :
#         flow.response = http.HTTPResponse.make(
#             200,  # (optional) status code
#             b"Hello World",  # (optional) content
#             {"Content-Type": "text/html"}  # (optional) headers
#         )


from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:
    if "quote.json" in flow.request.pretty_url :
        with open('text.json',encoding='utf-8') as f:

            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                f.read(),  # (optional) content
                {"Content-Type": "application/json"}  # (optional) headers
            )