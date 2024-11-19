# import modules
from tkinter import *


# define all functions
def login():
    login_text = username_entry.get()
    message_label.config(text="Welcome, " + login_text + ".")


def clear_form():
    # get() len() of username entry text.
    username_text = username_entry.get()
    username_length = len(username_text)
    # if username_length > 0 then delete() text from entry form up to length
    if username_length > 0:
        username_entry.delete(0, username_length)

    # get() len() of password entry text.
    password_text = password_entry.get()
    password_length = len(password_text)
    # if password_length > 0 then delete() text from entry form up to length
    if password_length > 0:
        password_entry.delete(0, password_length)


def exit_program():
    print("closing ...")
    # terminate/finish this python program and return code 0; meaning no errors
    exit(0)


# create window
window = Tk()
window.title("Exercise 7")
window.geometry("300x105")

# create widgets
username_label = Label(window, text="Username:")
password_label = Label(window, text="Password:")
message_label = Label(window, text="Welcome")
username_entry = Entry(window)
password_entry = Entry(window)
submit_button = Button(window, text="Submit", command= login)
clear_button = Button(window, text="Clear", command= clear_form)
close_button = Button(window, text="Close", command= exit_program)

# place widgets into window container using the grid layout
username_label.grid(row=0, column=0)
username_entry.grid(row=0, column=1, columnspan=2)
password_label.grid(row=1, column=0)
password_entry.grid(row=1, column=1, columnspan=2)
submit_button.grid(row=2, column=0)
clear_button.grid(row=2, column=1)
close_button.grid(row=2, column=2)
message_label.grid(row=3, column=0, columnspan=2)

# open window
window.mainloop()
