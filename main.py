from tkinter import *
from pandas import *
from random import *

from pandas.core.methods.to_dict import to_dict

BACKGROUND_COLOR = "#B1DDC6"
current_value = {}
data_dict  = {}
# -------------------brain----------------#
try:
    data =read_csv("./data/word_to_learn.csv")
except FileNotFoundError:
    orginal_data = read_csv("./data/french_words.csv")
    data_dict = orginal_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")
def next_card():
    global current_value,flip_timer
    window.after_cancel(flip_timer)
    current_value = choice(data_dict)
    canvas.itemconfig(title,text="French",fill="black")
    canvas.itemconfig(answer,text=current_value["French"],fill="black")
    canvas.itemconfig(bg,image=front_image)
    flip_timer = window.after(3000, func=flipcard)
def flipcard():
    canvas.itemconfig(title,text="English",fill="white")
    canvas.itemconfig(answer,text=current_value["English"],fill="white")
    canvas.itemconfig(bg,image=flash_card)
def is_know():
    data_dict.remove(current_value)
    removed_data = DataFrame(data_dict)
    removed_data.to_csv("./data/word_to_learn.csv",index=False)
    next_card()

# ------------------UI-----------------#
window = Tk()
window.title("Flash Card")
window.config(padx=15,pady=15,bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,func=flipcard)

canvas = Canvas(width=800,height=526)
front_image = PhotoImage(file="./images/card_front.png")
flash_card = PhotoImage(file="./images/card_back.png")
bg = canvas.create_image(400,263,image=front_image)
title = canvas.create_text(400,150,text="",font=("Arial",40,"italic"))
answer = canvas.create_text(400,263,text="",font=("Arial",40,"bold"))

canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image,bg=BACKGROUND_COLOR,highlightthickness=0,command=next_card)
wrong_button.grid(row=1,column=0)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image,bg=BACKGROUND_COLOR,highlightthickness=0,command=is_know)
right_button.grid(row=1,column=1)

next_card()
window.mainloop()