# -*- coding: utf-8 -*-
'''
@Date: 2020-02-24 00:21:07
@LastEditors: fzzjj2008
@LastEditTime: 2020-02-27 05:48:55
'''

import sys, os
sys.path.append(os.getcwd())
import pytest
from patterns.creational.prototype import Person, Experience

class TestPrototype:

    def test_shallow_clone(self):
        # p2浅拷贝，父对象的子对象("BB", 10)同一份
        # p1: ("tom", ("AA", 5)) -> ("tom", ("BB", 10))
        # p2: ("tom", ("AA", 5)) -> ("sam", ("BB", 10))
        p1 = Person("tom", Experience("AA", 5))
        p2 = p1.shallow_clone()
        p2.set("sam", Experience("BB", 10))
        # print(p1)
        # print(p2)
        assert (id(p1) != id(p2))
        assert (p1.name == "tom")
        assert (p1.exp.company == "BB")
        assert (p1.exp.years == 10)
        assert (p2.name == "sam")
        assert (p2.exp.company == "BB")
        assert (p2.exp.years == 10)

    def test_deep_clone(self):        
        # p2深拷贝，父对象的子对象("BB", 10)不同
        # p1: ("tom", ("AA", 5))
        # p2: ("tom", ("AA", 5)) -> ("sam", ("BB", 10))
        p1 = Person("tom", Experience("AA", 5))
        p2 = p1.deep_clone()
        p2.set("sam", Experience("BB", 10))
        # print(p1)
        # print(p2)
        assert (id(p1) != id(p2))
        assert (p1.name == "tom")
        assert (p1.exp.company == "AA")
        assert (p1.exp.years == 5)
        assert (p2.name == "sam")
        assert (p2.exp.company == "BB")
        assert (p2.exp.years == 10)