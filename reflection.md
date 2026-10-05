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
In app.py, line 85, Claude let me know random.randit was first hardcoded a range from 1 to 100, so I should change it to random.randit (low, high) so it can match the difficulty the player selected. 
I told Claude to also add a boundary check for when the player enter the number, so I can verify both of these requirements by playing the game myself and not just rely fully on the pytest. 
So I would start a new game after every input, and enter a number outside of the difficult's range, which does behave as intended. 

- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
Claude told me that the logic behind attempt number limit and difficulty is not sound, that harder difficulty should have more attempts instead of the other way around. 
For me personally, if it is "Hard", it shouldn't just be bigger range, but also less chances so that the player has to be smart about each of their choices to minimize the range with each guess. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
A bug is really fixed when both pytest and manual testing passed, multiple times. 

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
One test I do manually is testing whether the attempt number increases if the guess is invalid (not a number or out of range). I just keep entering a few numbers out of range, and then guess the actually number. Then I open the develope debug log to see how my score is calculated (-5 for every wrong but valid guesses), and compare it against my actual valid attempt recored. 

Being out of range was not considered in the first version of the code, so mine actually paid attention to an undocumented requirements. 

- Did AI help you design or understand any tests? How?
My pytest was entirely written by Claude with clear naming convention that let me know exactly what each test is testing.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit reruns mean that the app runs its code again whenever a user interacts with something, like clicking a button or changing an input. 
Session state lets the app remember information between reruns, so it doesn't lose things like the user's input or selections.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
I would like to keep asking AI to write my test cases, at the same time, run the application and check it myself.

- What is one thing you would do differently next time you work with AI on a coding task?
With every change suggested by AI, I would ask it to explain the changes it comes up by itself before deciding if I should implement it or not. 

- In one or two sentences, describe how this project changed the way you think about AI generated code.
AI is a powerful partner in coding, especially with debugging and identify logical mistakes. However, I think AI is only good as a partner to help you write/fix code, and is not reliable at writing a fully functional application. 
