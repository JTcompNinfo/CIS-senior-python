'''
investBook.py 
Joel Dinovo
9/23/25
comp info sci

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
intrestRate = intrestRate / 100
# intiailzie the accumulator

totalIntrest = 0.0

#Display the header for the table
print("%4s%18s%10s%16s" % ("Year", "Starting balance", "Interest", "Ending balance"))

# compute and display the results for each year

for year in range(1, yearsInvest + 1):
    intrest = startInvest * intrestRate
    endBalance = startInvest + intrest
    print("%4d%18.2f%10.2f%16.2f" % (year, startInvest, intrest, endBalance))
    startInvest = endBalance
    totalIntrest += intrest
    
    
#Display the totals for the period
print("Ending balance$%0.2f" % endBalance)
print("Total intrest amount $%0.2f" % totalIntrest)