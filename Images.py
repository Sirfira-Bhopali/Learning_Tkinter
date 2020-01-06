from tkinter import *
from PIL import ImageTk,Image

frame=Tk()

img=ImageTk.PhotoImage(Image.open("C:/Users/HP/Desktop/pic image tkinter/AirBrush_20180621184412.jpg"))
label=Label(frame,image=img)
label.pack()

b1=Button(frame,text="quit",command=frame.quit)
b1.pack()


mainloop()