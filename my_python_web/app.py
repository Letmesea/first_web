#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Letmesea
# @Time : 2018/8/11 11:21
# @Email :  : LIANGZHONGHAI3@ceair.com
# @File : app.py
# @TODO :

from tornado import web,ioloop,httpserver

class MainPageHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("index.html")

application = web.Application([(r"/",MainPageHandler)])


def main():
    http_server = httpserver.HTTPServer(application)
    http_server.listen(8080)
    ioloop.IOLoop.current().start()
if __name__ == "__main__":
    main()