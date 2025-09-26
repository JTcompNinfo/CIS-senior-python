'''
quizeScore.py
Joel Dinovo
Comp Info Sci
9/25/25
'''
# set main list up
studentAwnser=[]
rightAwnser=[] 

print("\n")
print("=" * 40)
print("\n")

#get user info and question amount

name =input("What is the Student's name? ")
questionsTotal = int(input("How many questions are there? "))
studentScore = 0

print("\n")
print("=" * 40)
print("\n")

#Get student answers

print("1 for True and 0 for false")
for count in range(1, questionsTotal + 1):
    question = int(input("Question #" + str(count) + " True or Flase "))
    studentAwnser.append(question)
    
print("\n")
print("=" * 40)
print("\n")

#Get correct answers

for times in range(1, questionsTotal + 1):
    awnser = int(input("What is the correct answers to question " + str(times) + "? "))
    rightAwnser.append(awnser)
    
print("\n")
print("=" * 40)
print("\n")
    
    #Calculate which ones are wrong
x = 0

for scoring in range(1, questionsTotal + 1):
    
    if studentAwnser[x] == rightAwnser[x]:
        print("Question " + str(scoring) + ": Correct")
        studentScore += 1
    else:
        print("Question " + str(scoring) + ": Wrong")
    x += 1
    

#get score

quizeScore = (studentScore / questionsTotal) * 100

print("\n")
print("=" * 40)
print("\n")

# print results

if quizeScore >= 70:
    print(name, "passed with a score of %0.1f" % quizeScore + ("!"))
else: 
    print(name, "failed with a score of %0.1f" % quizeScore + ("."))
