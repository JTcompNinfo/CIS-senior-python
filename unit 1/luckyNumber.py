import random

# Game statistics
total_rounds = 0
total_wins = 0
total_guesses = 0

print("=" * 50)
print("  WELCOME TO THE LUCKY NUMBER GUESSING GAME!")
print("=" * 50)
print()

# Start game
while True:
    
    # Get the random number
    luckyNum = random.randint(1,50)
    
    # Set round values
    max_attempts = 7
    
    attemps = 0
    
    total_rounds += 1
    
    result = ""
    
    # Inital instructions
    print(f"\nRound", total_rounds)
    print("I'm thinking of a lucky number between 1 and 50...")
    print(f"You have", max_attempts, "attempts to guess it!")
    print()
    
    
    # Guessing loo-
    while attemps < max_attempts:
        #Total guesses left
        print("Number of attemps: " + str(attemps) +"/7")
        #add attemp by 1 and total guesses by 1
        attemps+=1
        total_guesses+=1
        #user input
        num = int(input("Enter a number between 1 and 50: "))
        #Win condition
        if num == luckyNum:
            print("You guessed right!")
            total_wins += 1
            result = "Win"
            break
        
        #Hints
        if num >  luckyNum:
            print("Too big")
        elif num < luckyNum:
            print("Too small")
        print()
        
        
    #if you lose 
    if result != "Win":
        print("You lose!")
        result = "Lost"
        
        
    #round stats
    print("\nYou", result, "with " + str(attemps) +"/7 attemps\n")
    
    #see if user wants to play again
    again = input("Do you want to play again? Type 'No' To stop. ").lower()
    
    
    if again == "no":
        break
   
# final stats
print("\n\n") 
print("Total wins:", total_wins)
print("Total guesses:", total_guesses)
print("Total rounds:", total_rounds)
print("\nThanks for playing! Goodbye!")