from tkinter import *
root=Tk()
root.title("Your VIT score card")
root.geometry("300x250")


def show():
    global l1,l2,l3,l4
    l1.pack_forget()
    l2.pack_forget()
    l3.pack_forget()
    l4.pack_forget()

    l1=Label(root,text=var1.get())
    l2=Label(root,text=var2.get())
    l3=Label(root,text=var3.get())
    l4=Label(root,text=var4.get())

    l1.pack()
    l2.pack()
    l3.pack()
    l4.pack()

frame1=LabelFrame(root,text="options")
frame1.pack(padx=10,pady=15)

var1=StringVar()
var2=StringVar()
var3=StringVar()
var4=StringVar()

cb1=Checkbutton(frame1,text="Fucked up FFCS",variable=var1,command=show,onvalue="50")
cb2=Checkbutton(frame1,text="Caught while giving proxy",variable=var2,command=show,onvalue="100")
cb3=Checkbutton(frame1,text="Hugged someone of opposite gender",variable=var3,command=show,onvalue="150")
cb4=Checkbutton(frame1,text="Attended today's session :P",variable=var4,command=show,onvalue="200")

cb1.deselect()
cb2.deselect()
cb3.deselect()
cb4.deselect()

cb1.pack(anchor=W)
cb2.pack(anchor=W)
cb3.pack(anchor=W)
cb4.pack(anchor=W)

l1=Label(root,text="0")
l2=Label(root,text="0")
l3=Label(root,text="0")
l4=Label(root,text="0")

l1.pack()
l2.pack()
l3.pack()
l4.pack()

mainloop()