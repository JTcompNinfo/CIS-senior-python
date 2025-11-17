def display_welcome():
    pass

def get_college_count():
    """
    Number of colleges the user is applying to
    return
        count (int)
    """
    
    count = int(input("How many colleges have you applied for? "))
    return count
    
def get_application_cost(num_colleges):
    """
    Calculate total apliction cost
    
    return 
        total_cost (float)
    """
    total_cost = float(num_colleges * 50)
    return total_cost
    
def get_sat_score():
    """
    get users sat score
    return
        score (int)
    """
    score = int(input("What is your SAT score? "))
    return score
    
def analyze_sat(score):
    """
    provide feedback on sat
    >= 1400 - excellent
    >= 1200 - good score
    >= 1000 - solid foundation
    else - consider retakinf to improve college options
    """
    if score >= 1400:
        feedback = "Excellent"
    elif score >= 1200:
        feedback = "Good Score"
    elif score >= 1000:
        feedback = "Good Score"
    else:
        feedback = "Consider retakinf to improve college options"
    return feedback

def display_summary(colleges, cost, sat_score, sat_feedback):
    print("Number of colleges:", colleges)
    print("Total cost:", cost)
    print("SAT score", sat_score)
    print("SAT Feedback:", sat_feedback)
    
    

def main():
    #Welcome the user
    display_welcome()
    
    #Collect some info
    num_colleges = get_college_count()
    total_cost = get_application_cost(num_colleges)
    sat = get_sat_score()
    
    # Analyze data
    feedback = analyze_sat(sat)
    
    #displya results
    display_summary(num_colleges, total_cost, sat, feedback)



# Entry Point
if __name__ == "__main__":
    main()