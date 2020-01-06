from tkinter import *

frame=Tk()

def click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def add():
    global f_num
    global math
    f_num=e.get()
    e.delete(0,END)
    math=add

def substract():
    global f_num
    global math
    f_num=e.get()
    e.delete(0, END)
    math=substract

def multiply():
    global f_num
    global math
    f_num=e.get()
    e.delete(0, END)
    math=multiply

def divide():
    global f_num
    global math
    f_num=e.get()
    e.delete(0, END)
    math=divide

def clear():
    e.delete(0,END)

def equate():
    sec_num=e.get()
    e.delete(0,END)
    if math==add:
        e.insert(0,str(int(f_num)+int(sec_num)))
    if math==substract:
        e.insert(0,str(int(f_num)-int(sec_num)))
    if math==multiply:
        e.insert(0,str(int(f_num)*int(sec_num)))
    if math==divide:
        e.insert(0,str(int(f_num)/int(sec_num)))

e=Entry(frame,width=45)
e.grid(row=0,column=0,columnspan=3,pady=15)

b1=Button(frame,text="1",command=lambda: click(1),padx=40,pady=20)
b2=Button(frame,text="2",command=lambda: click(2),padx=40,pady=20)
b3=Button(frame,text="3",command=lambda: click(3),padx=40,pady=20)
b4=Button(frame,text="4",command=lambda: click(4),padx=40,pady=20)
b5=Button(frame,text="5",command=lambda: click(5),padx=40,pady=20)
b6=Button(frame,text="6",command=lambda: click(6),padx=40,pady=20)
b7=Button(frame,text="7",command=lambda: click(7),padx=40,pady=20)
b8=Button(frame,text="8",command=lambda: click(8),padx=40,pady=20)
b9=Button(frame,text="9",command=lambda: click(9),padx=40,pady=20)
b0=Button(frame,text="0",command=lambda: click(0),padx=40,pady=20)
b_clear=Button(frame,text="Clear",padx=30,pady=20,command=clear)
b_add=Button(frame,text="+",padx=40,pady=20,command=add)
b_substract=Button(frame,text="-",padx=40,pady=20,command=substract)
b_multiply=Button(frame,text="*",padx=40,pady=20,command=multiply)
b_divide=Button(frame,text="/",padx=40,pady=20,command=divide)
b_equal=Button(frame,text="equate",command=equate,width=40,height=4)

b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)
b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)
b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)
b0.grid(row=4,column=0)
b_clear.grid(row=4,column=1)
b_add.grid(row=4,column=2)
b_substract.grid(row=5,column=0)
b_multiply.grid(row=5,column=1)
b_divide.grid(row=5,column=2)
b_equal.grid(row=6,column=0,columnspan=3)

mainloop()
