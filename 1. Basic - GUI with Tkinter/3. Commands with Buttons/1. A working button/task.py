# 1. import required modules
from tkinter import *


# 2. define functions
def clickityclack():
    print("Hello there, I am working")


window = Tk()
window.title("Clicking application")
window.geometry("300x350")

button1 = Button(window, text="Click me!", command=clickityclack)
button1.pack()

window.mainloop()