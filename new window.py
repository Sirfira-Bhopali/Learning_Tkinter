<<<<<<< HEAD
from tkinter import *
root=Tk()

def click():
    new_window=Toplevel()
    label=Label(new_window,text="Hey !!! I'm a new window ").pack()
    button_exit=Button(new_window,text="EXIT",command=new_window.destroy).pack()

button=Button(root,text="click me!",padx=10,pady=10,command=click).pack(padx=10,pady=10)

=======
from tkinter import *
root=Tk()

def click():
    new_window=Toplevel()
    label=Label(new_window,text="Hey !!! I'm a new window ").pack()
    button_exit=Button(new_window,text="EXIT",command=new_window.destroy).pack()

button=Button(root,text="click me!",padx=10,pady=10,command=click).pack(padx=10,pady=10)

>>>>>>> d58411fc1358ab69c34a05a5a12f4d3f9e5498d0
mainloop()