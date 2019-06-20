# -*- coding: utf-8 -*-

# @Time : 2019-06-19 10:33
# @Author : Li Fu

import logging

import asyncio

from aiohttp import web

logging.basicConfig(level=logging.INFO)


def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', content_type="text/html")


def init_routes_map(web_app):
    web_app.router.add_route('GET', '/', index)


async def start_srv(web_app):
    runner = web.AppRunner(web_app)
    await runner.setup()
    site = web.TCPSite(runner, '127.0.0.1', 9000)
    await site.start()
    logging.info('server started at http://127.0.0.1:9000')


if __name__ == '__main__':
    app = web.Application()
    init_routes_map(app)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_srv(app))
    loop.run_forever()
