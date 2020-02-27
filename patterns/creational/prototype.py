# -*- coding: utf-8 -*-
'''
@Date: 2020-02-24 00:20:48
@LastEditors: fzzjj2008
@LastEditTime: 2020-02-24 01:07:16
'''

import copy

class ICloneable:
    def shallow_clone(self):
        """
        浅拷贝
        """
        return copy.copy(self)
    
    def deep_clone(self):
        """
        深拷贝
        """
        return copy.deepcopy(self)

class Experience(ICloneable):
    company = ""
    years = 0
    def __init__(self, company, years):
        self.company = company
        self.years = years

class Person(ICloneable):
    name = ""
    exp = Experience("", 0)
    def __init__(self, name, exp):
        self.name = name
        self.exp = exp

    def set(self, name, exp):
        self.name = name
        self.exp.company = exp.company
        self.exp.years = exp.years

    def __str__(self):
        return ("(%s, %s, %d)" % (self.name, self.exp.company, self.exp.years))