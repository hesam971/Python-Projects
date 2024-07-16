from tkinter import *
from tkinter import messagebox
import random
import json

# init tk
windows = Tk()
windows.title("pass_manager")
windows.config(pady=20, padx=20)

# create canvas
myCanvas = Canvas(height=200, width=200)


# call data
def call_data():
    with open("new_data.json", "r") as new_json:
        try:
            read_data = json.load(new_json)
            messagebox.showinfo(title=f"{E1.get()} info", message=f"email:{read_data[E1.get()]['email']} \n password: {read_data[E1.get()]['password']}")
        except json.decoder.JSONDecodeError:
            messagebox.showerror(title="Error", message="the json file is empty")
        except KeyError:
            messagebox.showerror(title="Error", message="the webpage is not exist.")


# Password Generator Project
def pass_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    [password_list.append(random.choice(letters)) for _ in range(nr_letters)]
    [password_list.append(random.choice(symbols)) for _ in range(nr_symbols)]
    [password_list.append(random.choice(numbers)) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    print(f"Your password is: {password}")
    E3.insert(0, password)


# add function
def add_to_text():
    all_data = [E1.get(), E2.get(), E3.get(), "\n"]
    last_edit = " / ".join(all_data)

    # check for the empty value
    if len(E1.get()) == 0 or len(E2.get()) == 0 or len(E3.get()) == 0:
        messagebox.showerror(title="Error", message="please fill the inputs")
    else:
        # check for the save the info
        popup_answer = messagebox.askyesnocancel(title="save info", message="do you want to save them?")
        if popup_answer:
            web_info = E1.get()
            email_info = E2.get()
            pass_info = E3.get()
            our_json_info = \
                {
                    web_info:
                        {
                            "email": email_info,
                            "password": pass_info
                        }

                }

            try:
                with open("new_data.json", "r") as new_json:
                    read_data = json.load(new_json)
                    read_data.update(our_json_info)
            except json.decoder.JSONDecodeError:
                with open("new_data.json", "w") as new_json_file:
                    json.dump(our_json_info, new_json_file, indent=4)
            else:
                with open("new_data.json", "w") as new_json_file:
                    json.dump(read_data, new_json_file, indent=4)

            E1.delete(0, END)
            E2.delete(0, END)
            E3.delete(0, END)


# image
pass_image = PhotoImage(file='logo.png')
myCanvas.create_image(100, 100, image=pass_image)
myCanvas.grid(row=2, column=1)

# website text
web_text = Label(text="website: ", font=("Courier", 14))
web_text.grid(row=3, column=0)
# email/username text
username = Label(text="email/username: ", font=("Courier", 14))
username.grid(row=4, column=0)
# password text
password = Label(text="password: ", font=("Courier", 14))
password.grid(row=5, column=0)

# input for web_text
E1 = Entry(width=21)
E1.grid(row=3, column=1)
E1.focus()
# input for email/username
E2 = Entry(width=38)
E2.grid(row=4, column=1, columnspan=2)
E2.insert(0, "hesam971@gmail.com")
# input for password
E3 = Entry(width=21)
E3.grid(row=5, column=1)
# Create button for next text.
gen_pass = Button(text="Generate Password", command=pass_generator)
gen_pass.grid(row=5, column=2)
# Create button for next text.
add_button = Button(text="Add", width=36, command=add_to_text)
add_button.grid(row=6, column=1, columnspan=2)
# Create button for search data.
add_button = Button(text="Search", width=13, command=call_data)
add_button.grid(row=3, column=2)
# add to window and show
windows.mainloop()
