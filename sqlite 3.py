import sqlite3
from tkinter import *

root=Tk()

display=Label(root,text="")

def save():
    conn = sqlite3.connect("address_book.db")
    c = conn.cursor()

    c.execute("update address_book03 set f_name=:f_name,l_name=:l_name,city=:city,zipcode=:zipcode where OID=:OID",
              {'f_name': f_name_update.get(),
               'l_name': l_name_update.get(),
               'city': city_update.get(),
               'zipcode': zipcode_update.get(),
               'OID':selected_ID.get()
               }
              )
    conn.commit()
    conn.close()

    update_root.destroy()

def update():
    global f_name_update,l_name_update,city_update,zipcode_update,update_root
    conn = sqlite3.connect("address_book.db")
    c=conn.cursor()

    update_root=Tk()

    f_name_l = Label(update_root, text="First Name")
    l_name_l = Label(update_root, text="Last Name")
    city_l = Label(update_root, text="City")
    zipcode_l = Label(update_root, text="Zipcode")

    f_name_l.grid(row=0, column=0)
    l_name_l.grid(row=1, column=0)
    city_l.grid(row=2, column=0)
    zipcode_l.grid(row=3, column=0)

    f_name_update= Entry(update_root)
    l_name_update = Entry(update_root)
    city_update = Entry(update_root)
    zipcode_update = Entry(update_root)

    f_name_update.grid(row=0, column=1)
    l_name_update.grid(row=1, column=1)
    city_update.grid(row=2, column=1)
    zipcode_update.grid(row=3, column=1)

    update=Button(update_root,text="Click Here to Save Changes",command=save)
    update.grid(row=4,column=0,columnspan=2)

    c.execute("select *,OID from address_book03 where OID="+selected_ID.get())
    records=c.fetchall()
    for record in records:
        f_name_update.insert(0,record[0])
        l_name_update.insert(0,record[1])
        city_update.insert(0,record[2])
        zipcode_update.insert(0,record[3])
    conn.commit()
    conn.close()


def delete():
    conn=sqlite3.connect("address_book.db")
    c=conn.cursor()

    c.execute("delete from address_book03 where OID="+selected_ID.get())

    conn.commit()
    conn.close()

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
    global display
    conn = sqlite3.connect("address_book.db")
    c=conn.cursor()
    c.execute("select *,OID from address_book03")
    records=c.fetchall()

    print_record=""

    for record in records:
        print_record +=str(record)+"\n"


    display.grid_forget()
    display=Label(root,text=print_record)
    display.grid(row=8,column=0,columnspan=2)

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

select_l=Label(root,text="Enter Record ID")
select_l.grid(row=6,column=0)

selected_ID=Entry(root)
selected_ID.grid(row=6,column=1)

delete_record=Button(root,text="Delete Selected Record",command=delete)
delete_record.grid(row=7,column=0,columnspan=2)

update_record=Button(root,text="Update Selected Record",command=update)
update_record.grid(row=9,column=0,columnspan=2)

mainloop()