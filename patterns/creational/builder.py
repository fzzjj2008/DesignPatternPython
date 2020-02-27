# -*- coding: utf-8 -*-
'''
@Date: 2020-02-27 06:58:24
@LastEditors: fzzjj2008
@LastEditTime: 2020-02-27 07:15:56
'''

class Product:

    partA = ""
    partB = ""
    
    def setPartA(self, partA):
        self.partA = partA

    def setPartB(self, partB):
        self.partB = partB
    
    def show(self):
        return (self.partA, self.partB)


class Builder:

    product = Product()
    
    def addPartA(self, partA):
        self.product.setPartA(partA)

    def addPartB(self, partB):
        self.product.setPartB(partB)
    
    def build(self):
        return self.product
