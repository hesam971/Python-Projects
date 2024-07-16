from tkinter import *
import requests
import html

dic = {
    "amount": 50,
    "type": "boolean"
}

response = requests.get("https://opentdb.com/api.php", params=dic)
json_answer = response.json()["results"]
all_question = [(html.unescape(json_answer[i]["question"]), json_answer[i]["correct_answer"]) for i in
                range(0, len(json_answer))]
VALUE = 0
SCORE = 0


class QuizApp:
    def __init__(self):
        self.windows = Tk()
        self.windows.config(bg="gray")
        self.label = Label(text=f"Score: {SCORE}", bg="gray", padx=20, pady=20)
        self.label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, )
        self.canvas.grid(row=1, column=0, columnspan=2, padx=40)
        self.canvas_text = self.canvas.create_text(150, 125, text=f"{all_question[VALUE][0]}", fill='black',
                                                   font=("Arial", 20), width=280)
        self.windows.title("Quiz_App")
        self.true_image = PhotoImage(file="images/true.png")
        self.false_image = PhotoImage(file="images/false.png")
        self.button = Button(image=self.true_image, command=self.check_right_answer)
        self.button.grid(row=2, column=0, pady=20)
        self.button = Button(image=self.false_image, command=self.check_false_answer)
        self.button.grid(row=2, column=1, pady=20)
        self.windows.mainloop()

    def check_right_answer(self):
        global VALUE, SCORE
        VALUE += 1
        if all_question[VALUE][1] == "True":
            SCORE += 1
            self.label["text"] = f"Score: {SCORE}"
        self.canvas.itemconfig(self.canvas_text, text=f"{all_question[VALUE][0]}")

    def check_false_answer(self):
        global VALUE, SCORE
        VALUE += 1
        if all_question[VALUE][1] == "False":
            SCORE += 1
            self.label["text"] = f"Score: {SCORE}"
        self.canvas.itemconfig(self.canvas_text, text=f"{all_question[VALUE][0]}")
