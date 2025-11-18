import random

# List of words (fruits)
word_list = ["apple", "banana", "cherry", "orange", "grape"]

# Pick a random word
word = random.choice(word_list)

# Set to store guessed letters
guessed_letters = set()

# Number of incorrect attempts allowed
attempts = 10

# Welcome message
print("Welcome to the Word Guessing Game!")

# Hint for the user
print("Hint: The word is a type of fruit!")

# Game loop
while attempts > 0:
    # Show current progress
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    print("Word: ", " ".join(display))

    # Check if all letters have been guessed
    if set(word) == guessed_letters:
        print(f"Congratulations! You guessed the word '{word}'!")
        break

    # Ask for user input
    guess = input("Guess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    # Check guess
    if guess in word:
        print(f"Good job! '{guess}' is in the word.")
        guessed_letters.add(guess)
    else:
        attempts -= 1
        print(f"Wrong guess. You have {attempts} attempts left.")

# If attempts run out
if attempts == 0:
    print(f"Game Over! Better luck next time... The word was '{word}'. Try again later.")
