'''
investmeant.py
Joel Dinovo
CIS seniors
9/22/25

Compute an Investent amount
1. The inputs are:
    starting investment amount
    number of years
    Intrest rate (an intrger percent)
    
2. The report is displayed in tabular form with a header
3. computataions and outputs:
    for each year of the investment
        compput the intrest and add it ti the investmnt
        print a formatted row of reults for that year
4. The ending investment and interest paid in total are also displayed
'''
#Accept the inputs
startInvest = float(input("How much was your starting Investmeant: "))
yearsInvest = int(input("How many years has this lasted: "))
intrestRate = int(input("What is the intrest rate as a whole number: "))

# make the rate into a decmiale
intrestRate = intrestRate / 100

#set total to work with
investforYear = startInvest

# start loop
loop = 0
print("you start with $" + str(startInvest))
while loop < yearsInvest:
    loop = loop + 1
    #calculate the new total
    investforYear = (investforYear * intrestRate) + investforYear
    print("In year", loop, "you have $" + str(investforYear))