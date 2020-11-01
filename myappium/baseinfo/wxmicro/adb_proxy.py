# -*- coding: utf-8 -*-
# @Time    : 2020/11/1 11:24
# @Author  : 饭盆里
# @File    : adb_proxy.py
# @Software: PyCharm
# @desc    :

from mitmproxy.utils import strutils
from mitmproxy import ctx
from mitmproxy import tcp


def tcp_message(flow: tcp.TCPFlow):
    message = flow.messages[-1]
    old_content = message.content
    #message.content = old_content.replace(b"foo", b"bar")
    message.content = old_content.replace(b"@webview_devtools_remote_", b"@.*.*.*._devtools_remote_")

    ctx.log.info(
        "[tcp_message{}] from {} to {}:\n{}".format(
            " (modified)" if message.content != old_content else "",
            "client" if message.from_client else "server",
            "server" if message.from_client else "client",
            strutils.bytes_to_escaped_str(message.content))
    )
