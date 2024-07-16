import tkinter

window = tkinter.Tk()

window.title("My Do-Nothing Application")
window.minsize(200, 200)


def click():
    answer["text"] = round(float(entry.get()) * 1.609344)  # 1 mile = 1.609344 kilometers
    #print(f"{entry.get()}")


equal = tkinter.Label(text="is equal to")
equal.grid(column=0, row=1)

button = tkinter.Button(text="calculate", command=click)
button.grid(column=1, row=2)


entry = tkinter.Entry(width=5)
entry.grid(column=1, row=0)

Miles = tkinter.Label(text="Miles")
Miles.grid(column=2, row=0)

Km = tkinter.Label(text="Km")
Km.grid(column=2, row=1)

answer = tkinter.Label(text=0)
answer.grid(column=1, row=1)


# start the program
window.mainloop()
