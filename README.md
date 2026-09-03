# CodeAlpha_Hungman_game

A simple **text-based Hangman Game** developed using Python. The player has to guess a randomly selected word by entering one letter at a time.

This project is beginner-friendly and demonstrates important Python programming concepts such as **lists, strings, loops, conditional statements, user input, and the random module**.

---

## 📌 Project Overview

The Hangman Game selects one word randomly from a predefined list of five words.

The player guesses the word by entering one letter at a time.

- ✅ Correct guesses reveal the letter.
- ❌ Incorrect guesses reduce the number of remaining attempts.
- ⚠️ A maximum of **6 incorrect guesses** is allowed.
- 🎉 The player wins if the complete word is guessed.
- 💀 The game ends if all 6 incorrect guesses are used.

---

## 🎯 Features

- 🎲 Random word selection
- 🔤 One-letter-at-a-time guessing
- ❤️ Maximum 6 incorrect guesses
- 👀 Displays the current progress of the word
- 📝 Keeps track of guessed letters
- ⚠️ Prevents duplicate guesses
- ❌ Validates user input
- 🎉 Win and game-over messages
- 💻 Simple console-based interface
- 🚫 No external files or APIs required

---

## 🛠️ Technologies Used

- **Python 3**
- `random` module
- Console / Terminal

---

## 🧠 Python Concepts Used

This project demonstrates the following concepts:

### 1. Lists
Used to store:
- Predefined words
- Guessed letters
- Hidden/revealed characters

### 2. Strings
Used for:
- Words
- User input
- Display messages

### 3. `random` Module
Used to randomly select a word from the list.

```python
word = random.choice(words)
