from tkinter import *

root=Tk()

options=["1","2","3","4","5","6","7","8","9"]

option=StringVar()
option.set(options[0])

dd=OptionMenu(root,option,*options)
dd.pack()

mainloop()