from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
timer1 = ""
word = {}
data_dict = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")



def next_card():
    global word, flip_timer
    window.after_cancel(flip_timer)
    word = random.choice(data_dict)
    canvas.itemconfig(lang_text, text= "French", fill= "black")
    canvas.itemconfig(text, text= word["French"], fill= "black")
    canvas.itemconfig(img_canvas, image=card_front_img)
    flip_timer = window.after(3000, func=create_card)

def is_known():
    data_dict.remove(word)
    data = pandas.DataFrame(data_dict)
    data.to_csv("data/words_to_learn.csv", index= False)
    next_card()

def create_card():
    canvas.itemconfig(lang_text, text="English", fill= "white")
    canvas.itemconfig(text, text= word["English"], fill= "white")
    canvas.itemconfig(img_canvas, image= card_back_img)



window = Tk()
window.title('Flash Card Game')
window.config(padx=50, pady=50,  bg= BACKGROUND_COLOR)
flip_timer = window.after(3000, create_card)

# Canvases
canvas = Canvas(width=800, height=526, bg= BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
img_canvas =canvas.create_image(400, 263, image= card_front_img)
lang_text = canvas.create_text(400, 150, text= "Title",font=("Arial", 40, "italic"))
text = canvas.create_text(400, 263, text= "word",font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()

