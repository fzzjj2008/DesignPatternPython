# -*- coding: utf-8 -*-
'''
@Date: 2020-02-27 06:28:32
@LastEditors: fzzjj2008
@LastEditTime: 2020-02-27 06:59:55
'''

# 设备簇
class Device:
    def show(self):
        pass

class TV(Device):
    def show(self):
        return "tv"

class PC(Device):
    def show(self):
        return "pc"

# 产家簇
class Producer:
    def get_producer(self):
        pass

class Haier(Producer):
    def get_producer(self):
        return "haier"

class Huawei(Producer):
    def get_producer(self):
        return "huawei"

# 抽象工厂类
class AbstractFactory:
    def create_device(self):
        pass
    def create_producer(self):
        pass

# Haier产家，生产TV
class HaierFactory(AbstractFactory):
    def create_device(self):
        return TV()
    def create_producer(self):
        return Haier()

# Huawei产家，生产pc
class HuaweiFactory(AbstractFactory):
    def create_device(self):
        return PC()
    def create_producer(self):
        return Huawei()