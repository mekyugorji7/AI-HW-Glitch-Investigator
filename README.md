# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] **Describe the game's purpose.**  
  The app is a Streamlit number-guessing game where players choose a difficulty, make guesses, and get higher/lower hints while tracking attempts and score.
- [x] **Detail which bugs you found.**  
  I found reversed hint messages, broken new-game reset behavior (game stayed in won/lost state), and test/import issues that prevented `pytest` from running cleanly.
- [x] **Explain what fixes you applied.**  
  I corrected `check_guess` hint direction, fixed new-game/session-state reset (`attempts`, `status`, `history`, and difficulty-based secret range), refactored logic into `logic_utils.py`, and added/updated pytest regression tests until all tests passed.

## 📸 Demo

- [x] [<img width="1497" height="859" alt="image" src="https://github.com/user-attachments/assets/be6bb4f8-4ef4-4139-a977-2ccf2344b085" />


