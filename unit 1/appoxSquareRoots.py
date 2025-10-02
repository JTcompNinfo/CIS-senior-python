'''
write a program that computes square roots. You will use Python's math module. Python's math module has a function called sqrt - math.sqrt() - will only be used at the end to compare your calculation with Python's calculation.

Compute square root of a number:
1. The input is a number.
2. The output are the program's estiimate of the square root using Newton's method of seccessive apporoxmations, and python's own estimate using math.sqrt().
'''
import math

# Receive the input number from the user
x = float(input("Enter a postive numbe: "))


# Intialize the tolerance and estimate
tolerant = 0.000001
estimate = 1.0

# preform the succesive approximations

while True:
    estimate = (estimate + x / estimate) / 2
    diffrence = abs(x - estimate ** 2)
    if diffrence <= tolerant:
        break
    
print("The program's estimate is ", estimate)
print("python's is ", math.sqrt(x))