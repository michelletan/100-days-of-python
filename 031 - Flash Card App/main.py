from tkinter import Tk, Canvas, PhotoImage, Label
from tkmacosx import Button
from PIL import Image, ImageTk

BACKGROUND_COLOR = "#B1DDC6"
CARD_FRONT_COLOR = "#FFFFFF"
CARD_BACK_COLOR = "#88BAA7"
WINDOW_PADDING = 40
CARD_WIDTH = 600
CARD_HEIGHT = 400
BUTTON_SIZE = 60
BUTTON_OPTIONS = {
    "bg": BACKGROUND_COLOR,
    "activebackground": BACKGROUND_COLOR,
    "focusthickness": 0,
    "borderless": True
}
FONT_OPTIONS_TITLE = ("Arial", 25, "bold")
FONT_OPTIONS_SUBTITLE = ("Arial", 20, "bold")
FONT_OPTIONS_NORMAL = ("Arial", 16, "bold")
LABEL_OPTIONS_FRONT = {
    "bg": CARD_FRONT_COLOR,
    "fg": CARD_BACK_COLOR
}
LABEL_OPTIONS_BACK = {
    "bg": CARD_BACK_COLOR,
    "fg": CARD_FRONT_COLOR
}

LANG_SOURCE = "English"
LANG_TARGET = "Japanese"

window = Tk()
window.title("Learn Japanese")
window.minsize(width=CARD_WIDTH, height=CARD_HEIGHT)
window.config(padx=WINDOW_PADDING, pady=WINDOW_PADDING, bg=BACKGROUND_COLOR)

# Import images
pil_img_card_front = Image.open(
    "./images/card_front.png").resize((CARD_WIDTH, CARD_HEIGHT))
pil_img_card_back = Image.open(
    "./images/card_back.png").resize((CARD_WIDTH, CARD_HEIGHT))
img_card_front = ImageTk.PhotoImage(pil_img_card_front)
img_card_back = ImageTk.PhotoImage(pil_img_card_back)

img_button_right = PhotoImage(file="./images/right.png")
img_button_wrong = PhotoImage(file="./images/wrong.png")

# Setup canvas
canvas_card = Canvas(width=CARD_WIDTH, height=CARD_HEIGHT,
                     bg=BACKGROUND_COLOR, highlightthickness=0)
container_card = canvas_card.create_image(
    CARD_WIDTH/2, CARD_HEIGHT/2, anchor="center", image=img_card_front)
canvas_card.grid(row=0, column=0, rowspan=5, columnspan=3, sticky='nesw')

# Setup labels
label_lang = Label(text=LANG_TARGET, font=FONT_OPTIONS_TITLE,
                   **LABEL_OPTIONS_FRONT)
label_word = Label(text="WORD", font=FONT_OPTIONS_SUBTITLE,
                   **LABEL_OPTIONS_FRONT)
label_lang.grid(row=1, column=1, sticky='ew')
label_word.grid(row=2, column=1, sticky='ew')

# Setup buttons
btn_right = Button(image=img_button_right, **BUTTON_OPTIONS)
btn_wrong = Button(image=img_button_wrong, **BUTTON_OPTIONS)
btn_right.grid(row=5, column=0)
btn_wrong.grid(row=5, column=2)

window.mainloop()
