# -*- coding: utf-8 -*-
'''
@Date: 2020-02-23 18:57:32
@LastEditors: fzzjj2008
@LastEditTime: 2020-02-24 00:18:11
'''

class SingletonBase(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton(metaclass=SingletonBase):
    def __init__(self):
        pass
