# -*- coding: utf-8 -*-
'''
@Date: 2020-02-27 06:55:12
@LastEditors: fzzjj2008
@LastEditTime: 2020-02-27 06:58:03
'''

import sys, os
sys.path.append(os.getcwd())
import pytest
from patterns.creational.absfactory import HaierFactory, HuaweiFactory

class TestAbsFactory:

    def test_haier(self):
        device = HaierFactory().create_device()
        producer = HaierFactory().create_producer()
        assert device.show() == "tv"
        assert producer.get_producer() == "haier"

    def test_huawei(self):
        device = HuaweiFactory().create_device()
        producer = HuaweiFactory().create_producer()
        assert device.show() == "pc"
        assert producer.get_producer() == "huawei"
