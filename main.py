#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado import ioloop
from tornado import web
from tornado import options
from etc.config import settings

import url

options.define("port", default=8080, help="run on this port", type=int)

def main():
    options.parse_command_line()
    application = web.Application(url.router, **settings)
    application.listen(options.options.port)
    ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    print('Server started at port %s' % options.options.port)
    main()
