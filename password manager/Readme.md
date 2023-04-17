# Password Manager
This is a simple password manager program that uses Tkinter, a standard Python library for creating graphical user interfaces (GUI). The program allows users to generate strong passwords, save them along with website and email/username information, and retrieve them when needed. The program uses JSON file to store the password data locally.
# Features
## Password Generator
The program generates strong passwords consisting of lowercase letters, uppercase letters, numbers, and symbols. The length of the password and the number of symbols and numbers can be customized.
## Save Password
Users can save the generated password along with the website and email/username information. The data is stored in a JSON file with the website as the key and the email/username and password as values.
## Find Password
Users can search for a saved password by entering the website name. If the website is found in the JSON file, the program displays the email/username and password associated with the website and copies the password to the clipboard
## User Interface (UI)
The program has a simple and user-friendly UI created using Tkinter. It includes labels, text entries, buttons, and an image.
## Usage
1. Run the program in a Python environment.
2. Enter the website, email/username, and password information.
3. Click on the "Generate Password" button to generate a strong password.
4. Click on the "Add" button to save the password.
5. To search for a saved password, enter the website name in the website entry and click on the "Search" button.
Note: The generated passwords are automatically copied to the clipboard for ease of use.
## Dependencies
The program uses the following Python libraries:

* Tkinter: for creating the graphical user interface (GUI).
* Pyperclip: for copying passwords to the clipboard.
* JSON: for storing password data in a JSON file.
