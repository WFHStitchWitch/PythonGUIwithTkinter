# import modules
from tkinter import *


# define all functions
def clicked():
    text = entry_text.get()
    print("Hello,", text + "! How are you?")


# create window
window = Tk()
window.title("Clicking application")
window.geometry("300x350")

# create widgets
text1 = Label(window, text="Enter your name here")
button1 = Button(window, text="Click me!", command=clicked)
entry_text = Entry(window)
password_text = Entry(window, show="*")
# pack widgets into window container
text1.pack()
button1.pack()
entry_text.pack()
password_text.pack()
# open window
window.mainloop()
