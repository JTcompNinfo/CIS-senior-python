'''
bmiCalc.py
Joel Dinovo
CIS seniors
9/23/25


'''
print("== PERSONAL FITNESS TRACKER ==")

print("\nWelcome to your personalized fitness tracker!")

#colect important data
name = input("What is your name? ")
age = int(input("What is your age? "))
weight = float(input("What is your weight in pounds? "))
height = int(input("What is your height in inches? "))
weeklyExercise = float(input("How many hors do you exercise per week? "))
goal = input("What is your fitness goal? ")

#calculations
bmi = (weight / (height ** 2)) * 703
weeklyCalories = weeklyExercise * 300
dailyExercise = (weeklyExercise * 60) / 7

#outputs


print()
print("=" * 40)
print("\t\tFITNESS REPORT FOR", name.upper())
print("=" * 40)

print("\nPersonal Infromation:")
print("\tName:", name)
print("\tAge:", age, "years old")
print("\tWeight:", weight, "lbs")
print("\tHeight:", height, "inches")

print("\nFitness Metrics:")
print("\tBMI:", bmi)
print("\tWeekly Exercise:", weeklyExercise, "hours")
print("\tDaily Exercise:", dailyExercise, "minutes per day")
print("\tEstimated Weekly Calories Burned:", weeklyCalories, "calories")

print("\nFitness Goal:", goal)

print("Keep up the good work!")
print("=" * 40)