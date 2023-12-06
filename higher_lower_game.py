import random
from art import logo, vs
from game_data import data
from replit import clear

def get_value_from_data(celebrity):
    # access the values in the data dictionary from the game_data.py file and access 2 accounts randomly
    first_account = random.choice(celebrity)
    remaining_data = [account for account in celebrity if account != first_account]
    second_account = random.choice(remaining_data)
    return first_account, second_account

def compare_follower():
    # Main game loop.
    is_game_over = False
    score = 0
    versus_data1, versus_data2 = get_value_from_data(data)  # Initial data selection

    while not is_game_over:
        # Displaying the comparison options to the user.
        print(f"Compare A: {versus_data1['name']}, {versus_data1['description']}, from {versus_data1['country']}.")
        print(vs)  # Display versus symbol
        print(f"Compare B: {versus_data2['name']}, {versus_data2['description']}, from {versus_data2['country']}.")

        # User makes a choice between two options.
        choose_side = input("Who has more followers? Type 'A' or 'B': ").lower()

        # Check if user's choice is correct and update score.
        if (choose_side == "a" and versus_data1['follower_count'] > versus_data2['follower_count']) or \
           (choose_side == "b" and versus_data2['follower_count'] > versus_data1['follower_count']):
            score += 1
            clear()  # Clear the screen for next round
            print(f"You're right! Current score: {score}.")
            versus_data1 = versus_data2  # Update versus_data1 to the current versus_data2
            _, versus_data2 = get_value_from_data(data)  # Get new versus_data2
        else:
            # End the game if the user's choice is incorrect.
            clear()
            is_game_over = True
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")

# Start the game
compare_follower()

