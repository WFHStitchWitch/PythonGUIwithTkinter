# import modules
from tkinter import *

# create window
window = Tk()
window.title("Exercise 6")
window.geometry("300x350")

# create widgets
text1= Label(window, text= "Text 1")
button1 = Button(window,text= "Button 1")
button2 = Button(window, text= "Button 2")
button3 = Button(window, text= "Button 3")
button4 = Button(window, text= "Button 4")
text2 = Label(window, text= "Text 2")
# place widgets into window container using the grid layout
text1.grid(row=0, column=0, columnspan=3)
button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=2, column=0)
button4.grid(row=2, column=1)
text2.grid(row=1, column=2, rowspan=2)

# open window
window.mainloop()
