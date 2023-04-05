import json
import pyperclip
from tkinter import Tk, Canvas, PhotoImage, Label, Entry, messagebox, END
from tkmacosx import Button
from password_generator import generate_password

FONT = ("Arial", 20)
GRID_PADDING_Y = (0, 10)
DEFAULT_EMAIL = "example@github.com"
OUTPUT_FILEPATH = "data.json"

# ---------------------------- HELPER METHODS ------------------------------- #


def clear_inputs(*inputs):
    for i in inputs:
        i.delete(0, END)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def get_password():
    global password_entry
    pw = generate_password()
    password_entry.insert(0, pw)
    pyperclip.copy(pw)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    global website_entry, email_entry, password_entry
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if not website or not email or not password:
        messagebox.showwarning(
            title="Oops", message="Don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(
            title=website, message=f"These are the details entered:\n Email:{email}\n Password: {password}\n Is it ok to save?")

        if is_ok:
            try:
                with open(OUTPUT_FILEPATH, mode="r") as save_file:
                    save_data = json.load(save_file)
            except FileNotFoundError:
                with open(OUTPUT_FILEPATH, mode="w") as save_file:
                    json.dump(new_data, save_file, indent=4)
            except json.JSONDecodeError:
                with open(OUTPUT_FILEPATH, mode="w") as save_file:
                    json.dump(new_data, save_file, indent=4)
            else:
                save_data.update(new_data)
                with open(OUTPUT_FILEPATH, mode="w") as save_file:
                    json.dump(save_data, save_file, indent=4)
            finally:
                clear_inputs(website_entry, password_entry)

# ---------------------------- SEARCH PASSWORD ------------------------------- #


def search_website():
    global website_entry
    keyword = website_entry.get()
    if keyword:
        try:
            with open(OUTPUT_FILEPATH, mode="r") as save_file:
                save_data = json.load(save_file)
        except FileNotFoundError:
            messagebox.showinfo(message="Save file does not exist.")
        except json.JSONDecodeError:
            messagebox.showinfo(message="Save file is empty.")
        else:

            result = save_data.get(keyword)
            if result:
                messagebox.showinfo(
                    message=f"Email: {result['email']} \n Password: {result['password']}")
            else:
                messagebox.showinfo(
                    message=f"Sorry, {keyword} was not found in your saved data.")
    else:
        messagebox.showwarning(message="Website cannot be empty.")


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
website_entry.grid(row=1, column=1, sticky="ew")
website_entry.focus()

search_btn = Button(text="Search", command=search_website)
search_btn.grid(row=1, column=2, sticky="ew")

email_label = Label(text="Email:", anchor="e", font=FONT)
email_label.grid(row=2, column=0, pady=GRID_PADDING_Y)

email_entry = Entry()
email_entry.grid(row=2, column=1, columnspan=2, sticky="ew")
email_entry.insert(0, DEFAULT_EMAIL)

password_label = Label(text="Password:", anchor="e", font=FONT)
password_label.grid(row=3, column=0, pady=GRID_PADDING_Y)

password_entry = Entry()
password_entry.grid(row=3, column=1, sticky="ew")

password_btn = Button(text="Generate Password", command=get_password)
password_btn.grid(row=3, column=2, sticky="ew")

add_btn = Button(text="Add", command=save_password)
add_btn.grid(row=4, column=1, columnspan=2, sticky="ew")

window.mainloop()
