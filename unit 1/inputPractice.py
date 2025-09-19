'''
Filename: inputPractice
Author: Joel Dinovo
Class CIS
Date: 9/19/25

Ask: 
First name
Last name
Favorite Number
Second Number
Favorite Movie
Favorite Food

- Write out a out paragraph outlining the user data using variable. Using the first and second numbers create 3 seprate math equations and print out the values from the expresion
'''

firstName = input("What is your first name? ")
lastName = input("\nWhat is your last name? ")
favColor = input("\nWhat is your favorite color? ")
favShow = input("\nWhat is your favorite show? ")
favMovie = input("\nWhat is your favorite movie? ")
favSong = input("\nWhat is your favorite song? ")
favFood = input("\nWhat is your favorite food? ")

numberOne = input("\nGive me a number: ")
numberTwo = input("Give me another number: ")

print("--------------------------------------------------------------\n")

print("Hello", firstName, lastName + "! I hear that your favorite movie is", favMovie + ", mine too. I also hear that your favorite color is", favColor + ". I think that color is really cool. I can’t believe you like", favFood + ", it is super nasty.", favShow, "is a good song.")

comboOne = int(numberOne) + int(numberTwo)
comboTwo = int(numberOne) * int(numberTwo)
comboThree = int(numberOne) - int(numberTwo)

print(numberOne, "+", numberTwo, "=", comboOne)
print(numberOne, "*", numberTwo, "=", comboTwo)
print(numberOne, "-", numberTwo, "=", comboThree)
