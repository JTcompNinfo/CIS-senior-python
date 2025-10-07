# Python Variable Name Validator
# Student Name: Joel Dinovo
# Date: 10/7/2025

# List of Python keywords
python_keywords = [
    'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'
]

# Display welcome message
print("=== PYTHON VARIABLE NAME VALIDATOR ===")
print("This program checks if your variable name is valid in Python.")
print()

# Get user input
variable_name = input("Enter a variable name to validate: ")

# Your validation code goes here
invalid_start_charachters = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

invalid_charachters = [
    ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '`', '{', '|', '}', '~'
]
passing = True

while True:
    if variable_name == "":
        print("Invalid input, must enter at least one charcter")
        passing = False
        break
    for number in range(0, 35):
        if variable_name == python_keywords[number]:
            print(python_keywords[number], "is a python keyword.")
            print("Varibales can not be a python keyword.")
            passing = False
            break
    if passing == False:
        break
    for loop in range(0, 10):
        if variable_name.startswith(invalid_start_charachters[loop]):
            print("Variables can not start with a number.")
            print("Variables can only start with an underscore or a letter")
            passing = False
            break
    if passing == False:
            break
    for times in range(0, 32):
        if invalid_charachters[times] in variable_name:
            print("You can not use special characters in your variable")
            print("Variables can only containe numbers, letters, and underscores")
            passing = False
            break
    if passing == False:
            break
    break
if passing:
    print("'" + variable_name + "' is a vaid variable name.")
# Check each rule and provide appropriate feedback
