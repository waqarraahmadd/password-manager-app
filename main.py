from tkinter import *
from tkinter import messagebox
import random
import pyperclip

FONT = "ariel"
FONT_SIZE = 13


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_input.delete(0,"end")
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for num in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for sym in range(random.randint(2, 4))]

    password_list = password_symbols + password_numbers + password_letters
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = username_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showerror(title="ERROR", message="You cannot have an empty website or password")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n\nEmail: {email}"
                                                              f"\nPassword: {password}"
                                                              f"\nIs it okay to save?")
        if is_ok:
            with open("passwords.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
                password_input.delete(0, "end")
                website_input.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(pady=50, padx=50)
window.title("Password Manager")

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(135, 100, image=logo)
canvas.grid(row=0, column=1)

# labels
website_label = Label(text="Website:", font=(FONT, FONT_SIZE))
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username:", font=(FONT, FONT_SIZE))
username_label.grid(row=2, column=0)

password_label = Label(text="Password:", font=(FONT, FONT_SIZE))
password_label.grid(row=3, column=0)

# Entries/input
website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

username_input = Entry(width=35)
username_input.grid(row=2, column=1, columnspan=2)
username_input.insert(1, "waqar.ahmad@gmail.com")

password_input = Entry(width=21)
password_input.grid(row=3, column=1)

# Buttons
generate_button = Button(text="Generate Password", font=(FONT, FONT_SIZE), command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", font=(FONT, FONT_SIZE), width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
