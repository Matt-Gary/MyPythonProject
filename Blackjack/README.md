# BlackJack Game
This is a simple implementation of the classic game Blackjack using Python. The game is played in the terminal.
## How to play
The goal of Blackjack is to beat the dealer's hand without going over 21.

At the beginning of the game, the player is dealt two cards and the dealer is dealt one card face up and one card face down.

The player can then choose to "hit" (take another card) or "stand" (keep their current hand).

The player can continue to hit until they either reach 21 ("Blackjack"), decide to stand, or go over 21 ("bust").

Once the player has completed their turn, the dealer will reveal their face down card and hit until their hand totals 17 or more.

The winner is determined by comparing the player's and dealer's final hands. If the player's hand is closer to 21 than the dealer's hand without going over 21, the player wins. If the dealer's hand is closer to 21, the dealer wins. If there is a tie, the game ends in a draw.
## How to run
This program is run in the terminal using Python. To run the game, simply run the file blackjack.py.
```
python blackjack.py
```
You will then be prompted to play a game of Blackjack. Type 'y' to start a game or 'n' to quit.

During the game, follow the prompts to hit or stand. Once the game is over, you will be prompted to play again or quit.
