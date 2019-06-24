# -*- coding: utf-8 -*-

# @Time : 2019-06-21 16:47
# @Author : Li Fu

from model import User

from req import get


@get('/')
async def index(request):
    users = await User.find_all()
    return {
        '__template__': 'test.html',
        'users': users
    }
