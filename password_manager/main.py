from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
    


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    
    password_entry.delete(0, END)
    password_entry.insert(0, "".join(password_list))
    pyperclip.copy("".join(password_list))

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    new_data = {
        website_entry.get(): {
            "email": email_entry.get(),
            "password": password_entry.get(),
        }
    }
    if len(website_entry.get()) == 0 or len(email_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("passwords.json", "r") as file:
                #Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("passwords.json", "w") as file:
                #Saving updated data  
                json.dump(new_data, file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)
            
            with open("passwords.json", "w") as file:  
                #Saving updated data  
                json.dump(data, file, indent=4)
        finally: 
            website_entry.delete(0, END)
            password_entry.delete(0, END)
        
    

# ---------------------------- UI SETUP ------------------------------- #
#Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.resizable(False, False)

#Canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1,row=0)

#Labels
website_label = Label(text="Website:")
website_label.grid(column=0,row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0,row=2)
password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

#Entries
website_entry = Entry(width=32)
website_entry.grid(column=1,row=1)
website_entry.focus()
email_entry = Entry(width=50)
email_entry.grid(column=1,row=2, columnspan=2)
email_entry.insert(0, "example@mail.com")
password_entry = Entry(width=32)
password_entry.grid(column=1,row=3)

#Button
search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2,row=1)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2,row=3)

add_button = Button(text="Add", width=42, command=save)
add_button.grid(column=1,row=4, columnspan=2)


window.mainloop()