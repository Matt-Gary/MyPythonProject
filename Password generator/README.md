# Password Generator
This is a simple password generator that allows the user to create a custom password by choosing the number of letters, symbols and numbers that will be included in the password.
## How to use
1. Run the script.
2. Enter the number of letters you want in your password when prompted.
3. Enter the number of symbols you want in your password when prompted.
4. Enter the number of numbers you want in your password when prompted.
5. The script will generate a new password and display it on the screen.
## How it works
The script uses a list of letters, numbers, and symbols to generate a random password. It first asks the user how many letters, symbols and numbers they would like in their password.

Then, it creates an empty list called *password_list*, and loops through the number of letters, symbols, and numbers that the user wants in their password. For each iteration, it uses the **random.choice()** function to select a random character from the corresponding list (letters, symbols, or numbers) and adds it to the *password_list*.

Once all the characters have been added to the *password_list*, the script uses the **random.shuffle()** function to shuffle the characters in the list to make the password more random.

Finally, the script creates an empty string called password and loops through each character in *password_list*, adding it to password one by one. Once all the characters have been added, it prints the final password to the screen.
