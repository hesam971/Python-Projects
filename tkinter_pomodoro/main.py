from tkinter import *
import math
windows = Tk()
TIMER = None
CONTROLLER = 0
check_mark_list = ""


def control_start_counting():
    global CONTROLLER
    CONTROLLER += 1

    """Long period break"""
    if CONTROLLER % 8 == 0:
        start_counting(20 * 60)
        timer_label["text"] = "Long break Time"
        """Break period"""
    elif CONTROLLER % 2 == 0:
        start_counting(5 * 60)
        timer_label["text"] = "Break Time"
    else:
        """work period"""
        start_counting(10)
        timer_label["text"] = "Work Time"


def start_counting(sec):
    global TIMER
    second = math.floor(sec % 60)
    minute = math.floor(sec / 60)

    if second < 10:
        second = f"0{second}"

    if second == 0:
        second = "00"

    canvas.itemconfig(timer_counter, text=f"{minute}:{second}")
    if sec > 0:
        TIMER = windows.after(1000, start_counting, sec - 1)
    else:
        control_start_counting()
        """check_mark controller"""
        if CONTROLLER % 2 == 0:
            check_mark["text"] += "✓"


def reset_counting():
    global CONTROLLER, check_mark_list
    windows.after_cancel(TIMER)
    canvas.itemconfig(timer_counter, text="00:00")
    timer_label["text"] = "Timer"
    CONTROLLER = 0
    check_mark["text"] = ""


windows.title("pomodoro")
windows.config(padx=20, pady=20)
canvas = Canvas(width=200, height=224, highlightthickness=0)
python_image = PhotoImage(file='tomato.png')
canvas.create_image((100, 112), image=python_image)
canvas.grid(column=2, row=2)
timer_counter = canvas.create_text((105, 122), text="00:00", font=("Arial", 30), fill="white")
timer_label = Label(text='Timer', fg="red", font=('Arial', 30))
timer_label.grid(column=2, row=1)
check_mark = Label(text=check_mark_list, fg="green", font=('Arial', 30))
check_mark.grid(column=2, row=3)
start_button = Button(text="start", command=control_start_counting)
start_button.grid(column=1, row=3)
reset_button = Button(text="reset", command=reset_counting)
reset_button.grid(column=3, row=3)


windows.mainloop()


