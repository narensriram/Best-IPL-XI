import random

# Best IPL XI Selection (Can be customized)
best_xi = [
    'Travis Head', 'Sunil Narine', 'Virat Kohli', 'Riyan Parag', 'Venkatesh Iyer',
    'Andre Russell', 'Heinrich Klaasen', 'Mitchell Starc', 'Thangarasu Natarajan', 
    'Varun Chakravarthy', 'Jasprit Bumrah'
]

# Function to rate the user's team based on how many players match the Best XI
def rate_team(user_team):
    matching_players = sum(1 for player in user_team if player in best_xi)

    # Assign a rating based on the number of correct players
    if matching_players == 11:
        rating = "Best 🏆"
    elif matching_players >= 9:
        rating = "Great 🔥"
    elif matching_players >= 6:
        rating = "Good ✅"
    elif matching_players >= 3:
        rating = "Average ⚠️"
    else:
        rating = "Worst ❌ "

    return matching_players, rating

# Main game function with an interactive loop
def ipl_random_xi_game():
    print("\n🏏 Welcome to the IPL Best XI Game! 🏏\n")
    print("🔹 RULES:")
    print("   - Enter the **full name** of each player.")
    print("   - **Correct spelling and capitalization are required!**")
    print("   - Build a full **XI-player team**.")
    print("   - Have fun! 🎉\n")

    user_team = []

    while len(user_team) < 11:
        print(f"\n✅ You have {len(user_team)} players so far.")

        player = input(f"Enter player {len(user_team) + 1}: ").strip()

        if player in best_xi and player not in user_team:
            user_team.append(player)
            print(f"🎯 **{player}** added to your team!")

        elif player in user_team:
            print(f"⚠️ **{player}** is already in your team! Choose another player.")

        else:
            print(f"❌ **{player}** is not in the Best XI. Try again!")

        # Update rating after each attempt
        matching_players, rating = rate_team(user_team)

        print(f"\n⭐ **Players matched:** {matching_players} / 11")
        print(f"🏆 **Your current team rating:** {rating}")

    # Game Over Message
    print("\n🎉 **Congratulations! You successfully built an IPL Best XI!** 🎉")
    print(f"🏏 **Your final team:** {', '.join(user_team)}")
    print("✅ **Game Over.**")

# Run the game
ipl_random_xi_game()
