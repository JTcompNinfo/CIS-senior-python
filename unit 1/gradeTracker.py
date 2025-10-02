'''
gardeTracker.py
Joel Dinovo
CIS seniors
10/1/25
'''

import math

print("Welocme to your new Grade Tracker")

print("\n\n")

numStu = int(input("How many students are in your class? "))
print("You will enter grades for", numStu, "students")
print("-" *40)

print("\nEnter student data")

names = []
numScores =[]
letScore = []
# get info
for count in range (1, numStu + 1):
    print("Student #" + str(count))
    name = input("\tEnter Students name: ")
    score = int(input("Enter their score: "))
    names.append(name)
    numScores.append(score)
    
#get letter grades
for times in range (1, numStu + 1):
    if numScores[times - 1] >= 90:
        letter = "A"
    elif numScores[times - 1] >= 80:
        letter = "B"
    elif numScores[times - 1] >= 70:
        letter = "C"
    elif numScores[times - 1] >= 60:
        letter = "D"
    else:
        letter = "F"
    
    letScore.append(letter)

classTotal = 0
for numbers in range(1, numStu + 1):
    classTotal += numScores[numbers - 1]
    
classAvg = classTotal / numStu

passing = []
passTimes = 0

for see in range(0, numStu):
    if numScores[see]  >= 70:
        didit = True
        passTimes += 1
    else: 
        didit = False
    passing.append(didit)


gradeA = 0
gradeB = 0
gradeC = 0
gradeD = 0
gradeF = 0


for loop in range(0, numStu):
    if letScore[loop] == "A":
        gradeA += 1
    elif letScore[loop] == "B":
        gradeB += 1
    elif letScore[loop] == "C":
        gradeC += 1
    elif letScore[loop] == "D":
        gradeD += 1
    elif letScore[loop] == "F":
        gradeF += 1
passPecent = passTimes / numStu * 100
print("Class Summary")
print('\tTotal Students:', numStu)
print('\tTotal Points:', classTotal)
print('\tClass Avrage:', classAvg)
print('\tHighest Score:', max(numScores))
print('\tLowest Score:', min(numScores))
print('\tPassing students: ' + str(passTimes) + "/" + str(numStu))
print('\tPassing rate:', passPecent)

print("\n\n")

print("Grade distbuation")
print("\tGrade A:", gradeA)
print("\tGrade B:", gradeB)
print("\tGrade C:", gradeC)
print("\tGrade D:", gradeD)
print("\tGrade F:", gradeF)

gradOkay = []

for avrage in range(0, numStu):
    if numScores[avrage] >= 80:
        okay = "Above average"
    else:
        okay = "Below average"
    gradOkay.append(okay)
    
print("\n\nIndivdual Scores")

for last in range (0, numStu):
    print(names[last] + ": " + str(numScores[last]) + " (" + str(letScore[last]) + ") - " + gradOkay[last])