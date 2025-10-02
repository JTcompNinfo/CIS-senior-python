'''
Python had a module called random. 
'''
import random


for roll in range(10):
    print(random.randint(1,6), end = " ")
    
smaller = int(input("Enter a smaller number: "))
bigger = int(input("Enter a bigger number: "))
myNUmber = random.randint(smaller, bigger)
count = 0


while True:
    count+=1
    user = int(input("Enter a number: "))
    if user < myNUmber:
        print("Too Small")
    elif user > myNUmber:
        print("Too big")
    elif user == myNUmber:
        print("Congrants! you got it in", count, "tries.")
        break