# -*- coding: utf-8 -*-

# @Time : 2019-06-19 10:33
# @Author : Li Fu

import asyncio

import logging

import os

from aiohttp import web

from jinja2 import Environment, FileSystemLoader

from conf.app_config import LocalConfig

from connect import create_pool

from jinjia_conf import datetime_filter

from middleware import logger_factory, response_factory, auth_factory

from req import add_routes, add_static

logging.basicConfig(level=logging.INFO)


def init_jinja2(_, **kw):
    logging.info('init jinja2...')
    options = dict(
        autoescape=kw.get('autoescape', True),
        block_start_string=kw.get('block_start_string', '{%'),
        block_end_string=kw.get('block_end_string', '%}'),
        variable_start_string=kw.get('variable_start_string', '{{'),
        variable_end_string=kw.get('variable_end_string', '}}'),
        auto_reload=kw.get('auto_reload', True)
    )
    path = kw.get('path', None)
    if path is None:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    logging.info('set jinja2 template path: %s' % path)
    env = Environment(loader=FileSystemLoader(path), **options)
    filters = kw.get('filters', None)
    if filters is not None:
        for name, f in filters.items():
            env.filters[name] = f
    app['__templating__'] = env


async def start_srv(web_app):
    init_jinja2(web_app, filters=dict(datetime=datetime_filter))
    add_routes(web_app, 'handlers')
    add_static(web_app)
    runner = web.AppRunner(web_app)
    await runner.setup()
    site = web.TCPSite(runner, '127.0.0.1', 9000)
    await create_pool(user=LocalConfig.db_user, password=LocalConfig.db_password, db=LocalConfig.db_name)
    await site.start()
    logging.info('server started at http://127.0.0.1:9000')


if __name__ == '__main__':
    app = web.Application(middlewares=[
        logger_factory,
        response_factory,
        auth_factory,
    ])
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_srv(app))
    loop.run_forever()
