# PingPong Classic Arcade Game
PingPong is a classic arcade game that simulates a table tennis game. It was first released by Atari in 1972 and quickly became a popular game in arcades around the world. The game is played with two players, each using a paddle to hit a ball back and forth across a table.
## Gameplay
The game consists of two paddles, one on the left and one on the right, and a ball. The objective is to hit the ball with the paddles, and make it go past the other player's paddle. Each time the ball goes past a player's paddle, the opponent gets a point. The player with the most points at the end of the game wins.
## Controls
Player 1 (Left Paddle):

Move up: 'w' key
Move down: 's' key
Player 2 (Right Paddle):

Move up: 'Up' arrow key
Move down: 'Down' arrow ke
## Installation
- Clone the repository
- Install the required modules: pip install -r requirements.txt
- Run the game: python main.py
## Code
This game is implemented in Python, using the Turtle module. The game consists of 3 classes:

**Paddle**: This class is responsible for the paddles in the game.

**Ball**: This class is responsible for the ball in the game.

**Scoreboard**: This class keeps track of the score in the game.
The Screen class is used to create the game screen, and the time module is used to control the speed of the ball.

The game loop is implemented using a while loop that runs until the game is over. In each iteration of the loop, the ball and paddles are moved and collisions are detected. If the ball goes past a paddle, the opponent gets a point. The game ends when one player reaches a certain number of points.
## Development
PingPong was one of the first arcade games ever made and was developed by Allan Alcorn at Atari. The game was based on the classic game of table tennis and was designed to be simple and easy to understand.

The game was programmed using the Pong Game Simulator, a custom software tool that Alcorn developed specifically for the game. The simulator allowed Alcorn to test the game on a television screen and make adjustments as needed.

The original version of PingPong used simple black-and-white graphics and was played on a small, monochrome monitor. Over time, the game was updated with color graphics and improved sound effects.
## Legacy
PingPong was a huge success and helped to launch the arcade game industry. The game was so popular that it spawned a number of imitators, including Breakout and Space Invaders.

Today, PingPong is considered a classic arcade game and is still played by fans all over the world. The game has been ported to a variety of platforms, including home consoles and mobile devices.
## Acknowledgments
This game was made with the help of the "100 Days of Code - The Complete Python Pro Bootcamp for 2021" course on Udemy.
