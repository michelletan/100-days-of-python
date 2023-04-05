from tkinter import Canvas
from PIL import Image, ImageTk


class Card(Canvas):
    """Draws a canvas representing an empty flash card.
    Handles display of the flash card images and flip function.

    Attributes:
        - is_front: Represents the state of the card
        - on_card_clicked: Optional callback function for when the card is clicked
        - img_card_front: Image for the front of the card
        - img_card_back: Image for the back of the card
        - container: Image container for the card
    """

    def __init__(self, card_width, card_height, background_color, on_card_clicked) -> None:
        super().__init__(width=card_width, height=card_height,
                         bg=background_color, highlightthickness=0)
        self.is_front = True
        self.on_card_clicked = on_card_clicked

        # Import images
        pil_img_card_front = Image.open(
            "./images/card_front.png").resize((card_width, card_height))
        pil_img_card_back = Image.open(
            "./images/card_back.png").resize((card_width, card_height))

        self.img_card_front = ImageTk.PhotoImage(pil_img_card_front)
        self.img_card_back = ImageTk.PhotoImage(pil_img_card_back)

        self.container = self.create_image(
            card_width/2, card_height/2, anchor="center", image=self.img_card_front)
        self.bind("<Button-1>", self.flip)

    def flip(self, event):
        self.is_front = not self.is_front

        self.update_card()

        # If there is a callback for the click event, call it
        if self.on_card_clicked:
            self.on_card_clicked(event)

    def reset(self):
        self.is_front = True
        self.update_card()

    def update_card(self):
        new_img = self.img_card_front if self.is_front else self.img_card_back
        self.itemconfig(self.container, image=new_img)
