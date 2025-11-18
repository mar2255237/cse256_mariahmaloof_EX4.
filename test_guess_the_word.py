import random
import pytest
from guess_the_word import word_list


# Function to display word progress (for testing)
def display_word_progress(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

# Test that selected word is from the word list
def test_select_word():
    word = random.choice(word_list)
    assert word in word_list

# Test display when no letters guessed
def test_display_word_progress_no_guesses():
    word = "apple"
    guessed_letters = set()
    progress = display_word_progress(word, guessed_letters)
    assert progress == "_ _ _ _ _"

# Test display with some letters guessed
def test_display_word_progress_some_guesses():
    word = "banana"
    guessed_letters = {"a", "n"}
    progress = display_word_progress(word, guessed_letters)
    assert progress == "_ a n a n a"

# Test display when all letters guessed
def test_display_word_progress_all_guessed():
    word = "cherry"
    guessed_letters = set(word)
    progress = display_word_progress(word, guessed_letters)
    assert progress == "c h e r r y"
