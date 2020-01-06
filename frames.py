from tkinter import *

root=Tk()

frame=LabelFrame(text="heyo !!!",padx=10,pady=10)
frame.pack(padx=10,pady=10)

b1=Button(frame,text="just a button")
b1.grid(row=0,column=0)
b2=Button(frame,text="just another button")
b2.grid(row=1,column=1)

mainloop()