# import modules
from tkinter import *


# define all functions
def clicked():
    name = name_entry.get()
    surname = surname_entry.get()
    message_label.config(text="Welcome " + name + " " + surname + "! You have registered.")


# create window
window = Tk()
window.title("Exercise 5")
window.geometry("300x150")

# create widgets
top_frame = Frame(window)
middle_frame = Frame(window)
name_label = Label(top_frame, text="Name")
name_entry = Entry(top_frame)
surname_label = Label(middle_frame, text="Surname")
surname_entry = Entry(middle_frame)
register_button = Button(window, text="Register", command=clicked)
message_label = Label(window, text="Message")

# pack widgets into window container
top_frame.pack(fill="both")
middle_frame.pack(fill="both")
name_label.pack(side=LEFT)
name_entry.pack(side=RIGHT, fill="both", expand=True)
surname_label.pack(side=LEFT)
surname_entry.pack(side=LEFT, fill="both", expand=True)
register_button.pack()
message_label.pack()

# open window
window.mainloop()
