from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    pass
# ---------------------------- SAVE PASSWORD ------------------------------- #


def add():
    with open('passwords.txt','a') as pfile:
        pfile.write(f"{web_entry.get()} | {email_entry.get()} | {password_entry.get()} \n")
    web_entry.delete(0,END)
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
