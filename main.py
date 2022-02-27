from tkinter import *
from tkinter import messagebox
import random, pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    random.shuffle(letters)
    random.shuffle(numbers)
    random.shuffle(symbols)
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list = [item for item in letters[0:nr_letters]]
    password_list.extend([item for item in numbers[0:nr_numbers]])
    password_list.extend([item for item in symbols[0:nr_symbols]])

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0,END)
    password_entry.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add():

    if len(password_entry.get()) == 0 or len(web_entry.get()) == 0 or len(email_entry.get()) == 0:
        messagebox.showerror(message=" One or more of the fields is blank")

    else:
        is_ok = messagebox.askokcancel(title=web_entry.get(),
                                       message=f"Data entered: \nEmail: {email_entry.get()} \nPassword: "
                                               f"{password_entry.get()} \nIs This Correct? ")
        if is_ok:
            with open('passwords.txt','a') as pfile:
                pfile.write(f"{web_entry.get()} | {email_entry.get()} | {password_entry.get()} \n")
            pyperclip.copy(password_entry.get())
            web_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()


window.title("Password Manager")
window.config(padx=50, pady=50)

lock_img = PhotoImage(file="lock.gif")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

lab1 = Label(text="Website:")
lab1.grid(column=0, row=1)

web_entry = Entry(width=52)
web_entry.grid(column=1, row=1, columnspan=2)

lab2 = Label(text="Email/Username:")
lab2.grid(column=0, row=2)

email_entry = Entry(width=52)
email_entry.insert(0, "bingo@gmail.com") #inserts text at the zeroth character
email_entry.grid(column=1, row=2, columnspan=2)

lab3 = Label(text="Password:")
lab3.grid(column=0, row=3)

password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)

password_button = Button(text="Generate Password", command=generate)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", command = add, width=44)
add_button.grid(column=1, row=4, columnspan=2)

#22323
window.mainloop()
