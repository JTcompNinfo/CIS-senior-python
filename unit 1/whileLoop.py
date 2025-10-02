'''
set the sum to 0.0
input a string
while the sting is not the emptyu string 
convert the string to a float
add the float to the sum
input a string
print the sum

zLoop control variable - the first input statment that initalizes a variable to a value that the loop condition can test
'''

theSum = 0.0
data = input("Enter a number or just enter to quit: ")
while data != "":
    number = float(data)
    theSum += number
    data = input("Enter a number or just enter to quit: ")
    
print("The sum is:", theSum)


