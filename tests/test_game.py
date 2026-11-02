"""Unit tests for the determine_winner game logic."""

import pytest
from game import determine_winner


@pytest.mark.parametrize(
    "player,computer,expected",
    [
        ("rock", "scissors", "win"),
        ("scissors", "paper", "win"),
        ("paper", "rock", "win"),
        ("scissors", "rock", "lose"),
        ("paper", "scissors", "lose"),
        ("rock", "paper", "lose"),
        ("rock", "rock", "tie"),
        ("paper", "paper", "tie"),
        ("scissors", "scissors", "tie"),
    ],
)
def test_determine_winner_outcomes(player, computer, expected):
    """Test all valid 9 matchups for correct outcome."""
    assert determine_winner(player, computer) == expected


def test_determine_winner_invalid_choice():
    """Test that invalid choices raise ValueError."""
    with pytest.raises(ValueError):
        determine_winner("lizard", "rock")
    with pytest.raises(ValueError):
        determine_winner("", "paper")
