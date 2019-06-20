# -*- coding: utf-8 -*-

# @Time : 2019-06-20 15:43
# @Author : Li Fu


# field 对象相关
class Field(object):

    def __init__(self, name, column_type, primary_key, default):
        self.name = name
        self.column_type = column_type
        self.primary_key = primary_key
        self.default = default

    def __str__(self):
        return '<%s, %s:%s>' % (self.__class__.__name__, self.column_type, self.name)


class StringField(Field):

    def __init__(self, name=None, primary_key=False, default=None, ddl='varchar(100)'):
        super().__init__(name, ddl, primary_key, default)


class IntegerField(Field):

    def __init__(self, name=None, primary_key=False, default=None, ddl='int'):
        super().__init__(name, ddl, primary_key, default)


class BooleanField(Field):

    def __init__(self, name=None, primary_key=False, default=None, ddl='bool'):
        super().__init__(name, ddl, primary_key, default)


class FloatField(Field):

    def __init__(self, name=None, primary_key=False, default=None, ddl='float'):
        super().__init__(name, ddl, primary_key, default)


class TextField(Field):

    def __init__(self, name=None, primary_key=False, default=None, ddl='text'):
        super().__init__(name, ddl, primary_key, default)
