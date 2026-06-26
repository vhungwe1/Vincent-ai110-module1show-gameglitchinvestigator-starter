# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Activate virtual environment: `.venv\Scripts\activate`
3. Run the app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab to see 
   the secret number. Try to win.
2. **Find the State Bug.** The secret number was switching between 
   a number and text on every even attempt, causing random behavior.
3. **Fix the Logic.** The hints ("Higher/Lower") were completely 
   backwards. Fixed by swapping the messages in check_guess.
4. **Refactor and Test.** Moved all logic into `logic_utils.py` 
   and ran pytest until all tests passed.

## 📝 Document Your Experience

- [x] The game is a number guessing game where the player tries to 
      guess a secret number within a limited number of attempts. 
      The game gives hints after each guess and tracks your score.

- [x] Bugs found:
      1. Hints were backwards — "Go Higher" showed when guess was 
         too high and "Go Lower" showed when guess was too low.
      2. Hard difficulty range was 1-50, easier than Normal (1-100).
      3. Secret number switched between integer and string on even 
         attempts, causing random hint failures.
      4. Wrong guesses on even attempts added 5 points instead of 
         subtracting them.

- [x] Fixes applied:
      1. Swapped "Go HIGHER" and "Go LOWER" messages in check_guess.
      2. Changed Hard difficulty range from 1-50 to 1-200.
      3. Removed the if/else that converted secret to string on 
         even attempts.
      4. Removed the scoring logic that added points for wrong guesses.
      5. Fixed new_game button to use difficulty range instead of 
         hardcoded 1-100.
      6. Refactored all 4 functions into logic_utils.py.

## 📸 Demo Walkthrough

1. User opens the game and selects Normal difficulty (range 1-100)
2. User types a guess of 40 and clicks Submit Guess
3. Game returns "Go Higher!" meaning the secret is above 40
4. User types 70 and clicks Submit Guess
5. Game returns "Go Lower!" meaning the secret is below 70
6. User types 55 and clicks Submit Guess
7. Game returns "Correct!" with balloons and shows final score
8. Score decreases by 5 points for each wrong guess made

## 🧪 Test Results

```
(.venv) PS C:\Users\vinny\Vincent-ai110-module1show-gameglitchinvestigator-starter> python -m pytest
==================================== test session starts ====================================
platform win32 -- Python 3.11.9, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\vinny\Vincent-ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.14.0
collected 9 items

tests\test_game_logic.py .........                                                     [100%]

9 passed in 0.04s
```
## 🚀 Stretch Features

### ✅ Advanced Edge-Case Testing 
Added 5 edge case pytest tests targeting:
- Empty string input → returns "Enter a guess." error
- Non-numeric input (e.g. "abc") → returns "That is not a number." error
- Negative numbers (e.g. "-5") → parses correctly as -5
- Decimal input (e.g. "42.7") → converts correctly to 42
- None input → returns "Enter a guess." error

All 9 tests pass successfully as shown in the Test Results section above.

### ✅ Professional Documentation and Style 
Added professional PEP 257 docstrings to all 4 functions in 
`logic_utils.py`:
- `get_range_for_difficulty` — documents difficulty parameter and 
  return tuple
- `parse_guess` — documents three-part return tuple with examples
- `check_guess` — documents guess/secret parameters and outcomes
- `update_score` — documents scoring rules and attempt-based logic

All prompts and changes are documented in `ai_interactions.md`.