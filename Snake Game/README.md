# Snake Game
This is a simple implementation of the classic Snake game using the turtle module in Python. The objective of the game is to move the snake around the screen, eating turtles to grow in size while avoiding colliding with the walls or the snake's own body.
## Game Controls
The game is controlled using the arrow keys:

- Up arrow: move the snake upwards
- Down arrow: move the snake downwards
- Left arrow: move the snake to the left
- Right arrow: move the snake to the right
## Features
- Snake movement
- Food generation
- Snake growth upon food consumption
- Wall collision detection
- Self-collision detection
- Score tracking
## Modules
The game is built using three modules:

**newsnake.py**: contains the *Snake class* that defines the behavior and properties of the snake
**food.py**: contains the *Food class* that defines the behavior and properties of the food
**scoreboard.py**: contains the *Scoreboard class* that tracks the score and displays it on the screen
## Dependencies
The game requires the **turtle module**, which comes pre-installed with Python.
## How to Play
To play the game, simply run the **snake_game.py** script. Use the arrow keys to move the snake around the screen and eat the food. If the snake collides with the walls or its own body, the game will reset and the score will be set back to zero. The game can be exited by closing the window or by pressing the **Esc** key.
