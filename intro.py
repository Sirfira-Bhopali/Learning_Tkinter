from tkinter import *
root=Tk()
root.geometry("300x150")
root.title("Greet me")
label1=Label(root,text="")
def greet():
    global label1
    label1.pack_forget()
    label1=Label(root,text="hii "+entry1.get())
    label1.pack()

entry1=Entry(root)
entry1.pack()
b1=Button(root,text="Greet",command=greet).pack()

root.mainloop()