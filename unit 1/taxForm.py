'''
taxForm.py
Joel Dinovo
CIS Seniors
9/22/25

Compute a person's income tax
1. Significant constants
    tax rat 
    standard deduction
    deduction per dependant


2. The inputs are gross income
    number of de[endants

3. Computations:
    taxable income = gross income - the standard deduction - a deduction for each dependant
    income tx = is a fixed percentage of the tax income
    
4. The outputs are:
    the income tax
'''
print("\n\nMy Tax Rate Calculator")
print("=" * 40)
# Initiialize the constants
TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.0
DEPENDANT_DEDUCTION = 3000.0

#request the inputs
grossIncome = float(input("Enter the gross income:"))
numDependants = int(input("Enter the number of dependants: "))

# Compute Things
taxableIncome = grossIncome - STANDARD_DEDUCTION - DEPENDANT_DEDUCTION * numDependants
incomeTax = taxableIncome * TAX_RATE

#Display the income tax
print("The income tex is $" + str(incomeTax) + "\n\n")