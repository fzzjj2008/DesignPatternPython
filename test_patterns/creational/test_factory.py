# -*- coding: utf-8 -*-
'''
@Date: 2020-02-27 06:22:53
@LastEditors: fzzjj2008
@LastEditTime: 2020-02-27 06:25:22
'''

import sys, os
sys.path.append(os.getcwd())
import pytest
from patterns.creational.factory import CarFactory, BusFactory

class TestFactory:

    def test_car(self):        
        car = CarFactory().createProduct()
        assert car.show() == "show car"

    def test_bus(self):        
        bus = BusFactory().createProduct()
        assert bus.show() == "show bus"