# import modules
from tkinter import *

# create window
window = Tk()
window.title("Python GUI with tkinter grid layouts")
window.geometry("300x350")

# create widgets
username_label = Label(window, text="Username:")
password_label = Label(window, text="Password:")
username_entry = Entry(window)
password_entry = Entry(window)
submit_button = Button(window, text="Submit")
clear_button = Button(window, text="Clear")
close_button = Button(window, text="Close")

# place widgets into window container using the grid layout
username_label.grid(row=0, column=0)
username_entry.grid(row=0, column=1, columnspan=2)
password_label.grid(row=1, column=0)
password_entry.grid(row=1, column=1, columnspan=2)
submit_button.grid(row=2, column=0, sticky="we")
clear_button.grid(row=2, column=1, sticky="we")
close_button.grid(row=2, column=2, sticky="we")

# open window
window.mainloop()
