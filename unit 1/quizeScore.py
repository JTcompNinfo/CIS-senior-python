'''
quizeScore.py
Joel Dinovo
Comp Info Sci
9/25/25
'''
lst=[]
name =input("What is the Student's name? ")
questionsTotal = int(input("How many questions are there? "))
studentScore = 0
print("\n\nTrue and 0 for false")
for count in range(1, questionsTotal + 1):
    pointScore = int(input("Question #" + str(count) + " True or Flase "))
    lst.append(pointScore)
    
    ''''if pointScore == "yes" or "1":
        pointScore = 1
    else: 
        pointScore = 0
    studentScore += pointScore'''
    
print(lst)
'''    
quizeScore = (studentScore / questionsTotal) * 100

if quizeScore >= 70:
    print(name, "passed with a score of %0.1f" % quizeScore + ("!"))
else: 
    print(name, "failed with a score of %0.1f" % quizeScore + ("."))

    '''