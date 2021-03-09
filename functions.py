# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 15:11:36 2020
@author: Bruna
"""

import db
from classes import Customer
import random

cart = 0
order = []
newTotal = 0
discountAmount = 0
name = ""

def displayTitle():
    print("\n===== WELCOME TO THE ONLINE STORE =====")
    print()
    displayMenu()

def displayMenu():
    print("\n===== COMMAND MENU =====")
    print("view - View Items")
    print("buy - Buy Items")
    print("cart - View My Cart")
    print("pay - Pay and Exit")
    print("exit - Exit")
    
def displayItems():
    print("\n===== Items avalibale in the store =====")
    print()
    items = db.getItems()
    
    for item in items:
        print(str(item.itemID + 1) + ". " + item.name + "\n   $" + str(item.price))
        print()
    

def addCustomer():
    global name
    name = input("Please enter your name:\t")
    print()
    print("Hello, " + name)
    
    customerID = random.randrange(1000)
    customer = Customer(customerID = customerID, name = name)
    db.addCustomer(customer)

def buyItem():
    again = "y"
    
    print("If you buy more than one item, you will receive a 20% discount!!")
    while again.lower() == "y":
        userInput = int(input("Enter the number of the item you want to buy:\t"))
        
        choice = db.getItem(userInput - 1)
        
        order.append(choice)
        try:
            if order == None:
                print("There is no item with that ID. Try again.\n")
                buyItem()
            else:
                global cart
                cart += 1
                print(choice.name + " was added to the cart")
                print()
        except TypeError:
            print("There is no item with that ID. Try again.\n")
            buyItem()
        again = input("Do you want to keep buying? (y/n)\t")
        print()
        
            
def displayCart():
    print("\n===== YOUR CART =====")
    print("You have " + str(cart) + " items.")
    
    global newTotal
    global discountAmount
    total = 0
    
    if cart == 0:
            print("Your cart is empty")
            print()
    elif cart > 0:
        for item in order:
            print(str(item.itemID + 1) + ". " + item.name + "\n   $" + str(item.price))
            print()
            
        for item in order:
            total += item.price
        
        if cart == 1:
            print("Your total is $" + str(total))
            newTotal = total
            print()
        elif cart > 1:
            discountAmount = round(total * .2, 2)
            print("Your original total is $" + str(total))
            print("You have a discount of $" + str(discountAmount))
            print()


def displayReceipt():
    global name
    global newTotal
    global discountAmount
    finalTotal = 0
    
    if cart > 0:
        
        print("\n===== RECEIPT =====")
        print("Items bought")
        print()
        for item in order:
            print(str(item.itemID + 1) + ". " + item.name + "\n   $" + str(item.price))
            print()
    
        for item in order:
            finalTotal += item.price
        if cart == 1:
            discountAmount = 0.00
            print("You had a discount of $" + str(discountAmount))
            print("Amount Paid: \t$" + str(finalTotal))
            
        elif cart > 1:
            newTotal = round(finalTotal * .8, 2)

            discountAmount = round(finalTotal * .2, 2)
    
            print("You had a discount of $" + str(discountAmount))
            print("Amount Paid: \t$" + str(newTotal))
        print("\nThank you for buying with us, " + name + ". Come back soon!")
        