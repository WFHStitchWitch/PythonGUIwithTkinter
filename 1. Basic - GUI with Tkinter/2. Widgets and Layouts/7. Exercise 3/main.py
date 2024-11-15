from tkinter import *

window = Tk()
window.title("Exercise 3")

top_frame = Frame(window)
left_frame = Frame(window)
right_frame = Frame(window)
left_middle_frame = Frame(left_frame)
left_bottom_frame = Frame(left_frame)

top_frame.pack()
left_frame.pack(side=LEFT)
right_frame.pack(side=RIGHT)
left_middle_frame.pack()
left_bottom_frame.pack()

text1 = Label(top_frame, text="This application demonstrates frame layout")
text2 = Label(right_frame, text="This application demonstrates frame layout")
button1 = Button(left_middle_frame, text="Button 1", fg="green")
button2 = Button(left_middle_frame, text="Button 2", fg="red")
button3 = Button(left_bottom_frame, text="Button 3", fg="blue")
button4 = Button(left_bottom_frame, text="Button 4", fg="blue")

text1.pack()
text2.pack(side=RIGHT)
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)

window.mainloop()
