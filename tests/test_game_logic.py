import sys
from pathlib import Path

# FIX: Added with AI troubleshooting so pytest can import project modules reliably from tests/.
sys.path.append(str(Path(__file__).resolve().parents[1]))

from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


def test_hint_direction_stays_correct_when_secret_is_string():
    # FIX: AI-paired regression case for the mixed-type secret path that previously caused hint confusion.
    outcome, message = check_guess(60, "50")
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_check_guess_returns_correct_directional_hint():
    """
    FIX: AI-assisted regression test for the hint-direction bug where a low guess
    could incorrectly tell the player to guess lower.
    """
    outcome, message = check_guess(1, 8)
    assert outcome == "Too Low"
    assert "HIGHER" in message
