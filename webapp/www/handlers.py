# -*- coding: utf-8 -*-

# @Time : 2019-06-21 16:47
# @Author : Li Fu

import time

from model import Blog, User

from req import get


@get('/')
async def index(request):
    summary = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, ' \
              'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    a = Blog(id='1', name='Test Blog', summary=summary, created_at=time.time() - 120)
    print(a)
    blogs = [
        Blog(id='1', name='Test Blog', summary=summary, created_at=time.time() - 120),
        Blog(id='2', name='Something New', summary=summary, created_at=time.time() - 3600),
        Blog(id='3', name='Learn Swift', summary=summary, created_at=time.time() - 7200)
    ]
    return {
        '__template__': 'blogs.html',
        'blogs': blogs
    }


@get('/api/users')
async def api_get_users():
    users = await User.find_all(order_by='created_at desc')
    for u in users:
        u.passwd = '******'
    return dict(users=users)
