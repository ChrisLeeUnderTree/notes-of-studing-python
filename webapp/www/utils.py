# -*- coding: utf-8 -*-

# @Time : 2019-06-20 14:28
# @Author : Li Fu

import hashlib

import logging

import time

from conf.app_config import LocalConfig

from model import User

_COOKIE_KEY = LocalConfig.session

logging.basicConfig(level=logging.INFO)


def user2cookie(user, max_age):
    """ Generate cookie str by user. """
    # build cookie string by: id-expires-sha1
    expires = str(int(time.time() + max_age))
    s = '%s-%s-%s-%s' % (user.id, user.passwd, expires, _COOKIE_KEY)
    l = [user.id, expires, hashlib.sha1(s.encode('utf-8')).hexdigest()]
    return '-'.join(l)


async def cookie2user(cookie_str):
    """ Parse cookie and load user if cookie is valid. """
    if not cookie_str:
        return
    try:
        L = cookie_str.split('-')
        if len(L) != 3:
            return
        uid, expires, sha1 = L
        if int(expires) < time.time():
            return
        user = await User.find(uid)
        if user is None:
            return
        s = '%s-%s-%s-%s' % (uid, user.passwd, expires, _COOKIE_KEY)
        if sha1 != hashlib.sha1(s.encode('utf-8')).hexdigest():
            logging.info('invalid sha1')
            return
        user.passwd = '******'
        return user
    except Exception as e:
        logging.exception(e)
        return None
