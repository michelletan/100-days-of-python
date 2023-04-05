from tkinter import Canvas
from PIL import Image, ImageTk


class Card(Canvas):
    """Draws a canvas representing a flash card.
    Handles display of the flash card text and flip function."""

    def __init__(self, card_width, card_height, background_color) -> None:
        super().__init__(width=card_width, height=card_height,
                         bg=background_color, highlightthickness=0)
        self.is_front = True

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

    def flip(self, _):
        self.is_front = not self.is_front
        new_img = self.img_card_front if self.is_front else self.img_card_back
        self.itemconfig(self.container, image=new_img)
