"""Game logic module for Rock, Paper, Scissors."""


def determine_winner(player_choice, computer_choice):
    """Determine the winner of a Rock, Paper,
    Scissors round from the player's perspective.
    """
    valid_choices = ["rock", "paper", "scissors"]
    if player_choice not in valid_choices or computer_choice not in valid_choices:
        raise ValueError("Invalid choice.")
    if player_choice == computer_choice:
        return "tie"
    winning_combos = {("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")}
    if (player_choice, computer_choice) in winning_combos:
        return "win"
    return "lose"
