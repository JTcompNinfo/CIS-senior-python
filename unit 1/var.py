'''
File name: var.py
Author: Joel Dinovo
Date: 9/17/2025

Practicing variable basics
'''
#Variables can save all data types
myInt = 42
myFloat = 3.1415
myString = 'Joel Dinovo'
myBool = True

print("My name is: " + myString)

myAge = myInt

print("My age is: ", myAge)

print(myFloat)
myFloat = 6.28210
print(myFloat)

print("\n\n\n")
print("My Ticket App")
print("-------------")
ticketTotal = 43.50 + 43.50 +43.50
processFee = 2.95
venueFee = 3.95 + 3.95 + 3.95

print("\nMy Subtotal is:")
print("-----------------")
print("$", ticketTotal + processFee + venueFee)