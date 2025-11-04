'''
Student Grade Booke manger

Program: pyDict.py
Author: Joel Dinovo
Date: 11/04/2025

- Student ID: "S12345"
- Grade Level: 12
- Email: "emma.r@school.edu"
- Math grade: 95
- English Grade: 88
- Scince grade: 88
- Scince grade: 92
- Homework Completed: True

Tasks:
1. Create a dictionary called student 1 with all the infromation above
2. print the entire dictinary
3. print just emma' email address
4. print just emma's math grade
'''

#Part 1: Create your dictinary here
student1 = {
    "name": "Emma Rodriguez",
    "student_id": "S12345",
    "grade_level": 12,
    "email": "emma.r@school.edu",
    "math_grade": 95,
    "english_grade": 88,
    "scince_grade": 92,
    "homework_completed": True
}


# Print the entire dictinary
print("Complete student record:")
print(student1)

#print specific values
print("\nStudent email:", student1["email"])
print("Math grade:", student1["math_grade"])

# Part 2 

# Modify emms's homework status
student1["homework_completed"] = False

#update her english grade
student1["english_grade"] = 91

# add history grade
student1["history_grade"] = 89

# add clubs infromation
student1["clubs"] = ["Deabte Team", "Math Club"]

print("\nUpdated student Record")
print(student1)

# Part 3: Create a function to calculate avrage grade
def calculate_average(student): 
    # Get all the grades
    math = student1["math_grade"]
    english = student1["english_grade"]
    scince = student1["scince_grade"]
    history = student1["history_grade"]
    
    # Calculate average
    avg = (math + english + scince + history) / 4
    
    # Return the average
    return avg
    
    
#test your function
#function call:
average = calculate_average(student1)
print(f"\n{student1['name']}'s average grade: {average:.2f}")

# Part 4: using dictinary methods

# print all keys
print("\nAll values in the dictinary")
print(student1.keys())



#pirnt all key values
print("\nAll the key-value pairs")
print(student1.items())



# safely get phone number
phone = student1.get("phone_number")
print("\nPhone number:", phone)

student2 = {
    "name": "Marcus Chen",
    "student_id": "S12346"
}
#grade level 11, math 87, scince 90, english 85
student2.update({"grade": 11,"math_grade": 87, "scince_grade": 90,  "english_grade": 85})

print("\nNew student record")
print(student2)