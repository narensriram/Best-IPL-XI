import random

# A list of top IPL players (just an example, in reality, you can include actual stats or ratings)
best_xi = [
    'Travis Head','Travis', 'Head' 'Sunil Narine','Sunil', 'Narine' 'Virat Kohli','Virat', 'Kohli' 'Riyan Parag', 'Riyan', 'Parag' 'Venkatesh Iyer','Venky', 'Venkatesh'
    'Andre Russell','Andre', 'Russell' 'Heinrich Klaasen','Heinrich','Klaasen' 'Mitchell Starc','Mitchell', 'Stark' 'Thangarasu Natarajan','Nattu', 'Natarajan', 'T Natarajan','Varun Chakravarthy', 'Varun', 'Chakravarthy' 'Jasprit Bumrah','Jasprit', 'Bumrah'

]


# Function to rate the user's team based on matching the best XI
def rate_team(user_team):
    matching_players = 0

    # Using a for loop to check how many players match with the best XI
    for player in user_team:
        if player in best_xi:
            matching_players += 1

    # Rate the team based on how many players match
    if matching_players == 11:
        rating = "Best"
    elif matching_players >= 9:
        rating = "Great"
    elif matching_players >= 6:
        rating = "Good"
    elif matching_players >= 3:
        rating = "Average"
    else:
        rating = "Worst"

    return matching_players, rating


# Main game function with a loop
def ipl_random_xi_game():
    print("Welcome to the IPL Random XI Generator!")

    # This will be the user's team list
    user_team = []

    while len(user_team) < 11:  # Keep running until the user team has 11 correct players
        print(f"\nYou currently have {len(user_team)} correct players.")

        # Ask the user to input 11 players using a for loop
        player = input(f"Enter player {len(user_team) + 1}: ").strip()

        # If player is valid (part of the "best XI") and not already in the team
        if player in best_xi and player not in user_team:
            user_team.append(player)
            print(f"{player} added to your team!")
        elif player not in best_xi:
            print(f"{player} is not in the best XI, try again!")
        else:
            print(f"{player} is already in your team. Please pick another player.")

        # Check how many correct players are in the team
        matching_players, rating = rate_team(user_team)

        # Display the rating and give feedback
        print(f"\nPlayers matched with the Best XI: {matching_players} out of 11")
        print(f"Your team's rating so far: {rating}")

    # Game ends when all 11 players are correct
    print("\nCongratulations! You've successfully built the Best IPL XI!")
    print(f"Your team: {', '.join(user_team)}")
    print("Game Over.")


# Start the game
ipl_random_xi_game()
