from tkinter import *

root=Tk()
root.geometry("150x300")
crust=[("Thin Crust",50),("Hand Tossed",80),("Classic",100)]
toppings=[("Cheese",50),("Veggies",60),("Mushroom",70),("Pepperoni",80),("Onion",100)]

pizza_crust=StringVar()
pizza_crust.set("50")
pizza_topping=StringVar()
pizza_topping.set("50")

def click():
    global label
    label.pack_forget()
    label=Label(root,text=pizza_crust.get()+" +"+pizza_topping.get())
    label.pack()


frame_crusts=LabelFrame(text="CRUSTS")
frame_crusts.pack(padx=10,pady=10)

frame_toppings=LabelFrame(text="TOPPINGS")
frame_toppings.pack(padx=10,pady=10)

for crust_type,price in crust:
    Radiobutton(frame_crusts,text=crust_type,value=price,variable=pizza_crust,command=click).pack(anchor=W)
for topping,cost in toppings:
    Radiobutton(frame_toppings,text=topping,value=cost,variable=pizza_topping,command=click).pack(anchor=W)

label=Label(root,text="50 + 50")
label.pack()


mainloop()