from tkinter import *
root=Tk()

slider=Scale(root,from_=0,to=400)
slider.grid(row=0,column=1)

slider=Scale(root,from_=0,to=400,orient=HORIZONTAL)
slider.grid(row=1,column=0)

mainloop()