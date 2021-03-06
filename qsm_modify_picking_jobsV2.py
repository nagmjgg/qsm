"""
https://www.youtube.com/watch?v=i4qLI9lmkqw

Programa con marcos  y formulario con consulta a base de datos

#grids
https://pythonguides.com/python-tkinter-grid/

V2 Stable using Postgresql database

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

def clear():
    query = "select pick_id, creation_date, deliver_date, creation_time, job_number, product_name, received_by, delivered_by, delivered_flag, moved_flag, returned_flag, return_date, comments from picking_job"
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
    t8.set(item['values'][7])
    t9.set(item['values'][8])
    t10.set(item['values'][9])
    t11.set(item['values'][10])
    t12.set(item['values'][11])
    t13.set(item['values'][12])

def update_element():
    pick_id = t1.get()
    creation_date = t2.get()
    deliver_date = t3.get()
    creation_time = t4.get()
    job_number = t5.get()
    product_name = t6.get()
    received_by = t7.get()
    delivered_by = t8.get()
    delivered_flag = t9.get()
    moved_flag = t10.get()
    returned_flag = t11.get()
    return_date = t12.get()
    comments = t13.get()

    if messagebox.askyesno("confirm ?","Are you sure you want to update this element?"):
        query = "update pick_id = %s, creation_date = %s, deliver_date = %s, creation_time = %s, job_number = %s, " \
                "product_name = %s, received_by = %s, delivered_by = %s, delivered_flag = %s, moved_flag = %s, " \
                "returned_flag = %s, return_date = %s, comments = %s where pick_id = %s"
        cursor.execute(query, (pick_id, creation_date, deliver_date, creation_time, job_number, product_name,
                               received_by, delivered_by, delivered_flag, moved_flag, returned_flag, return_date,
                               comments))
        conn.commit()
        clear()
    else:
        return True

def add_new_element():
    pick_id = t1.get()
    creation_date = t2.get()
    deliver_date = t3.get()
    creation_time = t4.get()
    job_number = t5.get()
    product_name = t6.get()
    received_by = t7.get()
    delivered_by = t8.get()
    delivered_flag = t9.get()
    moved_flag = t10.get()
    returned_flag = t11.get()
    return_date = t12.get()
    comments = t13.get()

    query2 = "select max(index) from picking_data"
    cursor.execute(query2,(pick_id))
    max_index = cursor.fetchone()
    print(max_index)

    new_index = int(max_index[0]) + 1
    print(new_index)

    query = "insert into picking_data (pick_id, creation_date, deliver_date, creation_time, job_number, " \
            "product_name, received_by, delivered_by, delivered_flag, moved_flag, returned_flag, return_date, " \
            "comments) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    cursor.execute(query, (pick_id, creation_date, deliver_date, creation_time, job_number, product_name,
                           received_by, delivered_by, delivered_flag, moved_flag, returned_flag, return_date, comments))
    conn.commit()
    clear()

def delete_element():
    pick_id = t1.get()

    if messagebox.askyesno("confirm Delete ?","Are you sure you want to delete this element?"):
        query = "delete from picking_data where pick_id = " + pick_id + " and part_number = '" + part_number + "'"
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
    query = "select pick_id, creation_date, deliver_date, creation_time, job_number, product_name, received_by, " \
            "delivered_by, delivered_flag, moved_flag, returned_flag, return_date, comments from picking_job where " \
            "pick_id = '"+q2.upper()+"' or job_number like '%"+q2+"%'"
    cursor.execute(query)
    rows = cursor.fetchall()
    update(rows)



root = Tk()
q = StringVar()
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar()
t5 = StringVar()
t6 = StringVar()
t7 = StringVar()
t8 = StringVar()
t9 = StringVar()
t10 = StringVar()
t11 = StringVar()
t12 = StringVar()
t13 = StringVar()

wrapper1 = LabelFrame(root, text="Database")
wrapper2 = LabelFrame(root, text="Search")
wrapper3 = LabelFrame(root, text="Selection")

wrapper1.pack(fill="both", expand="yes", padx=10, pady=10)
wrapper2.pack(fill="both", expand="yes", padx=10, pady=10)
wrapper3.pack(fill="both", expand="yes", padx=10, pady=10)

trv = ttk.Treeview(wrapper1, columns=(1,2,3,4,5,6,7,8,9,10,11,12,13), show="headings", height="5")

verscrlbar = ttk.Scrollbar(wrapper1, orient="vertical", command=trv.yview)
verscrlbar.pack(side="right", fill="y")
trv['yscrollcommand']=verscrlbar.set


horscrlbar = ttk.Scrollbar(wrapper1, orient="horizontal", command=trv.xview)
horscrlbar.pack(side="bottom", fill="x")
trv['xscrollcommand']=horscrlbar.set


fields = ['pick_id', 'creation_date', 'deliver_date', 'creation_time', 'job_number', 'product_name', 'received_by',
          'delivered_by', 'delivered_flag', 'moved_flag', 'returned_flag', 'return_date', 'comments']

#columns width
trv.column(1,width=50)
trv.column(2,width=80)
trv.column(3,width=280)
trv.column(4,width=200)
trv.column(5,width=100)
trv.column(6,width=200)
trv.column(7,width=50)
trv.column(8,width=80)
trv.column(9,width=280)
trv.column(10,width=200)
trv.column(11,width=100)
trv.column(12,width=200)
trv.column(13,width=200)
trv.pack()
#index, 'part_number','location','expiration','qty', 'lot'
trv.heading(1, text="pick_id")
trv.heading(2, text="creation_date")
trv.heading(3, text="deliver_date")
trv.heading(4, text="creation_time")
trv.heading(5, text="job_number")
trv.heading(6, text="product_name")
trv.heading(7, text="received_by")
trv.heading(8, text="delivered_by")
trv.heading(9, text="delivered_flag")
trv.heading(10, text="moved_flag")
trv.heading(11, text="returned_flag")
trv.heading(12, text="return_date")
trv.heading(13, text="comments")



trv.bind('<Double 1>', getrow)

query = "select pick_id, part_number, part_description, location, qty, part_lot from picking_data"
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
lbl0 = Label(wrapper3, text="pick_id")
lbl0.grid(row=0, column=0, padx=5, pady=3)
ent0 = Entry(wrapper3, textvariable=t1)
ent0.grid(row=0, column=1, padx=5, pady=3, sticky='w')

lbl1 = Label(wrapper3, text="Part number")
lbl1.grid(row=1, column=0, padx=5, pady=3)
ent1 = Entry(wrapper3, textvariable=t2)
ent1.grid(row=1, column=1, padx=5, pady=3, sticky='w')

lbl2 = Label(wrapper3, text="Description")
lbl2.grid(row=2, column=0, padx=5, pady=3)
ent2 = Entry(wrapper3, textvariable=t3)
ent2.grid(row=2, column=1, padx=5, pady=3, ipadx=150, sticky='w')

lbl3 = Label(wrapper3, text="Location")
lbl3.grid(row=3, column=0, padx=5, pady=3)
ent3 = Entry(wrapper3, textvariable=t4)
ent3.grid(row=3, column=1, padx=5, pady=3, sticky='w')

lbl4 = Label(wrapper3, text="Qty")
lbl4.grid(row=4, column=0, padx=5, pady=3)
ent4 = Entry(wrapper3, textvariable=t5)
ent4.grid(row=4, column=1, padx=5, pady=3, sticky='w')

up_btn = Button(wrapper3, text="Update", command=update_element)
add_btn = Button(wrapper3, text="Add New", command=add_new_element)
delete_btn = Button(wrapper3, text="Delete", command=delete_element)

add_btn.grid(row=5, column=0, padx=5, pady=3)
up_btn.grid(row=5, column=1, padx=5, pady=3)
delete_btn.grid(row=5, column=2, padx=5, pady=3)


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
root.title("QSM Modify Picking Jobs")
root.geometry("1080x720")
root.mainloop()

