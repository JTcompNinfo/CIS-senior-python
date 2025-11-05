# Challenge: Complete Grade Book System

# Create a list of student dictionaries
student1 = {}
student2 = {}
student3 = {}
grade_book = [
    student1, 
    student2, 
    student3
]

def print_class_report(students):
    """Prints a formatted report for all students"""
    for student in students:
        student["name"] = input("Enter Student name: ")
        student["id"] = input(f"Enter Student id of {student["name"]}: ")
        student["math"] = int(input(f"Enter {student["name"]}'s Math grade: "))
        student["english"] = int(input(f"Enter {student["name"]}'s English grade: "))
        student["science"] = int(input(f"Enter {student["name"]}'s Science grade: "))
        student["history"] = int(input(f"Enter {student["name"]}'s History grade: "))
        student["avg"] = (student["math"] + student["science"] + student["english"] + student["history"]) / 4
        
        print("\n\n")
        
        

        
    # Your code here
    pass

def find_top_student(students):
    """Returns the student with the highest average"""
    top_student = students[0]  

    for student in students:
        if student["avg"] > top_student["avg"]:
            top_student = student
            
    return top_student
    pass

def count_honor_students(students):
    """Counts students with average >= 90"""
    # Your code here
    count = 0
    for student in students:
        if student["avg"] >= 90:
            count += 1
            
    return count
    pass

# Test your functions
print_class_report(grade_book)
top = find_top_student(grade_book)
count =count_honor_students(grade_book)

for student in grade_book:
    print(f"Student: {student["name"]}")
    print(f"ID: {student["id"]}")
    print(f"Math: {student["math"]}")
    print(f"English: {student["english"]}")
    print(f"Science: {student["science"]}")
    print(f"History: {student["history"]}")
    print(f"Average: {student["avg"]}")
    
    print("-" * 20)
    print()
    
    
print(f"Top Student: {top["name"]}")
print(f"Average: {top["avg"]}")
print(f"Honor Roll Students (avg >= 90): {count}")
print(f"Total Students: {len(grade_book)}")