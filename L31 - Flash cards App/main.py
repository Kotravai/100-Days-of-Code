from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
TITLE1 = "French"
WORD1 = NONE
learnt_dict = {}

#  --------------------- TIMER -----------------------------------#

# -------------------------Button Click Methods ---------------------#
try:
    file = pandas.read_csv("data/Words to learn.csv")
except FileNotFoundError:
    file = pandas.read_csv("data/french_words.csv")
    #file_dict = dict(zip(file.French, file.English))

file_dict = file.to_dict(orient='records')


def next_card():
    global card
    card = random.choice(file_dict)
    canvas.itemconfig(french_window, image=card_front)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=card['French'], fill="black")
    window.update()
    window.after(3000, english_card(card))
    # english_card(card)

    # n = random.randint(0, 100)
    # WORD1 = list(file_dict.items())[n][0]
    # canvas.itemconfig(title_text, text=TITLE1)
    # canvas.itemconfig(word_text, text=WORD1)


def english_card(choice):
    canvas.itemconfig(word_text, text=choice['English'], fill="white")
    canvas.itemconfig(french_window, image=card_green)
    canvas.itemconfig(title_text, text="English", fill="white")


def is_known():
    file_dict.remove(card)
    data = pandas.DataFrame(file_dict)
    data.to_csv("data/Words to learn.csv", index=False)
    next_card()


# -------------------- MAKING THE SCREEN ------------------------ #


window = Tk()
window.title("Learn French Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=40, pady=40)

card_front = PhotoImage(file="images/card_front.png")
card_green = PhotoImage(file="images/card_back.png")
tick = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=800, height=526)
french_window = canvas.create_image(400, 263, image=card_front)
title_text = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"), fill="black")
word_text = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"), fill="black")
canvas.config(highlightthickness=0, background=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=3)

tick_button = Button(image=tick, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=is_known)
tick_button.config(pady=20, padx=20)
wrong_button = Button(image=wrong, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=next_card)
wrong_button.config(padx=20, pady=20)

tick_button.grid(row=2, column=0)
wrong_button.grid(row=2, column=2)

next_card()

window.mainloop()
