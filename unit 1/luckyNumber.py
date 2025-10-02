import random

# Game statistics
total_rounds = 0
total_wins = 0
total_guesses = 0

print("=" * 50)
print("  WELCOME TO THE LUCKY NUMBER GUESSING GAME!")
print("=" * 50)
print()

# Main game loop - play multiple rounds
# TODO: Use while True loop with break statement here

# Generate random lucky number
# TODO: Use random.randint() to generate number between 1 and 50

# Set maximum attempts
# TODO: Set max_attempts to 7

# Initialize attempt counter
# TODO: Create attempts variable starting at 0

print(f"\nRound {total_rounds + 1}")
print("I'm thinking of a lucky number between 1 and 50...")
print(f"You have {max_attempts} attempts to guess it!")
print()

# Guessing loop - count-controlled while loop
# TODO: Use while loop that continues while attempts < max_attempts

    # Get user's guess
    # TODO: Get input and convert to integer
    
    # Increment attempt counter
    # TODO: Add 1 to attempts
    
    # Check if guess is correct
    # TODO: Compare guess to lucky_number
    
        # Player wins!
        # TODO: Display success message
        # TODO: Update statistics
        # TODO: Break out of guessing loop
        
    # Provide hints
    # TODO: Tell user if guess is too high or too low
    
# If loop completes without break, player lost
# TODO: Handle case where player runs out of attempts

# Display round statistics
# TODO: Show attempts used, win/loss for this round

# Ask if player wants to play again
# TODO: Get input and check if user wants to continue
# TODO: Use break statement to exit main game loop if done

# Display final statistics
# TODO: Show total rounds, wins, and average guesses per round

print("\nThanks for playing! Goodbye!")