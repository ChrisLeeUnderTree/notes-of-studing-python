# -*- coding: utf-8 -*-

# @Time : 2019-06-21 15:13
# @Author : Li Fu


class APIError(Exception):
    """ the base APIError which contains error(required), data(optional) and message(optional). """
    def __init__(self, error, data='', message=''):
        super(APIError, self).__init__(message)
        self.error = error
        self.data = data
        self.message = message
