# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 13:36:56 2020

@author: Bruna
"""
class Item:
    def __init__(self, itemID = 0, name = None, price = 0):
        self.itemID = itemID
        self.name = name
        self.price = price

class Customer:
    def __init__(self, customerID = 0, name = None):
        self.customerID = customerID
        self.name = name