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
import datetime
import os
import pandas as pd
from pandastable import Table
import psycopg2
import glob    #func last_filename
from functions import *
from datetime import *

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
    index_sel.set(item['values'][0])  #index
    part_number_sel.set(item['values'][1])  #part_number
    description_sel.set(item['values'][2])  #description
    location_sel.set(item['values'][3])  #location
    qty_sel.set(item['values'][4])  #qty
    lot_sel.set(item['values'][5])  #lot
    expiration_sel.set(item['values'][6])  #expiration

def update_element():
    '''
    index_sel = StringVar()
    part_number_sel = StringVar()
    description_sel = StringVar()
    location_sel = StringVar()
    qty_sel = StringVar()
    lot_sel = StringVar()
    expiration_sel = StringVar()
'''
    index = index_sel.get()
    part_number = part_number_sel.get()
    description = description_sel.get()
    location = location_sel.get()
    qty = qty_sel.get()
    lot = lot_sel.get()
    expiration = expiration_sel.get()

    if messagebox.askyesno("confirm ?","Are you sure you want to update this element?"):
        query = "update onhand_ingredients set index = %s, part_number = %s, description_x = %s, location = %s, " \
                "qty = %s, lot = %s, expiration = %s where  index = %s"
        cursor.execute(query, (index, part_number, description, location, qty, lot, expiration, index))
        conn.commit()
        clear()
    else:
        return True

def add_new_element():
    index = index_sel.get()
    part_number = part_number_sel.get()
    description = description_sel.get()
    location = location_sel.get()
    qty = qty_sel.get()
    lot = lot_sel.get()
    expiration = expiration_sel.get()

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

    query = "select max(index) from picking_data"
    cursor.execute(query)
    max_id = cursor.fetchone()

    date = date_now()
    time = time_now()

    pick_id = pick_id_job.get()
    modified =  date_now()
    creation_date = creation_date_job.get()
    delivery_date = delivery_date_lbl_job.get()
    time = time_job.get()
    job_number = job_number_job.get()
    product_name = product_name_job.get()
    received_by = received_by_job.get()
    delivered_by = delivered_by_job.get()
    delivered_flag = delivered_flag_job.get()
    moved_flag = moved_flag_job.get()
    returned_flag = returned_flag_job.get()
    returned_date = returned_date_job.get()
    comments = comments_job.get()
    part_number = t2_sel_data.get()
    part_description = t3_sel_data.get()
    location = t4_sel_data.get()
    qty = t5_sel_data.get()
    #unit = t8_sel_data.get()
    #amount_each = t9_sel_data.get()
    part_lot = t6_sel_data.get()
    part_expiration = t7_sel_data.get()

    creation_date = actual_date()

    query = "insert into picking_data (pick_id, creation_date, deliver_date, time, job_number, " \
            "product_name, received_by, delivered_by, delivered_flag, moved_flag, " \
            "returned_flag, comments, location, part_number, " \
            "part_description, part_lot, expiration, qty) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,  %s, %s,  %s, %s, %s, %s, %s, %s)"

    cursor.execute(query,(pick_id, creation_date, deliver_date, time, job_number, product_name, received_by,
                          delivered_by, delivered_flag, moved_flag,  returned_flag, comments, location, part_number,
                          part_description, part_lot, part_expiration, qty))
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

pick_id_job = StringVar()
modified = StringVar()
creation_date_job = StringVar()
delivery_date_job = StringVar()
time_job = StringVar()
job_number_job = StringVar()
product_name_job = StringVar()
received_by_job = StringVar()
delivered_by_job = StringVar()
delivered_flag_job = StringVar()
comments_job = IntVar()
moved_flag_job = IntVar()
returned_flag_job = IntVar()
returned_date_job = StringVar()

#job data section
pick_id_lbl_job = Label(wrapper0, text="Pick_id")
pick_id_lbl_job.grid(row=0, column=0, padx=PADX, pady=PADY)
pick_id_ent_job = Entry(wrapper0, textvariable=pick_id_job)
pick_id_ent_job.grid(row=1, column=0, padx=PADX, pady=PADY, sticky=W)

creation_date_lbl_job = Label(wrapper0, text="Creation_date")
creation_date_lbl_job.grid(row=0, column=1, padx=PADX, pady=PADY)
creation_date_ent_job = Entry(wrapper0, textvariable=creation_date_job)
creation_date_ent_job.grid(row=1, column=1, padx=PADX, pady=PADY, sticky=W)

delivery_date_lbl_job = Label(wrapper0, text="Delivery_date")
delivery_date_lbl_job.grid(row=0, column=2, padx=PADX, pady=PADY)
delivery_date_ent_job = Entry(wrapper0, textvariable=delivery_date_job)
delivery_date_ent_job.grid(row=1, column=2, padx=PADX, pady=PADY, sticky=W)

time_lbl_job = Label(wrapper0, text="Time")
time_lbl_job.grid(row=0, column=3, padx=PADX, pady=PADY)
time_ent_job = Entry(wrapper0, textvariable=time_job)
time_ent_job.grid(row=1, column=3, padx=PADX, pady=PADY, sticky=W)

job_number_lbl_job = Label(wrapper0, text="Job Number")
job_number_lbl_job.grid(row=0, column=4, padx=PADX, pady=PADY)
job_number_ent_job = Entry(wrapper0, textvariable=job_number_job)
job_number_ent_job.grid(row=1, column=4, padx=PADX, pady=PADY, sticky=W)

