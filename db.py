# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 13:49:48 2020
@author: Bruna
"""

import sys
import os
import sqlite3
from contextlib import closing

from classes import Item
from classes import Customer

conn = sqlite3.connect("project.sqlite")
conn.row_factory = sqlite3.Row

def connect():
    global conn
    if not conn:
        if sys.platform == "win32":
            DB_FILE = "\Desktop\GBC\WINTER 2020\PYTHON\PROJECT\project.sqlite"
        else:
            HOME = os.environ["HOME"]
            DB_FILE = HOME + "/Documents/murach/python/_db/movies.sqlite"
            conn = sqlite3.connect(DB_FILE)
            conn.row_factory = sqlite3.Row

def close():
    if conn:
        conn.close()
        
def makeItem(row):
    return Item(row[0], row[1], row[2])

# TO DISPLAY THE ITEMS AVAILABLE IN THE DATABASE
def getItems():
    query = '''SELECT itemID AS ID, 
                    name AS Item, 
                    price AS Price
                FROM Item'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()
        
    items = []
    for row in results:
        items.append(makeItem(row))
    return items

# TO GET ONE SPECIFC ITEM IN THE DATABASE
def getItem(itemID):
    query = '''SELECT itemID AS ID, name AS Item, price AS Price
                FROM Item WHERE itemID = ?'''

    with closing(conn.cursor()) as c:
        c.execute(query, (itemID,))
        row = c.fetchone()

    item = makeItem(row)
    return item

# ADD A NEW CUSTOMER IN THE DATABASE
def addCustomer(customer):
    sql = '''INSERT INTO Customer (customerID, name)
            VALUES (?, ?)'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (customer.customerID, customer.name))
        conn.commit()
