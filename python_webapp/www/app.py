#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Letmesea
# @Time : 2018/8/11 10:47
# @Email :  : LIANGZHONGHAI3@ceair.com
# @File : app.py
# @TODO :

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time

from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>',content_type='text/html') #为什么加上content_type就可以了

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 5000)
    logging.info('server started at http://127.0.0.1:5000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

