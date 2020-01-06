from tkinter import *

frame=Tk()
def click():
    Label(frame,text="ahh... you clicked me").grid(row=1,column=0)

Button(frame,text="click me not",command=click).grid(row=0,column=0)

frame.mainloop()