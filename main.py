best_xi = [
    'Travis Head', 'Sunil Narine', 'Virat Kohli', 'Riyan Parag', 'Venkatesh Iyer',
    'Andre Russell', 'Heinrich Klaasen', 'Mitchell Starc', 'Thangarasu Natarajan',
    'Varun Chakravarthy', 'Jasprit Bumrah'
]

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
        player = input(f"Enter player {len(user_team) + 1}: ").strip()

        if player in best_xi and player not in user_team:
            user_team.append(player)
            print(f"{player} added to your team!")
        elif player in user_team:
            print(f"{player} is already in your team!")
        else:
            print(f"{player} is not in the Best XI. Try again!")

        print(f"Current team: {', '.join(user_team)}")
        print(f"Players matched: {len(user_team)} / 11")
        print(f"Your team rating: {rate_team(len(user_team))}")

    print(f"🎉 Congratulations! You built the Best XI! Your final team: {', '.join(user_team)}")

# Start the game
game()
