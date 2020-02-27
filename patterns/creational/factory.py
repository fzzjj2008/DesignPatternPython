# -*- coding: utf-8 -*-
'''
@Date: 2020-02-27 06:06:24
@LastEditors: fzzjj2008
@LastEditTime: 2020-02-27 06:25:54
'''
class Product:
    def show(self):
        pass

class Car(Product):
    def show(self):
        return "show car"
    
class Bus(Product):
    def show(self):
        return "show bus"

class Factory:
    def createProduct(self):
        pass

class CarFactory(Factory):
    def createProduct(self):
        return Car()

class BusFactory(Factory):
    def createProduct(self):
        return Bus()
