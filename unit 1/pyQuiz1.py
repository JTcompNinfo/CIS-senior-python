# Question 1: Basic for Loop with range()
for times in range(0, 6):
    print(times)
    
print("\n\n")

# Question 2: for Loop with Upper and Lower Bounds
for num in range(3, 9):
    print(num)
    
print("\n\n")

# Question 3: for Loop with a Step

for step in range(0, 11, 2):
    print(step)
    
print("\n\n")


# Question 4: for Loop Counting Down
for count in range (10, 0, -1):
    print(count)
    
    
print("\n\n")

# Question 5: Formatted Text Output

for cal in range(1, 6):
    sum = 5 * cal
    print("5 x " + str(cal) + " = " + str(sum))
    
# Question 6: Simple if-else Statement

print("\n\n")

age = int(input("What is your age? "))

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
    
print("\n\n")

# Question 7: for Loop with if-else Inside
for queston7 in range(1, 11):
    if queston7 % 2 == 0:
        print("Even")
    else:
        print("odd")
        
print("\n\n")

# Question 8: Countdown with Step and Formatting
for queston8  in range(20, -1, -5):
    print("Countdown: " + str(queston8))
    
print("\n\n")

# Question 9: for Loop with if-else and Formatted Output
for question9 in range(1, 7):
    if question9 <= 3:
        print("Number " + str(question9) + " is Small")
    else:
        print("Number " + str(question9) + " is Large")
        
print("\n\n")

# Question 10: Complex Program - Combining All Concepts

number = int(input("Enter a number: "))

for question10 in range(1, number +1, 2):
    if question10 < 5:
        print("Low:" + str(question10))
    else:
        print("High:" + str(question10))
        
print("\n\n")

# Bonus Question

for bounus in range(15, -1, -3):
    if bounus == 0:
        print("Blastoff!")
    else:
        print(bounus)