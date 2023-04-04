from tkinter import Tk, Label, Entry, Button

window = Tk()
window.title("Convert Miles to KM")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

miles_input = Entry(width=10)
miles_input.grid(row=0, column=1)

miles_unit_label = Label(text="miles")
miles_unit_label.grid(row=0, column=2)

equal_label = Label(text="is equal to")
equal_label.grid(row=1, column=0)

km_value_label = Label(text="0")
km_value_label.grid(row=1, column=1)

km_unit_label = Label(text="km")
km_unit_label.grid(row=1, column=2)


def convert_miles():
    global miles_input
    miles = float(miles_input.get())
    km = round(miles * 1.609344, 3)
    km_value_label.config(text=f"{str(km)}")


button = Button(text="Calculate", command=convert_miles)
button.grid(row=2, column=1)

window.mainloop()
