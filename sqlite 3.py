import sqlite3
from tkinter import *

root=Tk()

def submit():
    # establish a connection with sqlite 3 database if present else creates a database
    conn=sqlite3.connect("address_book.db")

    # creating a cursor object to execute commands
    c=conn.cursor()

    # creating a table in database
    # c.execute("""create table address_book03 (
    # f_name varchar,
    # l_name varchar,
    # city varchar,
    # zipcode int
    # )
    # """)

    c.execute("insert into address_book03 (f_name,l_name,city,zipcode) values (:f_name,:l_name,:city,:zipcode)",
    {'f_name':f_name.get(),
    'l_name':l_name.get(),
    'city':city.get(),
    'zipcode':zipcode.get()
    }
    )
    conn.commit()
    conn.close()

    f_name.delete(0, END)
    l_name.delete(0, END)
    city.delete(0, END)
    zipcode.delete(0, END)

def show():
    conn = sqlite3.connect("address_book.db")
    c=conn.cursor()
    c.execute("select *,OID from address_book03")
    records=c.fetchall()

    print_record=""

    for record in records:
        print_record +=str(record)+"\n"

    display=Label(root,text=print_record)
    display.grid(row=6,column=0,columnspan=2)


    conn.commit()
    conn.close()

f_name_l=Label(root,text="First Name")
l_name_l=Label(root,text="Last Name")
city_l=Label(root,text="City")
zipcode_l=Label(root,text="Zipcode")

f_name_l.grid(row=0,column=0)
l_name_l.grid(row=1,column=0)
city_l.grid(row=2,column=0)
zipcode_l.grid(row=3,column=0)

f_name=Entry(root)
l_name=Entry(root)
city=Entry(root)
zipcode=Entry(root)

f_name.grid(row=0,column=1)
l_name.grid(row=1,column=1)
city.grid(row=2,column=1)
zipcode.grid(row=3,column=1)

submit_button=Button(root,text="Click here to Submit",command=submit)
submit_button.grid(row=4,column=0,columnspan=2)

show_button=Button(root,text="Show Inserted Values",command=show)
show_button.grid(row=5,column=0,columnspan=2)

mainloop()