# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

## 1. What was broken when you started?

When I first ran the game it looked normal but immediately showed wrong behavior 
when I started guessing. The hints were completely backwards — telling me to go 
lower when my guess was actually too low. The difficulty settings also did not 
make sense, with Hard being easier than Normal mode.

**Bug Reproduction Log**

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess of 20 (secret was higher) | Hint says "Go Higher!" | Hint said "Go Lower!" | none |
| Switch to Hard difficulty | Range should be harder than Normal (1-100) | Range was 1-50, easier than Normal | none |
| Guess on 2nd attempt (even attempt) | Consistent hint based on guess | Hint changes unexpectedly due to secret switching type | none |
| Wrong guess on even attempt | Score should decrease | Score increased by 5 points | none |

---

## 2. How did you use AI as a teammate?

## 2. How did you use AI as a teammate?

I used Claude (claude.ai) as my AI assistant on this project.

**Correct AI suggestion:**
I asked Claude to help me understand why the hints were backwards 
in the check_guess function. Claude correctly identified that the 
messages "Go HIGHER" and "Go LOWER" were swapped and suggested 
switching them around. I verified this by playing the game and 
confirming the hints now matched the actual guess results.

**Incorrect/Misleading AI suggestion:**
Claude initially suggested that Hard difficulty range should be 
1-200 but did not notice that the new_game button was hardcoded 
to always use 1-100 regardless of difficulty. I had to find and 
fix that separately by checking the new_game button code in app.py.

---

## 3. Debugging and testing your fixes

I decided a bug was really fixed when two things were true: the 
game behaved correctly when I played it manually, and the pytest 
tests passed without errors.

For testing, I ran `python -m pytest` which collected 4 tests from 
`tests/test_game_logic.py`. All 4 passed, including a new test I 
added called `test_hints_not_backwards` which specifically checks 
that guessing too high returns "Go LOWER" and guessing too low 
returns "Go HIGHER". This confirmed the backwards hints bug was 
fully fixed.

Claude helped me understand why the existing starter tests were 
failing — they were comparing the full return value of check_guess 
(which returns two values) against just one string. Claude suggested 
unpacking the result into `outcome, message` before asserting, 
which fixed the tests.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
