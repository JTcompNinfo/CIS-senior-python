exam1_grade = float(input("Enter score on Exam 1 (out of 100): "))
exam2_grade = float(input("Enter score on Exam 2 (out of 100): "))
exam3_grade = float(input("Enter score on Exam 3 (out of 100): "))

overall_grade = (exam1_grade + exam2_grade + exam3_grade) / 3

print(f"Your overall grade is: {overall_grade:.2f}")
print("\n\n tudent versions")

#Calculates the overall grade for four equally weighted programming assignments, in which each assignment is graded out of 50 points. Hint: First calculate the percentage for each assignment (e.g., score / 50), then calculate the overall grade percentage (be sure to multiply the result by 100).
def calculate_grade(points):
    total_points = int(input("please enter the total number of points for this assingment: "))
    grade = points / total_points
    return grade
    

program1 = int(input("Enter number of points on Program 1: "))
program2 = int(input("Enter number of points on Program 2: "))
program3 = int(input("Enter number of points on Program 3: "))
program4 = int(input("Enter number of points on Program 4: "))

#calculate the percentage
grade1 = calculate_grade(program1)
grade2 = calculate_grade(program2)
grade3 = calculate_grade(program3)
grade4 = calculate_grade(program4)

#claculate the overall grade
progAve = ((grade1 + grade2 + grade3 + grade4) / 4) * 100
print(f"\nStudent overall avrage on programing assignments: {progAve:.2f}")

#Calculates the overall grade for four equally weighted programming assignments, in which assignments 1 and 2 are graded out of 50 points and assignments 3 and 4 are graded out of 75 points.
assing1 = calculate_grade(int(input("Enter the grade for assingment 1: ")))
print()
assing2 = calculate_grade(int(input("Enter the grade for assingment 2: ")))
print()
assing3 = calculate_grade(int(input("Enter the grade for assingment 3: ")))
print()
assing4 = calculate_grade(int(input("Enter the grade for assingment 4: ")))

avg2 = ((assing1 + assing2 + assing3 + assing4) /4) *100
print(f"\nStudent overall avrage on programing assignments: {avg2:.2f}")

#Calculates the overall grade for a course with three equally weighted exams (graded out of 100 points) that account for 60% of the overall grade and four equally weighted programming assignments (graded out of 50 points) that account for 40% of the overall grade. Hint: The overall grade can be calculated as 0.6 * averageExamScore + 0.4 * averageProgScore.

overallAvg = (overall_grade * 0.5) +(progAve * 0.4) + (avg2 * 0.1)
print(f"The students overall average is {overall_grade:.2f}")