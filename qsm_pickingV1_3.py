"""
https://www.youtube.com/watch?v=i4qLI9lmkqw

Programa con marcos  y formulario con consulta a base de datos

#grids
https://pythonguides.com/python-tkinter-grid/

"""

import psycopg2
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
import pandas as pd
from pandastable import Table
import psycopg2
import glob    #func last_filename

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.colheader_justify', 'center')
pd.set_option('display.precision', 3)

#https://www.tutorialspoint.com/python_data_access/python_mysql_create_table.htm
db_name="qsm"
username='postgres'
user_password='Quality01'
db_host='127.0.0.1'
db_port= '5432'

#establishing the connection
conn = psycopg2.connect(database=db_name, user=username, password=user_password, host=db_host, port= db_port)

#Creating a cursor object using the cursor() method
cursor = conn.cursor()



"""
#establishing the connection
conn = psycopg2.connect(database=db_name, user=username, password=user_password, host=db_host, port= db_port)

#Creating a cursor object using the cursor() method
cursor = conn.cursor()
"""

def clear():
    query = "select index, part_number, description_x, location, qty, lot, expiration from onhand_ingredients"
    cursor.execute(query)
    rows = cursor.fetchall()
    update(rows)

def getrow(event):
    rowid = trv.identify_row(event.y)
    item = trv.item(trv.focus())
    t1.set(item['values'][0])
    t2.set(item['values'][1])
    t3.set(item['values'][2])
    t4.set(item['values'][3])
    t5.set(item['values'][4])
    t6.set(item['values'][5])
    t7.set(item['values'][6])

def update_element():
    index = t1.get()
    part_number = t2.get()
    description = t3.get()
    location = t4.get()
    qty = t5.get()
    lot = t6.get()
    expiration = t7.get()

    if messagebox.askyesno("confirm ?","Are you sure you want to update this element?"):
        query = "update onhand_ingredients set index = %s, part_number = %s, description_x = %s, location = %s, " \
                "qty = %s, lot = %s, expiration = %s where  index = %s"
        cursor.execute(query, (index, part_number, description, location, qty, lot, expiration, index))
        conn.commit()
        clear()
    else:
        return True

def add_new_element():
    index = t1.get()
    part_number = t2.get()
    description = t3.get()
    location = t4.get()
    qty = t5.get()
    lot = t6.get()
    expiration = t7.get()

    query = "insert into onhand_ingredients (index, part_number, description_x, location, qty, lot, expiration) values(%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (index, part_number, description, location, qty, lot, expiration))
    conn.commit()
    clear()

def delete_element():
    ingredient_id = t1.get()
    if messagebox.askyesno("confirm Delete ?","Are you sure you want to delete this customer?"):
        query = "select index, part_number, description_x, location, qty, lot, expiration from onhand_ingredients"
        cursor.execute(query)
        conn.commit()
        clear()
    else:
        return true

def update(rows):
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert('','end', values=i)

def search():
    q2 = q.get()
    query = "select index, part_number, description_x, location, qty, lot, expiration from onhand_ingredients where part_number like '%"+q2+"%' or description_x like '%"+q2+"%'"
    cursor.execute(query)
    rows = cursor.fetchall()
    update(rows)

def pick_element():
    index = t1.get()
    part_number = t2.get()
    description = t3.get()
    location = t4.get()
    qty = t5.get()
    lot = t6.get()

    query = "update onhand_ingredients set index = %s, part_number = %s, description_x = %s, location = %s, " \
            "qty = %s, lot = %s where  index = %s"
    cursor.execute(query, (index, part_number, description, location, qty, lot, index))
    conn.commit()
    clear()


root = Tk()
q = StringVar()
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar()
t5 = StringVar()
t6 = StringVar()
t7 = StringVar()

t11 = StringVar()

wrapper0 = LabelFrame(root, text="Job Data")
wrapper1 = LabelFrame(root, text="Database")
wrapper2 = LabelFrame(root, text="Search")
wrapper3 = LabelFrame(root, text="Selection")
wrapper4 = LabelFrame(root, text="Pick")

wrapper0.pack(fill="both", expand="yes", padx=10, pady=10)
wrapper1.pack(fill="both", expand="yes", padx=10, pady=10)
wrapper2.pack(fill="both", expand="yes", padx=10, pady=10)
wrapper3.pack(fill="both", expand="yes", padx=10, pady=10)
wrapper4.pack(fill="both", expand="yes", padx=10, pady=10)


trv = ttk.Treeview(wrapper1, columns=(1,2,3,4,5,6,7), show="headings", height="8")
verscrlbar = ttk.Scrollbar(wrapper1, orient="vertical", command=trv.yview)
verscrlbar.pack(side="right", fill="y")

