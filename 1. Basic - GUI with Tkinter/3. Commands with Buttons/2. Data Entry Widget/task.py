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
text1 = Label(window, text="Hi.")
button1 = Button(window, text="Click me.", command=clicked)
name_label = Label(window, text="Username")
pw_label = Label(window, text="Password")
entry_text = Entry(window)
entry2 = Entry(window, show="*")
frame1 = Frame(window)
frame2 = Frame(window)
frame3 = Frame(window)
# pack widgets into window container
frame1.pack()
frame2.pack()
frame3.pack()
text1.pack(frame1)
name_label.pack(frame2, side=LEFT)
entry_text.pack(frame2, side=RIGHT)
pw_label.pack(frame3, side=LEFT)
entry2.pack(frame3, side=RIGHT)
button1.pack()

# open window
window.mainloop()
