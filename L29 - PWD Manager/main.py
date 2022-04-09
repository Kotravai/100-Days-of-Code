from tkinter import *
from tkinter import messagebox
import pyperclip
import random
import json

FONT = ("courier", 24, "bold")
MAIL = "something@somemail.com"
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    password_letter = [random.choice(LETTERS) for _ in range(random.randint(6, 8))]
    password_numbers = [random.choice(NUMBERS) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(SYMBOLS) for _ in range(random.randint(2, 4))]

    password_list = password_letter + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    pwd_gen.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def password_adder():
    a = website_input.get()
    b = email_input.get()
    c = pwd_gen.get()
    new_data = {a: {"email": b, "password": c}}

    if len(str(a)) != 0 and len(str(c)) != 0:
        # is_ok = messagebox.askokcancel(title=a,message=f"These are the details entered:\n "
        #                                                f"Username: {a}\n Password: {b}\n Is it ok to save?")
        # if is_ok:
        try:
            with open("WordManager.json", "r") as file:
                data = json.load(file) # read the old file
                 # Add new entry to old file data
        except FileNotFoundError:
            with open("WordManager.json", "w") as file:
                json.dump(new_data, file, indent=4) # dump the entire thing to the existing file
        else:
            data.update(new_data)
            with open("WordManager.json", "w") as file:
                json.dump(data, file, indent=4) # dump the entire thing to the existing file
        finally:
            website_input.delete(0, END)
            pwd_gen.delete(0, END)
            if b != MAIL:
                email_input.delete(0, len(b))
                email_input.insert(0, MAIL)
            website_input.focus()

    #         messagebox.showinfo(title="Yaay!!", message="Password Saved! ")
    # else:
    #     messagebox.showwarning(title="Warning", message="Invalid Entry")

# --------------------------PASSWORD SEARCHER---------------------------#


def find_password():
    website = website_input.get()
    try:
        with open("WordManager.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Index", message="Data file does not exist")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="The Password", message=f"Email: {email} \n Password: {password}")
        else:
            messagebox.showinfo(title="key error", message="Password not found in database")
    finally:
        website_input.delete(0, END)
        website_input.focus()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.minsize(400, 400)
window.config(bg="white")
window.config(pady=40, padx=40)

canvas = Canvas(bg="white", width=200, height=200, highlightbackground="white")
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website: ", bg="white", fg="black")
website_label.config(pady=10, padx=10, anchor="center")
website_label.grid(row=1, column=0, sticky='ew')

website_input = Entry(width=10)
website_input.config(bg="white", fg="black", highlightbackground="grey")
website_input.focus()
website_input.grid(row=1, column=1, sticky='ew')

search_button = Button(text="Search", highlightbackground="white", command=find_password)
search_button.config(fg='black', width=15, bg='grey')
search_button.grid(row=1, column=2)

email_label = Label(text="E-Mail/Username: ", bg="white", fg="black", anchor='center')
email_label.config(pady=10, padx=10)
email_label.grid(row=2, column=0, sticky='ew')

email_input = Entry(width=40)
email_input.config(bg="white", fg="black", highlightbackground="grey")
email_input.insert(0, MAIL)
email_input.grid(row=2, columnspan=2, column=1, sticky='ew')

pwd_label = Label(text="Password: ", bg="white", fg="black")
pwd_label.config(pady=10, padx=10)
pwd_label.grid(row=3, column=0, sticky='ew')

pwd_gen = Entry(width=10)
pwd_gen.config(bg="white", fg="black", highlightbackground="grey")
pwd_gen.grid(row=3, column=1, sticky='ew')

gen_button = Button(text="Generate", highlightbackground="white", command=password_generator)
gen_button.config(fg='black', width=15, bg='grey')
gen_button.grid(row=3, column=2)

add_button = Button(text="Add", highlightbackground="white", command=password_adder)
add_button.config(fg='black', width=40, bg='grey')
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
