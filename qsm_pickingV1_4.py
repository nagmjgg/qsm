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
    t1_sel_data.set(item['values'][0])
    t2_sel_data.set(item['values'][1])
    t3_sel_data.set(item['values'][2])
    t4_sel_data.set(item['values'][3])
    t5_sel_data.set(item['values'][4])
    t6_sel_data.set(item['values'][5])
    t7_sel_data.set(item['values'][6])

def update_element():
    index = t1_sel_data.get()
    part_number = t2_sel_data.get()
    description = t3_sel_data.get()
    location = t4_sel_data.get()
    qty = t5_sel_data.get()
    lot = t6_sel_data.get()
    expiration = t7_sel_data.get()

    if messagebox.askyesno("confirm ?","Are you sure you want to update this element?"):
        query = "update onhand_ingredients set index = %s, part_number = %s, description_x = %s, location = %s, " \
                "qty = %s, lot = %s, expiration = %s where  index = %s"
        cursor.execute(query, (index, part_number, description, location, qty, lot, expiration, index))
        conn.commit()
        clear()
    else:
        return True

def add_new_element():
    index = t1_sel_data.get()
    part_number = t2_sel_data.get()
    description = t3_sel_data.get()
    location = t4_sel_data.get()
    qty = t5_sel_data.get()
    lot = t6_sel_data.get()
    expiration = t7_sel_data.get()

    query = "insert into onhand_ingredients (index, part_number, description_x, location, qty, lot, expiration) values(%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (index, part_number, description, location, qty, lot, expiration))
    conn.commit()
    clear()

def delete_element():
    ingredient_id = t1_sel_data.get()
    if messagebox.askyesno("confirm Delete ?","Are you sure you want to delete this customer?"):
        query = "select index, part_number, description_x, location, qty, lot, expiration from onhand_ingredients"
        cursor.execute(query)
        conn.commit()
        clear()
    else:
        return True

def update(rows):
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert('','end', values=i)

def search():
    q2 = q.get()
    query = "select index, part_number, description_x, location, qty, lot, expiration from onhand_ingredients where part_number like '%"+q2.upper()+"%' or description_x like '%"+q2+"%'"
    cursor.execute(query)
    rows = cursor.fetchall()
    update(rows)

def pick_element():

    pick_id = t1_job_data.get()
    creation_date = t1_job_data.get()
    deliver_date = t1_job_data.get()
    time = t1_job_data.get()
    job_number = t1_job_data.get()
    product_name = t1_job_data.get()
    received_by = t1_job_data.get()
    delivered_by = t1_job_data.get()
    delivered_flag = t1_job_data.get()
    moved_flag = t1_job_data.get()
    returned_flag = t1_job_data.get()
    return_date = t1_job_data.get()
    comments = t1_job_data.get()
    pick_id = t1_job_data.get()
    part_number = t2_sel_data.get()
    part_description = t3_sel_data.get()
    location = t4_sel_data.get()
    qty = t5_sel_data.get()
    part_lot = t6_sel_data.get()
    part_expiration = t7_sel_data()


    query = "update picking_data set pick_id = %s, creation_date = %s, deliver_date = %s, time = %s, job_number = %s, " \
            "product_name = %s, received_by = %s, delivered_by = %s, delivered_flag = %s, moved_flag = %s, " \
            "returned_flag = %s, return_date = %s, comments = %s, location = %s, part_number = %s, " \
            "part_description = %s, part_lot = %s, expiration = %s, qty = %s, unit = %s, amount = %s, adjust = %s, " \
            "qty_returned = %s"

    cursor.execute(query, (pick_id, creation_date, deliver_date, time, job_number, product_name, received_by,
                           delivered_by, delivered_flag, moved_flag,  returned_flag, return_date,  comments,
                           part_number, part_description, location, qty, part_lot, part_expiration))
    conn.commit()
    clear()


root = Tk()

PADX = 2
PADY = 2

wrapper0 = LabelFrame(root, text="Job Data")
wrapper1 = LabelFrame(root, text="Database")
wrapper2 = LabelFrame(root, text="Search")
wrapper3 = LabelFrame(root, text="Selection")
wrapper4 = LabelFrame(root, text="Pick")

