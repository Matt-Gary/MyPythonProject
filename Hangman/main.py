import random
import hangman_art
import hangman_words
import os
clear = lambda: os.system('cls')

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

print(hangman_art.logo)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    if guess in display:
      print(f"You've already guessed '{guess}'!\n Try Again! ")
    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives -= 1
        print(f"The letter '{guess}' isn't in the word, you lose life!\nTry Again!")
        if lives == 0:
            end_of_game = True
            print(f"You lose. The word was {chosen_word}")
    
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
    
    print(hangman_art.stages[lives])
   
