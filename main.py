  
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 13:44:10 2020
@author: Bruna
"""
import db
import functions as func


def main():
    db.connect()
    func.addCustomer()
    func.displayTitle()
    
    while True:
        command = input("Enter the command:\t")
        
        if command.lower() == "view":
            func.displayItems()
            func.displayMenu()
        elif command.lower() == "buy":
            func.displayItems()
            func.buyItem()
            func.displayMenu()
        elif command.lower() == "cart":
            func.displayCart()
            func.displayMenu()
        elif command.lower() == "pay":
            func.displayReceipt()
            break
        elif command.lower() == "exit":
            if func.cart == 0:
                print("\nCome back soon!")
                break
            elif func.cart > 0:
                print("\nYou have to pay for the things in your cart.")
                func.displayMenu()
        else:
            print("\nNot a valid command. Please try again.\n")
    db.close()
    
    
if __name__ == "__main__":
    main()