wrapper0.pack(fill="both", expand="yes", padx=3, pady=3)
wrapper1.pack(fill="both", expand="yes", padx=3, pady=3)
wrapper2.pack(fill="both", expand="yes", padx=3, pady=3)
wrapper3.pack(fill="both", expand="yes", padx=3, pady=3)
wrapper4.pack(fill="both", expand="yes", padx=3, pady=3)


trv = ttk.Treeview(wrapper1, columns=(1,2,3,4,5,6,7), show="headings", height="4")
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

t1_job_data = StringVar()
t2_job_data = StringVar()
t3_job_data = StringVar()
t4_job_data = StringVar()
t5_job_data = StringVar()
t6_job_data = StringVar()
t7_job_data = StringVar()
t8_job_data = StringVar()
t9_job_data = IntVar()
t10_job_data = IntVar()
t11_job_data = IntVar()
t12_job_data = StringVar()

#job data section
lbl0_job_data = Label(wrapper0, text="Pick_id")
lbl0_job_data.grid(row=0, column=0, padx=PADX, pady=PADY)
ent0_job_data = Entry(wrapper0, textvariable=t1_job_data)
ent0_job_data.grid(row=1, column=0, padx=PADX, pady=PADY, sticky=W)

lbl1_job_data = Label(wrapper0, text="Creation_date")
lbl1_job_data.grid(row=0, column=1, padx=PADX, pady=PADY)
ent1_job_data = Entry(wrapper0, textvariable=t2_job_data)
ent1_job_data.grid(row=1, column=1, padx=PADX, pady=PADY, sticky=W)

lbl2_job_data = Label(wrapper0, text="Delivery_date")
lbl2_job_data.grid(row=0, column=2, padx=PADX, pady=PADY)
ent2_job_data = Entry(wrapper0, textvariable=t3_job_data)
ent2_job_data.grid(row=1, column=2, padx=PADX, pady=PADY, sticky=W)

lbl3_job_data = Label(wrapper0, text="Time")
lbl3_job_data.grid(row=0, column=3, padx=PADX, pady=PADY)
ent3_job_data = Entry(wrapper0, textvariable=t4_job_data)
ent3_job_data.grid(row=1, column=3, padx=PADX, pady=PADY, sticky=W)

lbl4_job_data = Label(wrapper0, text="Job Number")
lbl4_job_data.grid(row=0, column=4, padx=PADX, pady=PADY)
ent4_job_data = Entry(wrapper0, textvariable=t5_job_data)
ent4_job_data.grid(row=1, column=4, padx=PADX, pady=PADY, sticky=W)

lbl5_job_data = Label(wrapper0, text="Product Name")
lbl5_job_data.grid(row=0, column=5, padx=PADX, pady=PADY)
ent5_job_data = Entry(wrapper0, textvariable=t6_job_data)
ent5_job_data.grid(row=1, column=5, padx=PADX, pady=PADY, ipadx=100)

lbl6_job_data = Label(wrapper0, text="Received by")
lbl6_job_data.grid(row=3, column=4, padx=PADX, pady=PADY)
ent6_job_data = Entry(wrapper0, textvariable=t7_job_data)
ent6_job_data.grid(row=3, column=5, padx=PADX, pady=PADY, ipadx=100)

lbl7_job_data = Label(wrapper0, text="Delivered by")
lbl7_job_data.grid(row=4, column=4, padx=PADX, pady=PADY)
ent7_job_data = Entry(wrapper0, textvariable=t8_job_data)
ent7_job_data.grid(row=4, column=5, padx=PADX, pady=PADY, ipadx=100)

lbl8_job_data = Label(wrapper0, text="Comments")
lbl8_job_data.grid(row=5, column=4, padx=PADX, pady=PADY)
ent8_job_data = Entry(wrapper0, textvariable=t9_job_data)
ent8_job_data.grid(row=5, column=5, padx=PADX, pady=PADY, ipadx=100)

ent9_job_data = Checkbutton(wrapper0, text="Delivered ?", variable=t9_job_data)
ent9_job_data.grid(row=3, column=0, padx=PADX, pady=PADY, sticky=W)

ent10_job_data = Checkbutton(wrapper0, text="Moved in FB ?", variable=t10_job_data)
ent10_job_data.grid(row=4, column=0, padx=PADX, pady=PADY, sticky=W)

