# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

Game bugs:
- The hint was wrong, I guessed 1 and told me "Go lower", 8 was the correct choice
- Attempts not updating/reloading correctly after each guess and new game
- Game not being playable after winning and pressing new game

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I utilized the GPT 5.3 Codex for this project. One example of how I used this AI was with the tests. It created its own test file when I already had one, so I had to make sure I deleted it and that tests were being written accurately. Also, since it's Python, the file path for the tests and pytest needed to be corrected. I manualy corrected that after the AI gave me the incorrect suggestion. They system also gave me the correct suggestion that the hint was backwards, so that's how I was able to fix the first bug I found.

The other bug I found was that the app was not updating after each attempt. For example, after I would do one attempt, the attempt would stay frozen, so it would just lag, and then upon a new game the attempts also didn't update. I had to fix that and collaborate with it AI in order to fix it, and it correctly found the issue within the @app.py file.

---

## 3. Debugging and testing your fixes

I decided a bug was really fixed only after I could reproduce the old behavior first and then confirm it no longer happened in the app. I manually tested by winning or losing a round and pressing **New Game**, then checking that attempts reset, status went back to playing, and the game accepted guesses again. I also ran `pytest -q` and used the regression test for the hint-direction bug (`check_guess(1, 8)` should return **Too Low** with a **HIGHER** hint), which confirmed the logic now points the player in the correct direction. AI helped me design that regression test and identify where to place it, but I still had to verify imports, test file location, and assertion format myself.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
