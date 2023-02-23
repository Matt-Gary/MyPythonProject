# Hangman Game
This is a simple implementation of the Hangman game. The player has to guess a secret word by suggesting letters. The game starts with an empty word, and for each correct guess, the corresponding letter(s) are revealed. If the player guesses the word correctly before running out of lives, they win; otherwise, they lose.
# How to Play
1. The game randomly selects a word from a predefined list.
2. The player guesses a letter by typing it on the keyboard.
3. If the letter is in the word, all instances of that letter are revealed.
4. If the letter is not in the word, the player loses a life.
5. The game continues until the player has either correctly guessed the word or has run out of lives.
# Code Explanation
The code consists of two imported modules: **hangman_art** and **hangman_words**.

The **hangman_art** module contains the ASCII art of the Hangman for each stage of the game, and the **hangman_words** module contains a predefined list of words for the game.

The game starts by selecting a random word from the **hangman_words** list. It then creates an empty list called display, which will be used to display the word as the player guesses each letter.

The game then enters a loop that continues until the end of the game is reached. In each iteration, the player is prompted to guess a letter. If the letter is already guessed, the player is notified, and the loop continues. If the letter is in the word, all instances of that letter in the word are revealed in the **display list**. If the letter is not in the word, the player loses a life, and the game continues.

If the player guesses the word correctly before running out of lives, the player wins. If the player runs out of lives before guessing the word, the player loses.
# Usage
To play the Hangman game, run the code in a Python environment. The game will run in the console, and the player can enter letters to make guesses.
