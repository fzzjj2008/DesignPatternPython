# -*- coding: utf-8 -*-
'''
@Date: 2020-02-23 18:57:40
@LastEditors: fzzjj2008
@LastEditTime: 2020-02-24 00:17:47
'''
import sys, os
sys.path.append(os.getcwd())
import pytest
import threading
from patterns.creational.singleton import Singleton

class TestSingleton:

    def test_id(self):
        obj1 = Singleton()
        obj2 = Singleton()
        assert (id(obj1) == id(obj2))

    def test_thread(self):

        obj = []
        obj.append(id(Singleton()))

        def task():
            obj_id = id(Singleton())
            obj.append(obj_id)

        for _ in range(10):
            t = threading.Thread(target=task)
            t.start()
        
        print(obj)
        assert (obj[0] == obj[10])