ent11_job_data = Checkbutton(wrapper0, text="Returned ?", variable=t11_job_data)
ent11_job_data.grid(row=5, column=0, padx=PADX, pady=PADY, sticky=W)

lbl8_job_data = Label(wrapper0, text="Return date")
lbl8_job_data.grid(row=5, column=1, padx=PADX, pady=PADY)
ent8_job_data = Entry(wrapper0, textvariable=t12_job_data)
ent8_job_data.grid(row=5, column=2, padx=PADX, pady=PADY)


#search section
q = StringVar()

lbl = Label(wrapper2, text="Search")
lbl.pack(side=tk.LEFT, padx=PADX)
ent = Entry(wrapper2, textvariable=q)
ent.pack(side=tk.LEFT, padx=PADX)
btn = Button(wrapper2, text="Search", command=search)
btn.pack(side=tk.LEFT, padx=PADX)
cbtn = Button(wrapper2, text="Clear", command=clear)
cbtn.pack(side=tk.LEFT, padx=PADX)


#user data selection
"""
    index = t1.get()
    part_number = t2.get()
    description = t3.get()
    location = t4.get()
    qty = t5.get()
    lot = t6.get()
    expiration = t7.get()
"""
t1_sel_data = StringVar()
t2_sel_data = StringVar()
t3_sel_data = StringVar()
t4_sel_data = StringVar()
t5_sel_data = StringVar()
t6_sel_data = StringVar()
t7_sel_data = StringVar()

lbl0 = Label(wrapper3, text="Index")
lbl0.grid(row=0, column=0, padx=PADX, pady=PADY, ipadx=2)
ent0 = Entry(wrapper3, textvariable=t1_sel_data)
ent0.grid(row=1, column=0, padx=PADX, pady=PADY, sticky=W)

lbl1 = Label(wrapper3, text="Part number")
lbl1.grid(row=0, column=1,padx=PADX, pady=PADY)
ent1 = Entry(wrapper3, textvariable=t2_sel_data)
ent1.grid(row=1, column=1, padx=PADX, pady=PADY, sticky=W)

lbl2 = Label(wrapper3, text="Description")
lbl2.grid(row=0, column=2, padx=PADX, pady=PADY)
ent2 = Entry(wrapper3, textvariable=t3_sel_data)
ent2.grid(row=1, column=2, padx=PADX, pady=PADY, ipadx=120, sticky=W)

lbl3 = Label(wrapper3, text="Location")
lbl3.grid(row=0, column=3, padx=PADX, pady=PADY)
ent3 = Entry(wrapper3, textvariable=t4_sel_data)
ent3.grid(row=1, column=3, padx=PADX, pady=PADY, ipadx=50, sticky=W)

lbl4 = Label(wrapper3, text="Qty")
lbl4.grid(row=0, column=4, padx=PADX, pady=PADY)
ent4 = Entry(wrapper3, textvariable=t5_sel_data)
ent4.grid(row=1, column=4, padx=PADX, pady=PADY, sticky=W)

lbl5 = Label(wrapper3, text="Lot")
lbl5.grid(row=2, column=3, padx=PADX, pady=PADY)
ent5 = Entry(wrapper3, textvariable=t6_sel_data)
ent5.grid(row=3, column=3, padx=PADX, pady=PADY, ipadx=50, sticky=W)

lbl6 = Label(wrapper3, text="Expiration")
lbl6.grid(row=2, column=4, padx=PADX, pady=PADY)
ent6 = Entry(wrapper3, textvariable=t7_sel_data)
ent6.grid(row=3, column=4, padx=PADX, pady=PADY, sticky=W)


up_btn = Button(wrapper3, text="Update", command=update_element)
add_btn = Button(wrapper3, text="Add New", command=add_new_element)
delete_btn = Button(wrapper3, text="Delete", command=delete_element)
pick_btn = Button(wrapper3, text="Pick", command=pick_element)

add_btn.grid(row=5, column=0, padx=5, pady=3, sticky=W)
up_btn.grid(row=5, column=1, padx=5, pady=3, sticky=W)
delete_btn.grid(row=5, column=2, padx=5, pady=3, sticky=W)
pick_btn.grid(row=5, column=3, padx=5, pady=3, sticky=W)


"""
style = Style(master)
style.configure("TRadiobutton", background = "light green",
                foreground = "red", font = ("arial", 10, "bold"))
"""

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