product_name_lbl_job = Label(wrapper0, text="Product Name")
product_name_lbl_job.grid(row=0, column=5, padx=PADX, pady=PADY)
product_name_ent_job = Entry(wrapper0, textvariable=product_name_job)
product_name_ent_job.grid(row=1, column=5, padx=PADX, pady=PADY, ipadx=100)

received_by_lbl_job = Label(wrapper0, text="Received by")
received_by_lbl_job.grid(row=3, column=4, padx=PADX, pady=PADY)
received_by_ent_job = Entry(wrapper0, textvariable=received_by_job)
received_by_ent_job.grid(row=3, column=5, padx=PADX, pady=PADY, ipadx=100)

delivered_by_lbl_job = Label(wrapper0, text="Delivered by")
delivered_by_lbl_job.grid(row=4, column=4, padx=PADX, pady=PADY)
delivered_by_ent_job = Entry(wrapper0, textvariable=delivered_by_job)
delivered_by_ent_job.grid(row=4, column=5, padx=PADX, pady=PADY, ipadx=100)

comments_lbl_job = Label(wrapper0, text="Comments")
comments_lbl_job.grid(row=5, column=4, padx=PADX, pady=PADY)
comments_ent_job = Entry(wrapper0, textvariable=comments_job)
comments_ent_job.grid(row=5, column=5, padx=PADX, pady=PADY, ipadx=100)

delivered_flag_ent_job = Checkbutton(wrapper0, text="Delivered ?", variable=delivered_flag_job)
delivered_flag_ent_job.grid(row=3, column=0, padx=PADX, pady=PADY, sticky=W)

moved_flag_ent_job = Checkbutton(wrapper0, text="Moved in FB ?", variable=moved_flag_job)
moved_flag_ent_job.grid(row=4, column=0, padx=PADX, pady=PADY, sticky=W)

returned_flag_ent_job = Checkbutton(wrapper0, text="Returned ?", variable=returned_flag_job)
returned_flag_ent_job.grid(row=5, column=0, padx=PADX, pady=PADY, sticky=W)

return_date_lbl_job = Label(wrapper0, text="Return date")
return_date_lbl_job.grid(row=5, column=1, padx=PADX, pady=PADY)
return_date_ent_job = Entry(wrapper0, textvariable=returned_date_job)
return_date_ent_job.grid(row=5, column=2, padx=PADX, pady=PADY)


#search section
q = StringVar()

search_lbl = Label(wrapper2, text="Search")
search_lbl.pack(side=tk.LEFT, padx=PADX)
search_ent = Entry(wrapper2, textvariable=q)
search_ent.pack(side=tk.LEFT, padx=PADX)
search_btn = Button(wrapper2, text="Search", command=search)
search_btn.pack(side=tk.LEFT, padx=PADX)
clear_btn = Button(wrapper2, text="Clear", command=clear)
clear_btn.pack(side=tk.LEFT, padx=PADX)


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
index_sel = StringVar()
part_number_sel = StringVar()
description_sel = StringVar()
location_sel = StringVar()
qty_sel = StringVar()
lot_sel = StringVar()
expiration_sel = StringVar()

index_lbl = Label(wrapper3, text="Index")
index_lbl.grid(row=0, column=0, padx=PADX, pady=PADY, ipadx=2)
index_ent = Entry(wrapper3, textvariable=index_sel)
index_ent.grid(row=1, column=0, padx=PADX, pady=PADY, sticky=W)

part_number_lbl = Label(wrapper3, text="Part number")
part_number_lbl.grid(row=0, column=1,padx=PADX, pady=PADY)
part_number_ent = Entry(wrapper3, textvariable=part_number_sel)
part_number_ent.grid(row=1, column=1, padx=PADX, pady=PADY, sticky=W)

description_lbl = Label(wrapper3, text="Description")
description_lbl.grid(row=0, column=2, padx=PADX, pady=PADY)
description_ent = Entry(wrapper3, textvariable=description_sel)
description_ent.grid(row=1, column=2, padx=PADX, pady=PADY, ipadx=120, sticky=W)

location_lbl = Label(wrapper3, text="Location")
location_lbl.grid(row=0, column=3, padx=PADX, pady=PADY)
location_ent = Entry(wrapper3, textvariable=location_sel)
location_ent.grid(row=1, column=3, padx=PADX, pady=PADY, ipadx=50, sticky=W)

qty_lbl = Label(wrapper3, text="Qty")
qty_lbl.grid(row=0, column=4, padx=PADX, pady=PADY)
qty_ent = Entry(wrapper3, textvariable=qty_sel)
qty_ent.grid(row=1, column=4, padx=PADX, pady=PADY, sticky=W)

lot_lbl = Label(wrapper3, text="Lot")
lot_lbl.grid(row=2, column=3, padx=PADX, pady=PADY)
lot_ent = Entry(wrapper3, textvariable=lot_sel)
lot_ent.grid(row=3, column=3, padx=PADX, pady=PADY, ipadx=50, sticky=W)

expiration_lbl = Label(wrapper3, text="Expiration")
expiration_lbl.grid(row=2, column=4, padx=PADX, pady=PADY)
expiration_ent = Entry(wrapper3, textvariable=expiration_sel)
expiration_ent.grid(row=3, column=4, padx=PADX, pady=PADY, sticky=W)


update_btn = Button(wrapper3, text="Update", command=update_element)
add_btn = Button(wrapper3, text="Add New", command=add_new_element)
delete_btn = Button(wrapper3, text="Delete", command=delete_element)
pick_btn = Button(wrapper3, text="Pick", command=pick_element)

add_btn.grid(row=5, column=0, padx=5, pady=3, sticky=W)
update_btn.grid(row=5, column=1, padx=5, pady=3, sticky=W)
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

