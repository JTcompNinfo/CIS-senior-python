# Import statements
import math

# Constants (ALL_CAPS naming convention)
APPLICATION_FEE = 75.00
AVG_ACCEPTANCE_RATE = 55.0
MAX_IDEAL_DISTANCE = 500

# Welcome message
print("=" * 70)
print("🎓 COLLEGE COLLEGE APPLICA APPLICATION TION TRACKER TRACKER 🎓")
print("=" * 70)
# Your welcome code here

# Variables for student info
# Your code here
name = input("\nWhat is your name? ")

print("\nWelcome", name + "! Let's track your college applications.")

# Lists to store college data
# Your code here
print("\nPlease enter information for 3 colleges you're considering: \n")

# Data collection loop or individual inputs
# Your code here
college_name = []
location = []
anual_tuition = []
distance = []
acceptance_rate = []

for count in range(1,4):
    print("---College #" + str(count) + "---")
    college_name.append(input("College name: "))
    location.append(input("Location (City, State): "))
    anual_tuition.append(float(input("Annual tuition ($): ")))
    distance.append(float(input("Distance from home (miles): ")))
    acceptance_rate.append(float(input("Acceptance rate (%): ")))
    print()

# Calculations using Math module
# Your code here
classifaction = []

for meep in range(0,3):
    if acceptance_rate[meep] >= 70:
        classifaction.append("Safety")
    elif acceptance_rate[meep] >= 40:
        classifaction.append("Match")
    else:
        classifaction.append("Reach")


# Summary report with f-strings
# Your code here
for times in range(0,3):
    print("College " + str(times + 1) + ": " + college_name[times])
    print("Annual Tuituon: $" + str(anual_tuition[times]))
    print("Distance from Home: " + str(distance[times]) + " miles")
    print("Acceptance Rate: " + str(acceptance_rate[times]))
    print("Classification: " + str(classifaction[times]))
    print("4-Year Total Cost: $" + str(anual_tuition[times] * 4))
    print("\n")
    
print("=" * 70)
print("💰 FINANCIAL ANALYSIS")
print("=" * 70)