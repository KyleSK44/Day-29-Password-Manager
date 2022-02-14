from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

lock_img = PhotoImage(file="lock.gif")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 112, image=lock_img)
canvas.grid(column=1, row=0)

#22323
window.mainloop()
