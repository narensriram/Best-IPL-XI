best_xi = [
    'Travis Head', 'Sunil Narine', 'Virat Kohli', 'Riyan Parag', 'Venkatesh Iyer',
    'Andre Russell', 'Heinrich Klaasen', 'Mitchell Starc', 'Thangarasu Natarajan',
    'Varun Chakravarthy', 'Jasprit Bumrah'
]

# Create a dictionary to map both first and last names to full names
best_xi_dict = {}
for player in best_xi:
    full_name = player.lower()
    first_name, last_name = full_name.split(" ", 1)  # Split into first and last name
    
    best_xi_dict[full_name] = player  # Store full name
    best_xi_dict[first_name] = player  # Store first name
    best_xi_dict[last_name] = player  # Store last name

def rate_team(matching_players):
    if matching_players == 11:
        return "Best 🏆"
    elif matching_players >= 9:
        return "Great 🔥"
    elif matching_players >= 6:
        return "Good ✅"
    elif matching_players >= 3:
        return "Average ⚠️"
    return "Worst ❌"

def game():
    user_team = []
    
    while len(user_team) < 11:
        input_player_name = input(f"Enter player {len(user_team) + 1}: ").strip().lower()

        if input_player_name in best_xi_dict:
            full_name = best_xi_dict[input_player_name]

            if full_name not in user_team:
                user_team.append(full_name)
                print(f"{full_name} added to your team!")
            else:
                print(f"{full_name} is already in your team!")
        else:
            print(f"{input_player_name} is not in the Best XI. Try again!")

        print(f"Current team: {', '.join(user_team)}")
        print(f"Players matched: {len(user_team)} / 11")
        print(f"Your team rating: {rate_team(len(user_team))}")

    print(f"🎉 Congratulations! You built the Best XI! Your final team: {', '.join(user_team)}")

# Start the game
game()

