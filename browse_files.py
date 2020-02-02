from tkinter import *
from tkinter import filedialog

root=Tk()

label_dir=Label(root,text="")
label_dir.grid(row=1,column=0,columnspan=3)

def browse():
    global label_dir
    label_dir.grid_forget()
    browse=filedialog.askopenfilenames(initialdir="c:\\Users\HP\Desktop\pic image tkinter",title="Please Select a File",filetypes=(("jpg files","*.jpg"),("All Files","*.*")))
    label_dir=Label(root,text=browse)
    label_dir.grid(row=1,column=0,columnspan=3)


button_browse=Button(root,text="click here to select files",command=browse)
button_browse.grid(row=0,column=0)

mainloop()