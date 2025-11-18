'''
Personal Finance Manger
Program: personalFincance.py
Author: JT
Date: 11/18/2025

This porgram demonstrates proper Python program using a main() function and helper functions to coordinate program flow.
'''

def display_header():
    """
    Display the program and welcome message
    This function has no parameters and returns nothing
    """
    
    print("\n\n\n")
    print("=" * 50)
    print("            PERSONAL FINACE MANAGER")
    print("            Plan Your College Budget")

def get_user_name():
    """
    Get the user's name
    
    returns:
        name (str)
        
        NOTE: We use a seprate function for this to keep each function doing ONE specific task
    """
    
    name = input("What is your name? ")
    return name

def get_income():
    """
    Get and return user's monthly income
    
    returns:
    INCOME (FLOAT): MONTHLY INCOME IN $
    """
    print("\nEnter your monthly income: $", end="")
    income_str = input()
    income = float(income_str)
    return income

def get_expenses():
    """
    Collect all expense categories from the user
    
    returns:
    expenses_dict (dict)
    total_expenses (float)
    NOTE: This function demastres collecting multiple related inputs and organizing them into a dictipnary for easy access later
    """
    print("\n--- EXPENSE TRACKING ---")
    
    #dictinary to store all expenses
    expenses = {}
    
    #Get each expense category
    print("Enter your rent/housing cost : $", end="")
    expenses['Rent/Housing'] = float(input())
    
    print("Enter your food/grocery budget : $", end="")
    expenses['Food/Groceries'] = float(input())
    
    print("Enter your transportation cost : $", end="")
    expenses['ransportation'] = float(input())
    
    print("Enter your entertainment budget : $", end="")
    expenses['Entertainment'] = float(input())
    print("Enter your savings goal budget : $", end="")
    expenses['Savings'] = float(input())
    
    print("Enter your miscellaneous exoenses : $", end="")
    expenses['Miscellaneous'] = float(input())
    
    # calculate total expenses
    total = sum(expenses.values)
    
    # return
    
    return expenses, total

def calulate_remaining(income, expnses):
    pass

def provide_feedback(remaining, income):
    pass

def display_summary(name, income, expenses_dict, total_expneses, remaing, feedback):
    pass

def main():
    """
    Mainfunction cordnate the whole program
    
    Notice how main() reads like a story:
    1. Display header
    2. Get user infomation
    3. get expnses
    4. Calulate results
    5. Get Feedback
    6. Display summary
    7. Say goodbye
    
    Each step is one function call, making logic easy to follow
    """
    
    #Display welcome
    display_header()
    print("Welcome! Let's track your monthly finances.\n")
    
    # Get user info
    user_name = get_user_name
    monthly_income = get_income()
    
    #Get expenses
    # NOTE: This functions returns two values (tuple unpacking) 
    expense_categories, total_expenses = get_expenses()

if __name__ == "__main__":
    main()