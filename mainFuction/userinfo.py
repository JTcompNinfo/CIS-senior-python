# Program entry
def main():
    """
    Main Fuction - controls program flow
    
    """
    print("Welcome to profile Creator")
    print("-" * 30)
    
    user_name = greet_user()
    user_age = get_age()
    
    display_info(user_name, user_age)
    print("\nThank you for using Profile Creator")
    
def greet_user():
    name = input("What is your name")
    print("Hello", name)
    return name
    

def get_age():
    age = int(input("ow old are you"))

def display_info(name, age):
    print("\n===Your profile===")
    print("Name:", name)
    print("Age:", age)
    print("Grade Level: Senior")

if __name__ == "__main__":
    main()