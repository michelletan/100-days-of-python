import random
import pandas
from tkinter import Tk, PhotoImage, Label
from tkmacosx import Button
from card import Card

# UI Options
BACKGROUND_COLOR = "#B1DDC6"
WINDOW_PADDING = 40
CARD_WIDTH = 600
CARD_HEIGHT = 400
CARD_FRONT_COLOR = "#FFFFFF"
CARD_BACK_COLOR = "#88BAA7"
LABEL_OPTIONS_FRONT = {
    "bg": CARD_FRONT_COLOR,
    "fg": CARD_BACK_COLOR
}
LABEL_OPTIONS_BACK = {
    "bg": CARD_BACK_COLOR,
    "fg": CARD_FRONT_COLOR
}
FONT_OPTIONS_TITLE = ("Arial", 25, "bold")
FONT_OPTIONS_SUBTITLE = ("Arial", 20, "bold")
FONT_OPTIONS_NORMAL = ("Arial", 16, "bold")

BUTTON_SIZE = 60
BUTTON_OPTIONS = {
    "bg": BACKGROUND_COLOR,
    "activebackground": BACKGROUND_COLOR,
    "focusthickness": 0,
    "borderless": True
}
LANG_SOURCE = "English"
LANG_TARGET = "Japanese"

# Settings
DATA_FILEPATH = "./data/ja_data.csv"
LEARNING_PILE_FILEPATH = "./saves/learning_pile.csv"
DISCARD_PILE_FILEPATH = "./saves/discard_pile.csv"

# State variables
learning_data: pandas.DataFrame = None
discard_data: pandas.DataFrame = None
current_text: pandas.Series = None

# ---------------------------- FLASH CARD LOGIC ------------------------------- #


def load_data():
    """Loads cards for the learning and discard piles from CSV save files. 
    If there is no learning pile save, loads from the original dataset.
    If there is no discard pile save, creates an empty dataframe.
    """
    global learning_data, discard_data
    try:
        l_data = pandas.read_csv(LEARNING_PILE_FILEPATH)
    except FileNotFoundError:
        l_data = pandas.read_csv(DATA_FILEPATH)
    finally:
        learning_data = l_data

    try:
        d_data = pandas.read_csv(DISCARD_PILE_FILEPATH)
    except FileNotFoundError:
        d_data = pandas.DataFrame(columns=['japanese', 'english', 'romaji'])
    finally:
        discard_data = d_data


def save_data():
    """Saves the learning and discard piles to CSV save files, then
    closes the application window."""
    global learning_data, discard_data

    discard_data.to_csv(DISCARD_PILE_FILEPATH, index=False)
    learning_data.to_csv(LEARNING_PILE_FILEPATH, index=False)

    window.destroy()


def show_new_card():
    """Randomises an index, then picks a card from the learning pile."""
    global learning_data, current_text, card
    num_rows = len(learning_data.index)
    random_index = random.randint(0, num_rows)
    current_text = learning_data.iloc[random_index]
    card.reset()
    update_card_text()


def update_card_text():
    """Updates the text shown on the card, depending on whether the card is showing
    the front or the back. Also updates the colours for the label accordingly."""
    global card, label_lang, label_word, current_text
    if card.is_front:
        label_lang.config(text=LANG_TARGET, **LABEL_OPTIONS_FRONT)
        label_word.config(
            text=f"{current_text.japanese}", **LABEL_OPTIONS_FRONT)
        label_subword.config(text="        ", **LABEL_OPTIONS_FRONT)
    else:
        label_lang.config(text=LANG_SOURCE, **LABEL_OPTIONS_BACK)
        label_word.config(text=f"{current_text.english}", **LABEL_OPTIONS_BACK)
        label_subword.config(
            text=f"{current_text.romaji}", **LABEL_OPTIONS_BACK)


def add_to_discard_pile(text: pandas.Series):
    global discard_data

    new_df = pandas.DataFrame([text])
    discard_data = pandas.concat([new_df, discard_data])


def on_card_clicked(_):
    update_card_text()


def on_right_btn_clicked():
    """Callback for the right button.

    Adds the currently shown card to the discard pile, then removes it from the learning pile.

    Refreshes the currently shown card."""
    global current_text

    add_to_discard_pile(current_text)

    print(learning_data[learning_data.japanese == current_text.japanese])
    learning_data.drop(
        learning_data[learning_data.japanese == current_text.japanese].index, inplace=True)
    print(learning_data[learning_data.japanese == current_text.japanese])
    show_new_card()


def on_wrong_btn_clicked():
    """Callback for the wrong button.

    The user's intention is to keep the currently shown card in the learning pile,
    so just refresh the currently shown card, no other action is needed."""
    show_new_card()


def main():
    load_data()
    show_new_card()
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Learn Japanese")
window.minsize(width=CARD_WIDTH, height=CARD_HEIGHT)
window.config(padx=WINDOW_PADDING, pady=WINDOW_PADDING, bg=BACKGROUND_COLOR)

card = Card(card_width=CARD_WIDTH, card_height=CARD_HEIGHT,
            background_color=BACKGROUND_COLOR, on_card_clicked=on_card_clicked)
card.grid(row=0, column=0, rowspan=5, columnspan=3, sticky='nesw')

img_button_right = PhotoImage(file="./images/right.png")
img_button_wrong = PhotoImage(file="./images/wrong.png")

# Setup labels
label_lang = Label(text=LANG_TARGET, font=FONT_OPTIONS_TITLE,
                   **LABEL_OPTIONS_FRONT)
label_word = Label(text="WORD", font=FONT_OPTIONS_SUBTITLE,
                   **LABEL_OPTIONS_FRONT)
label_subword = Label(text="Romaji", font=FONT_OPTIONS_NORMAL,
                      **LABEL_OPTIONS_FRONT)
label_lang.grid(row=1, column=1, sticky='ew')
label_word.grid(row=2, column=1, sticky='ew')
label_subword.grid(row=3, column=1, sticky='ew')

# Setup buttons
btn_right = Button(image=img_button_right,
                   command=on_right_btn_clicked, **BUTTON_OPTIONS)
btn_wrong = Button(image=img_button_wrong,
                   command=on_wrong_btn_clicked, **BUTTON_OPTIONS)
btn_right.grid(row=5, column=0)
btn_wrong.grid(row=5, column=2)

main()

# Triggers when user closes window
window.protocol("WM_DELETE_WINDOW", save_data)
window.mainloop()
