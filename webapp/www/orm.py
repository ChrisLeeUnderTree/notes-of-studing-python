# -*- coding: utf-8 -*-

# @Time : 2019-06-20 10:12
# @Author : Li Fu

from model import Model, StringField, IntegerField


class User(Model):
    __table__ = 'users'

    id = IntegerField(primary_key=True)
    name = StringField()
