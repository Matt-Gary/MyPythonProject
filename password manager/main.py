from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def password_generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    new_data = {
        website_entry.get(): {
            "email": email_entry.get(),
            "password": password_entry.get(),
        }
    }
    if website_entry.get() == "":
        messagebox.showinfo(title="Ops", message= "You left website field empty")
    elif email_entry.get() == "":
        messagebox.showinfo(title="Ops", message= "You left email field empty")
    elif password_entry.get() == "":
        messagebox.showinfo(title="Ops", message= "You left password field empty")
    else:
        is_ok = messagebox.askokcancel(title=website_entry.get(),
                                       message=f"These are the details entered \nWebsite: {website_entry.get()}\n"
                                               f"Email: {email_entry.get()}\n"
                                               f"Password: {password_entry.get()} ")
        if is_ok:
            try:
                with open('data.json', 'r') as data_file:
                    data = json.load(data_file)
            except(FileNotFoundError, json.decoder.JSONDecodeError):
                with open('data.json', 'w') as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open('data.json', 'w') as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                messagebox.showinfo(title="HURAAAA", message="New password saved")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
    #delete entry

# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    web = website_entry.get()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except:
        messagebox.showinfo(title="Not Found", message="No Data File Found")
    else:
        if web in data:
            senha = data[web]["password"]
            email = data[web]["email"]
            messagebox.showinfo(title=web, message=f"EMAIL: {email}\nPassword: {senha}")
            pyperclip.copy(senha)
            messagebox.showinfo(title="Info", message = "Password already copied!")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {web} exist")




#--------------------------- UI SETUP -------------------------------
window = Tk()
window.title = "Password Manager"
window.config(padx=50, pady=50)



canvas = Canvas(height=200, width=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)
#Label
website = Label(text="Website:")
website.grid(column=0, row=1)
email = Label(text="Email/Username:")
email.grid(column=0, row=2)
password = Label(text="Password:")
password.grid(column=0, row=3)
#Entries
website_entry = Entry(width=30)
website_entry.grid(column=1, row=1, sticky="w") #align to the left
website_entry.focus() #cursor appear in the website entry
email_entry = Entry(width=52)
email_entry.grid(column=1, row=2, columnspan=2, sticky="w")
#adding starting value to the entry
email_entry.insert(0, "@gmail.com") #END- constant that represent last character
password_entry = Entry(width=30)
password_entry.grid(column=1, row=3, sticky="w")
#Buttons
generate_button = Button(text="Generate Password", command=password_generate)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2)
search_button = Button(text="Search", width= 15, command=find_password)
search_button.grid(column=2, row=1, sticky="w")

window.mainloop()
