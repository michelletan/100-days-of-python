from tkinter import Tk, Canvas, PhotoImage, Label, Entry
from tkmacosx import Button

FONT = ("Arial", 20)
GRID_PADDING_Y = (0, 10)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    pass
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    pass


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("My Pass | Password Manager")
window.minsize(width=300, height=300)
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(250, 100, image=logo_img)
canvas.grid(row=0, column=0, columnspan=3, sticky="nesw")

website_label = Label(text="Website:",
                      anchor="e", font=FONT)
website_label.grid(row=1, column=0, pady=GRID_PADDING_Y)

website_entry = Entry()
website_entry.grid(row=1, column=1, columnspan=2, sticky="ew")

email_label = Label(text="Email:", anchor="e", font=FONT)
email_label.grid(row=2, column=0, pady=GRID_PADDING_Y)

email_entry = Entry()
email_entry.grid(row=2, column=1, columnspan=2, sticky="ew")

password_label = Label(text="Password:", anchor="e", font=FONT)
password_label.grid(row=3, column=0, pady=GRID_PADDING_Y)

password_entry = Entry()
password_entry.grid(row=3, column=1, sticky="ew")

password_btn = Button(text="Generate Password", command=generate_password)
password_btn.grid(row=3, column=2, sticky="ew")

add_btn = Button(text="Add", command=save_password)
add_btn.grid(row=4, column=1, columnspan=2, sticky="ew")

window.mainloop()
