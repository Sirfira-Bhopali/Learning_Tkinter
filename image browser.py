from tkinter import *
from PIL import ImageTk,Image

frame=Tk()

img1=ImageTk.PhotoImage(Image.open("C:/Users/HP/Desktop/pic image tkinter/img1.jpg"))
img2=ImageTk.PhotoImage(Image.open("C:/Users/HP/Desktop/pic image tkinter/img2.jpg"))
img3=ImageTk.PhotoImage(Image.open("C:/Users/HP/Desktop/pic image tkinter/img3.jpg"))
img4=ImageTk.PhotoImage(Image.open("C:/Users/HP/Desktop/pic image tkinter/img4.jpg"))
img5=ImageTk.PhotoImage(Image.open("C:/Users/HP/Desktop/pic image tkinter/img5.jpg"))

list1=[img1,img2,img3,img4,img5]

label=Label(image=img1)
label.grid(row=0,column=0,columnspan=3)

def forward(img_num):
    if img_num<4:
        global label
        label.grid_forget()
        label=Label(image=list1[img_num+1])
        label.grid(row=0,column=0,columnspan=3)
        img_num+=1
        b_forward=Button(frame,text=">>",command=lambda: forward(img_num))
        b_forward.grid(row=1,column=2)
        b_backward = Button(frame, text="<<", command=lambda: backward(img_num))
        b_backward.grid(row=1, column=0)

    if img_num==4:
        b_forward=Button(frame,text=">>",state=DISABLED)
        b_forward.grid(row=1,column=2)

def backward(img_num):
    if img_num >0 and img_num<5:
        global label
        label.grid_forget()
        label=Label(frame,image=list1[img_num-1])
        label.grid(row=0,column=0,columnspan=3)
        img_num-=1
        b_forward = Button(frame, text=">>", command=lambda: forward(img_num))
        b_forward.grid(row=1, column=2)
        b_backward = Button(frame, text="<<", command=lambda: backward(img_num))
        b_backward.grid(row=1, column=0)

    if img_num==0:
        b_backward = Button(frame, text="<<",state=DISABLED)
        b_backward.grid(row=1, column=0)


b_backward=Button(frame,text="<<",command=lambda:backward(0),state=DISABLED)
b_exit=Button(frame,text="exit",command=frame.quit)
b_forward=Button(frame,text=">>",command=lambda: forward(0))

b_backward.grid(row=1,column=0)
b_exit.grid(row=1,column=1)
b_forward.grid(row=1,column=2)

mainloop()