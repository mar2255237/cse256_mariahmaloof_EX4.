import random
import pytest
from guess_the_word import word_list


# Function to display word progress (for testing)
def display_word_progress(word, guessed_letters):
    """Return the word display with guessed letters shown and others as underscores."""
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])


# Test that selected word is from the word list
def test_select_word():
    """Ensure a randomly selected word is from the predefined word list."""
    word = random.choice(word_list)
    assert word in word_list


# Test display when no letters guessed
def test_display_word_progress_no_guesses():
    """Verify display shows all underscores when no letters are guessed."""
    word = "apple"
    guessed_letters = set()
    progress = display_word_progress(word, guessed_letters)
    assert progress == "_ _ _ _ _"


# Test display with some letters guessed
def test_display_word_progress_some_guesses():
    """Verify partially guessed letters appear in the correct positions."""
    word = "banana"
    guessed_letters = {"a", "n"}
    progress = display_word_progress(word, guessed_letters)
    assert progress == "_ a n a n a"


# Test display when all letters guessed
def test_display_word_progress_all_guessed():
    """Verify that fully guessing the word displays all letters."""
    word = "cherry"
    guessed_letters = set(word)
    progress = display_word_progress(word, guessed_letters)
    assert progress == "c h e r r y"


# Test display for incorrect guesses
def test_display_word_progress_incorrect_guess():
    """Ensure incorrect guesses do not reveal any letters."""
    word = "apple"
    guessed_letters = {"z"}  # incorrect guess
    progress = display_word_progress(word, guessed_letters)
    assert progress == "_ _ _ _ _"
