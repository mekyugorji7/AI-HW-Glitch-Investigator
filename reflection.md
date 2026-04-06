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

The secret number kept changing because of Streamlit's session_state functionality. Essentially, every time on every interaction, Streamlit reruns its session_state, which means anything that's outside of it is not protected and is able to be regenerated. Imagine every single time I press a button, I'm starting that script every single time. The session_state script is basically the memory of the system to keep track of what I've changed while I've been in the system. If it's not within session_state, then it's going to forget because it's going to wipe out everything. Imagine I'm cleaning a desk, but I put something in my pocket. That's my session_state. If it's not in my pocket, then it's not going to be there, and my session_state meaning is gone because it's missing. That's basically how it works, and the change I made was making sure that it stayed stable between guesses instead of changing unexpectedly. I reset the secret only inside the New Game Flow, so that made the game behavior way more predictable and corrected the issue.
---

## 5. Looking ahead: your developer habits

I really like AI's ability to create new edge cases. I think edge cases are one of the most important things when developing new systems, because you want to make sure your system survives no matter what data is being passed through it. With AI, it is able to create more cases than you can think of. I also think it's really beneficial just in terms of looking over your entire system, ensuring you have correct syntax, you are approaching the problem correctly, and it is able to provide you feedback. You basically have a personal system every single time you code. I think that's really good and really beneficial, especially within this field of software development.