#columns width
trv.column(1,width=50)
trv.column(2,width=80)
trv.column(3,width=280)
trv.column(4,width=200)
trv.column(5,width=100)
trv.column(6,width=200)
trv.column(7,width=100)
trv.pack()
#index, 'part_number','location','expiration','qty', 'lot'
trv.heading(1, text="index")
trv.heading(2, text="part_number")
trv.heading(3, text="Description")
trv.heading(4, text="Location")
trv.heading(5, text="Qty")
trv.heading(6, text="Lot")
trv.heading(7, text="Expiration")

trv.bind('<Double 1>', getrow)

query = "select index, part_number, description_x, location, qty, lot, expiration from onhand_ingredients"
cursor.execute(query)
rows = cursor.fetchall()
update(rows)


# Tree View: Picking 
trv_pick = ttk.Treeview(wrapper4, columns=(1,2,3,4,5,6,7), show="headings", height="8")
verscrlbar = ttk.Scrollbar(wrapper4, orient="vertical", command=trv_pick.yview)
verscrlbar.pack(side="right", fill="y")

#columns width
trv_pick.column(1,width=50)
trv_pick.column(2,width=80)
trv_pick.column(3,width=280)
trv_pick.column(4,width=200)
trv_pick.column(5,width=100)
trv_pick.column(6,width=200)
trv_pick.column(7,width=100)
trv_pick.pack()
#index, 'part_number','location','expiration','qty', 'lot'
trv_pick.heading(1, text="index")
trv_pick.heading(2, text="part_number")
trv_pick.heading(3, text="Description")
trv_pick.heading(4, text="Location")
trv_pick.heading(5, text="Qty")
trv_pick.heading(6, text="Lot")
trv_pick.heading(7, text="Expiration")


trv_pick.bind('<Double 1>', getrow)
query = "select pick_id, location, part_number, part_description, part_lot, expiration, qty from picking_data" # where pick_id = '" + pick_id + "'"
cursor.execute(query)
rows = cursor.fetchall()
update(rows)






#search section
lbl = Label(wrapper2, text="Search")
lbl.pack(side=tk.LEFT, padx=10)
ent = Entry(wrapper2, textvariable=q)
ent.pack(side=tk.LEFT, padx=6)
btn = Button(wrapper2, text="Search", command=search)
btn.pack(side=tk.LEFT, padx=6)
cbtn = Button(wrapper2, text="Clear", command=clear)
cbtn.pack(side=tk.LEFT, padx=6)


#user data section
lbl0 = Label(wrapper3, text="Index")
lbl0.grid(row=0, column=0, padx=5, pady=3)
ent0 = Entry(wrapper3, textvariable=t1)
ent0.grid(row=0, column=1, padx=5, pady=3)

lbl1 = Label(wrapper3, text="Part number")
lbl1.grid(row=1, column=0, padx=5, pady=3)
ent1 = Entry(wrapper3, textvariable=t2)
ent1.grid(row=1, column=1, padx=5, pady=3)

lbl2 = Label(wrapper3, text="Description")
lbl2.grid(row=2, column=0, padx=5, pady=3)
ent2 = Entry(wrapper3, textvariable=t3)
ent2.grid(row=2, column=1, padx=5, pady=3)

lbl3 = Label(wrapper3, text="Location")
lbl3.grid(row=3, column=0, padx=5, pady=3)
ent3 = Entry(wrapper3, textvariable=t4)
ent3.grid(row=3, column=1, padx=5, pady=3)

lbl4 = Label(wrapper3, text="Qty")
lbl4.grid(row=4, column=0, padx=5, pady=3)
ent4 = Entry(wrapper3, textvariable=t5)
ent4.grid(row=4, column=1, padx=5, pady=3)

up_btn = Button(wrapper3, text="Update", command=update_element)
add_btn = Button(wrapper3, text="Add New", command=add_new_element)
delete_btn = Button(wrapper3, text="Delete", command=delete_element)
pick_btn = Button(wrapper3, text="Pick", command=pick_element)

add_btn.grid(row=5, column=0, padx=5, pady=3)
up_btn.grid(row=5, column=1, padx=5, pady=3)
delete_btn.grid(row=5, column=2, padx=5, pady=3)
pick_btn.grid(row=5, column=3, padx=5, pady=3)

"""
trv.bind('<Double 1>', getrow)

query = "select ..."
cursor.execute(query)
rows = cursor.fetchall()
update(rows)

#search selection
lbl = Label(wrapper2, text="search")
lbl.pack(side=tk.LEFT, padx=10)
ent = Entry(wrapper2, textvariable=q)
ent.pack(side=tk.LEFT, padx=6)
btn = Button(wrapper2, text="search", command=search)
ent.pack(side=tk.LEFT, padx=6)
cbtn = Button(wrapper2, text="clear", command=clear)
cbtn.pack(side=tk.LEFT, padx=6)
"""
root.title("QSM Picking")
root.geometry("1080x720")
root.mainloop()

