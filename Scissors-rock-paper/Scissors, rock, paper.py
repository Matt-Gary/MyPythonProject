# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 17:55:46 2023

@author: mgarc
"""

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper, and 2 for Scissors\n"))
images = [rock, paper, scissors]
if player_choice >= 3 or player_choice < 0:
  print("You choose wrong number, you lose")
else: 
  print(images[player_choice])
  
  pc_random_choice = random.randint(0,2)
  print("Computer chose:\n")
  print(images[pc_random_choice])
  
  if player_choice == pc_random_choice:
    print("It's a draw")
  elif player_choice == 0 and pc_random_choice == 2:
    print("You win")
  elif pc_random_choice == 0 and player_choice == 2:
    print("You win")
  elif pc_random_choice > player_choice:
    print("You lose")
  elif player_choice > pc_random_choice:
      print("You win")