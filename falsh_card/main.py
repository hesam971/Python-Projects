from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
random_word = {}
to_learn = {}
try:
    read_csv = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = remind_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = read_csv.to_dict(orient="records")
# create a function to choice a random word
def word_reader():
    global random_word, after_id
    windows.after_cancel(after_id)
    random_word = random.choice(to_learn)
    canvas.itemconfig(word_definition, text=random_word["French"], fill='black')
    canvas.itemconfig(language_name, text="French", fill='black')
    canvas.itemconfig(old_image, image=img)
    windows.after(3000, change_card)


def change_card():
    canvas.itemconfig(language_name, text="English", fill='white')
    canvas.itemconfig(word_definition, text=random_word["English"], fill='white')
    canvas.itemconfig(old_image, image=back_img)

def save_cards():
    to_learn.remove(random_word)
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    word_reader()


windows = Tk()
windows.title("flash_card_capstone")
windows.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# read the answer of card
after_id = windows.after(3000, change_card)
# Create a canvas
canvas = Canvas(width=800, height=526)
canvas.grid(row=1, column=0, columnspan=2)
# Load a front image in the script
img = PhotoImage(file="images/card_front.png")
# Add image to the Canvas Items
old_image = canvas.create_image(400, 263, image=img)
# Load a back image in the script
back_img = PhotoImage(file="images/card_back.png")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
# add two button  as pass or fail
fail_photo = PhotoImage(file="images/wrong.png")
fail_button = Button(image=fail_photo, highlightthickness=0, command=word_reader)
fail_button.grid(row=2, column=0)
pass_photo = PhotoImage(file="images/right.png")
pass_button = Button(image=pass_photo, highlightthickness=0, command=save_cards)
pass_button.grid(row=2, column=1)
# Add a text in Canvas
language_name = canvas.create_text(400, 150, text="", fill="black", font=("Arial", 40))
word_definition = canvas.create_text(400, 263, text="", fill="black", font=("Arial", 60))
# call the function to fill the text
word_reader()

windows.mainloop()
