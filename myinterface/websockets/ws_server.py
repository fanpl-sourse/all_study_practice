# -*- coding: utf-8 -*-
# @Time    : 2020/11/21 16:49
# @Author  : 饭盆里
# @File    : ws_server.py
# @Software: PyCharm
# @desc    :
import asyncio
import websockets

async  def hello(websocket,path):
    name = await websocket.recv()
    print(f'<<{name}')

    greeting = f"hello {name}"
    print(f'>>{greeting}')

start_server = websockets.serve(hello,'127.0.0.1',8212)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()



