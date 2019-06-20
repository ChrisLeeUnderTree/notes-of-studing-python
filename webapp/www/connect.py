# -*- coding: utf-8 -*-

# @Time : 2019-06-20 10:12
# @Author : Li Fu

import logging

import aiomysql

logging.basicConfig(level=logging.INFO)


async def create_pool(**kw):
    logging.info('creating database connection pool...')
    global __pool
    __pool = await aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port', 3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get('charset', 'utf8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=kw.get('loop', None),
    )


async def select(sql, args, size=None):
    logging.info('sql: %s, args: %s' % (sql, args))
    global __pool
    with (await __pool) as conn:
        cur = await conn.cursor(aiomysql.DictCursor)
        await cur.execute(sql.replace('?', '%s'), args or ())
        if size:
            rs = await cur.fetchmany(size)
        else:
            rs = await cur.fetchall()
        await cur.close()
        logging.info('rows returned: %s' % len(rs))
        return rs


async def execute(sql, args):
    logging.info('sql: %s, args: %s' % (sql, args))
    with (await __pool) as conn:
        try:
            cur = await conn.cursor()
            await cur.execute(sql.replace('?', '%s'), args)
            affected = cur.rowcount
            await cur.close()
        except BaseException as e:
            raise e
        return affected
