from tkinter import *

window = Tk()
window.title("Exercise 2")

topFrame = Frame(window)
middleupperframe = Frame(window)
middlelowerframe = Frame(window)
bottomframe = Frame(window)

topFrame.pack()
middleupperframe.pack()
middlelowerframe.pack()
bottomframe.pack()

text1 = Label(topFrame, text="This application demonstrates frame layout")
button1 = Button(middleupperframe, text="Button 1", fg="green")
button2 = Button(middleupperframe, text="Button 2", fg="red")
button3 = Button(middleupperframe, text="Button 3", fg="blue")
button4 = Button(middlelowerframe, text="Button 4", fg="blue")
button5 = Button(middlelowerframe, text="Button 5", fg="green")
button6 = Button(middlelowerframe, text="Button 6", fg="red")
button7 = Button(bottomframe, text="Button 7", fg="blue")
button8 = Button(bottomframe, text="Button 8", fg="blue")
button9 = Button(bottomframe, text="Button 9", fg="blue")

text1.pack()
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)
button5.pack(side=LEFT)
button6.pack(side=LEFT)
button7.pack(side=LEFT)
button8.pack(side=LEFT)
button9.pack(side=LEFT)


window.mainloop()
