from tkinter import *

frame=Tk()

def click():
    label1=Label(frame,text="hii "+ e.get())
    label1.grid(row=3,column=0)

e=Entry(frame)
e.grid(row=0,column=0)

b1=Button(frame,text="entered",command=click)
b1.grid(row=1,column=0)

mainloop()

"""a().b() result is whatever b() returns and pack(),grid() returns none.
so we have to place a() and b() differently when we need to get result from a()"""