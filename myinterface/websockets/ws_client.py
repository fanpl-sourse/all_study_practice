# -*- coding: utf-8 -*-
# @Time    : 2020/11/21 16:49
# @Author  : 饭盆里
# @File    : ws_client.py
# @Software: PyCharm
# @desc    :
import asyncio
import websockets

async def hello():
    uri = 'ws://127.0.0.1:8211'
    async with websockets.connect(uri) as websocket:
        name = input("you are ?  ")
        await websocket.send(name)
        print(f">>{name}")

        greeting = await websocket.recv()
        print(f"<<{greeting}")

asyncio.get_event_loop().run_until_complete(hello())

