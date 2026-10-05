# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
While there is a note that said "Press Enter to Apply", nothing happens when I do, so I have to manually used the "Submit answer" button. It seems to me that Going Lower/Going Higher is returned at random because I entered the same input several times in the same game and was told to go lower AND go higher. Out of range numbers were accepted no matter what mode I play in, and it looks like the range is flipped between Medium and Hard. 

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
The Enter button does not work, I have to submit answer manually. 
Going Lower/Going Higher can both appear for the same number in the same game.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input              | Expected Behavior             | Actual Behavior | Console Output / Error |
|--------------------|-------------------------------|-----------------|------------------------|
|55                  | go HIGHER                     | go LOWER        | app.py - check_guess|
|Pressing Enter      | show "go HIGHER" or "go LOWER | Nothing happen  | app.py |
|Pressing "New Game" | start a New Game              | Nothing happen  | app.py  |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I'm using Claude for this project

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
