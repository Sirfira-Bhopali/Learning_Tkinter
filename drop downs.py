<<<<<<< HEAD
from tkinter import *

root=Tk()

options=["1","2","3","4","5","6","7","8","9"]

option=StringVar()
option.set(options[0])

dd=OptionMenu(root,option,*options)
dd.pack()

=======
from tkinter import *

root=Tk()

options=["1","2","3","4","5","6","7","8","9"]

option=StringVar()
option.set(options[0])

dd=OptionMenu(root,option,*options)
dd.pack()

>>>>>>> d58411fc1358ab69c34a05a5a12f4d3f9e5498d0
mainloop()