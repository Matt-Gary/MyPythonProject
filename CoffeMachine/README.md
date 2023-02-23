# Coffee Machine Simulator
This program simulates a coffee machine that allows users to purchase different types of coffee drinks. The coffee machine has a limited amount of resources (water, milk, coffee) and can only make drinks if it has enough resources. The program keeps track of the amount of money made from coffee sales.
## Menu
The coffee machine offers three different types of drinks:

- Espresso
- Latte
- Cappuccino
Each drink has a set of ingredients and a cost associated with it.
## Resources
The coffee machine has a limited amount of resources available to make drinks:

- Water (in milliliters)
- Milk (in milliliters)
- Coffee (in grams)
## Funcionality
The program allows the user to select a drink from the menu, insert coins to pay for the drink, and then dispense the drink if there are enough resources and the payment is successful. The program also allows the user to check the current resource levels and the amount of money made from coffee sales.

The program will terminate if the user enters "off" or if there are not enough resources to make a selected drink.
## Implementation
The program is implemented in Python and uses a dictionary to store the menu of drinks and their ingredients/cost. The program keeps track of the amount of money made from coffee sales using a global variable. The program also uses a dictionary to keep track of the current resource levels.

The program is implemented using a while loop to allow the user to make multiple selections without restarting the program. The user is prompted to enter their selection, and the program checks if there are enough resources to make the selected drink. If there are enough resources, the user is prompted to insert coins to pay for the drink. If the payment is successful, the program dispenses the drink and updates the resource levels and profit. If the user selects "report", the program prints out the current resource levels and the amount of money made from coffee sales. The program terminates if the user selects "off" or if there are not enough resources to make a selected drink.
