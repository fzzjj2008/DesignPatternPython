# -*- coding: utf-8 -*-
'''
@Date: 2020-02-27 07:15:34
@LastEditors: fzzjj2008
@LastEditTime: 2020-02-27 07:16:57
'''

import sys, os
sys.path.append(os.getcwd())
import pytest
from patterns.creational.builder import Builder

class TestBuilder:

    def test_builder(self):        
        builder = Builder()
        builder.addPartA("aa")
        builder.addPartB("bb")
        product = builder.build()
        assert (product.show() == ("aa", "bb"))