import random

# List of words (fruits)
word_list = ["apple", "banana", "cherry", "orange", "grape"]

# Maximum number of incorrect attempts per word
MAX_ATTEMPTS = 10

print("Welcome to the Word Guessing Game!")
print("Hint: The word is a type of fruit!\n")

# Main loop for replaying the game
while True:
    # Pick a random word
    word = random.choice(word_list)
    guessed_letters = set()
    attempts = MAX_ATTEMPTS

    print("New word! Try to guess it.")

    # Word guessing loop
    while attempts > 0:
        # Show current progress
        display = "".join([letter if letter in guessed_letters else "_" for letter in word])
        print("Word: ", " ".join(display))

        # Check if the word has been guessed
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
        print(f"Game Over! Better luck next time... The word was '{word}'. Try again!")

    # Ask if the user wants to play again
    while True:
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == "y":
            print("\nStarting a new word...\n")
            break  # Restart outer loop
        elif play_again == "n":
            print("Thanks for playing! Goodbye!")
            exit()
        else:
            print("Please enter 'y' for yes or 'n' for no.")
