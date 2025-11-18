import random

# List of words (fruits)
word_list = ["apple", "banana", "cherry", "orange", "grape"]

MAX_ATTEMPTS = 6

# Function to display word progress (used for testing)
def display_word_progress(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

# Function to play the game
def play_game():
    print("Welcome to the Word Guessing Game!")
    print("Hint: The word is a type of fruit!\n")

    while True:
        word = random.choice(word_list)
        guessed_letters = set()
        attempts = MAX_ATTEMPTS
        print("New word! Try to guess it.")

        while attempts > 0:
            display = display_word_progress(word, guessed_letters)
            print("Word: ", display)

            if set(word) == guessed_letters:
                print(f"Congratulations! You guessed the word '{word}'!\n")
                break

            guess = input("Guess a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
                continue

            if guess in word:
                print(f"Good job! '{guess}' is in the word.")
                guessed_letters.add(guess)
            else:
                attempts -= 1
                print(f"Wrong guess. You have {attempts} attempts left.")

        if attempts == 0:
            print(f"Game Over! The word was '{word}'.")

        while True:
            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again == "y":
                print("\nStarting a new word...\n")
                break
            elif play_again == "n":
                print("Thanks for playing! Goodbye!")
                return
            else:
                print("Please enter 'y' for yes or 'n' for no.")

# Only run the game if this file is executed directly
if __name__ == "__main__":
    play_game()
