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

- [x] Describe the game's purpose.
Guess a number between the given range with a certain amount of attempt. If the number guessed is less or higher than the given random secret, a message will tell you to either guess another higher or lower number. There are three difficulties, with three different number range and attempt limits.

- [x] Detail which bugs you found.
The return message of each guess seemed to be random, and the same guess can both return "go LOWER" and "go HIGHER" in the same game. This happened because user input was changed into string, and then get compare to a string, which comparing their unicode which cause the randomness in logic. 
The range for each "new game" reset is hardcoded, thus no matter what difficult the player picks, it will always be from 1 to 100.
The difficulty range was switch between Normal and Hard.
For some reasons, points were being calculated base on the fact if the attempt was odd or even. 

- [x] Explain what fixes you applied.
1) I remove any conversion of user input into string, so that all comparison is between int and int. 
2) st.session_state.secret = random.randint(1, 100) => st.session_state.secret = random.randint(low, high)
3) I switch their range manually
4) Simplified point calculation to -5 for every attempt used.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess of 25
2. Game returns "go HIGHER"
3. User enters a guess of 35
4. Game returnS "go HIGHER"
5. User enters a guess of 45
6. Game returnS "You Won! The Secret was 45. The final score is 50."

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
