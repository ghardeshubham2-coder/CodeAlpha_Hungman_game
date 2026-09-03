import random

# List of 5 predefined words
words = ["python", "computer", "program", "database", "keyboard"]

# Randomly select a word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum incorrect guesses
max_wrong_guesses = 6
wrong_guesses = 0

# Display hidden word
display_word = ["_"] * len(word)

print("================================")
print("       🎮 HANGMAN GAME")
print("================================")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.")
print()

# Main game loop
while wrong_guesses < max_wrong_guesses:

    # Display current word
    print("Word:", " ".join(display_word))

    # Display guessed letters
    print("Guessed letters:", " ".join(guessed_letters))
    print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

    # Check if the word is completely guessed
    if "_" not in display_word:
        print("\n🎉 Congratulations!")
        print("You guessed the word:", word)
        break

    # Take user input
    guess = input("\nEnter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter only one letter.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    # Add letter to guessed list
    guessed_letters.append(guess)

    # Check whether letter is in the word
    if guess in word:

        print("✅ Correct guess!")

        # Reveal the guessed letter
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess

    else:
        wrong_guesses += 1
        print("❌ Wrong guess!")

# If player reaches maximum wrong guesses
if wrong_guesses == max_wrong_guesses:
    print("\n💀 Game Over!")
    print("The word was:", word)

print("\nThanks for playing! 🎮")