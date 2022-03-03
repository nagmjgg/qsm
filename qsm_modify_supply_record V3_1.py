"""
https://www.youtube.com/watch?v=i4qLI9lmkqw

Programa con marcos  y formulario con consulta a base de datos

#grids
https://pythonguides.com/python-tkinter-grid/

V2 Stable using Postgresql database
V3 New database Mysql and connection file
V3_1 Adapted to modify Supply records V3_2

"""

import psycopg2
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
import pandas as pd
from pandastable import Table
import mysql.connector
import connection_file as con_file  #file with connection data
from datetime import datetime
from tkcalendar import DateEntry    #https://pypi.org/project/tkcalendar/


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.colheader_justify', 'center')
pd.set_option('display.precision', 3)

font_columns_name = ('Arial',12,'bold') # normal or bold
font_wrap_title = ('Arial',12,'bold') # normal or bold
font_entry = ('Arial',11,'normal') # normal or bold
font_label = ('Arial',12,'bold') # normal or bold
font_button = ('Arial',11,'bold') # normal or bold
font_main_title = ('Arial',18,'bold') # normal or bold

#establishing the connection
#conn = psycopg2.connect(database=db_name, user=username, password=user_password, host=db_host, port= db_port)
conn = mysql.connector.connect(database=con_file.db_name, user=con_file.username, password=con_file.user_password,
                               host=con_file.db_host, port=con_file.db_port)


#Creating a cursor object using the cursor() method
cursor = conn.cursor()

def date_now():
    date = datetime.now().strftime("%Y-%m-%d")
    return date

def time_now():
    time = datetime.now().strftime("%H:%M:%S")
    return time

def clear():
    query = "select id, date, time, part_number, part_name, lot, qty, unit, job_lot, neceived_by, delivered_by," \
            "relocated_flag, user_id from supplies"
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
    id = t1.get()
    date = t2.get()
    time = t3.get()
    part_number = t4.get()
    part_name = t5.get()
    lot = t6.get()
    qty = t7.get()
    unit = t8.get()
    job_lot = t9.get()
    received_by = t10.get()
    delivered_by = t11.get()
    relocated_flag = t12.get()
    user_id = t13.get()



    if messagebox.askyesno("confirm ?","Are you sure you want to update this element?"):
        query = "update picking_jobs set date = %s, time = %s, part_number = %s, part_name = %s, " \
                "lot = %s, qty = %s, unit = %s, job_lot = %s, received_by = %s, " \
                "delivered_by = %s, relocated_flag = %s, user_id = %s where id = %s"

        cursor.execute(query, (date, time, part_number, part_name, lot,
                               qty, unit, job_lot, received_by, delivered_by, relocated_flag,
                               user_id, id))
        conn.commit()
        clear()
    else:
        return True

def add_new_element():
    id = t1.get()
    date = t2.get()
    time = t3.get()
    part_number = t4.get()
    part_name = t5.get()
    lot = t6.get()
    qty = t7.get()
    unit = t8.get()
    job_lot = t9.get()
    received_by = t10.get()
    delivered_by = t11.get()
    relocated_flag = t12.get()
    user_id = t13.get()

    query = "insert into supplies (date, time, part_number, part_name, lot, qty, unit, job_lot, received_by, " \
            "delivered_by,relocated_flag, user_id) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    cursor.execute(query, (date, time, part_number, part_name, lot,
                               qty, unit, job_lot, received_by, delivered_by, relocated_flag,
                               user_id))
    conn.commit()
    clear()

def delete_element():
    id = t1.get()
    part_name = t5.get()

    if messagebox.askyesno("confirm Delete ?","Are you sure you want to delete this element?"):
        query = "delete from supplies where id = " + pick_id + " and part_name = '" + part_name + "'"
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
    query = "select id, date, time, part_number, part_name, lot, qty, unit, job_lot, received_by, delivered_by," \
            "relocated_flag, user_id from supplies where id = '"+q2.upper()+"' or part_name like '%"+q2+"%'"
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
t14 = StringVar()

PADX = 3
PADY = 3

font_columns_name = ('Arial',12,'bold') # normal or bold
font_wrap_title = ('Arial',12,'bold') # normal or bold
font_entry = ('Arial',11,'normal') # normal or bold
font_label = ('Arial',12,'bold') # normal or bold
font_button = ('Arial',11,'bold') # normal or bold
font_main_title = ('Arial',18,'bold') # normal or bold

wrapper0 = LabelFrame(root, text="")
wrapper1 = LabelFrame(root, text="Database")
wrapper2 = LabelFrame(root, text="Search")
wrapper3 = LabelFrame(root, text="Selection")

wrapper0.pack(fill="both", expand="yes", padx=10, pady=10)
wrapper1.pack(fill="both", expand="yes", padx=10, pady=10)
wrapper2.pack(fill="both", expand="yes", padx=10, pady=10)
wrapper3.pack(fill="both", expand="yes", padx=10, pady=10)

trv = ttk.Treeview(wrapper1, columns=(1,2,3,4,5,6,7,8,9,10,11,12,13,14), show="headings", height="10")

title_label = Label(wrapper0, text="VIEW WAREHOUSE SUPPLY RECORD", font=font_main_title)
title_label.pack()

verscrlbar = ttk.Scrollbar(wrapper1, orient="vertical", command=trv.yview)
verscrlbar.pack(side="right", fill="y")
trv['yscrollcommand']=verscrlbar.set

horscrlbar = ttk.Scrollbar(wrapper1, orient="horizontal", command=trv.xview)
horscrlbar.pack(side="bottom", fill="x")
trv['xscrollcommand']=horscrlbar.set


#columns width
trv.column(1,width=50)
trv.column(2,width=80)
trv.column(3,width=80)
trv.column(4,width=80)
trv.column(5,width=150)
trv.column(6,width=150)
trv.column(7,width=80)
trv.column(8,width=80)
trv.column(9,width=80)
trv.column(10,width=150)
trv.column(11,width=150)
trv.column(12,width=150)
trv.column(13,width=80)

trv.pack()
#date, time, part_number, part_name, lot, qty, unit, job_lot, received_by, delivered_by,relocated_flag, user_id
trv.heading(1, text="id")
trv.heading(2, text="date")
trv.heading(3, text="time")
trv.heading(4, text="part_number")
trv.heading(5, text="part_name")
trv.heading(6, text="lot")
trv.heading(7, text="qty")
trv.heading(8, text="unit")
trv.heading(9, text="job_lot")
trv.heading(10, text="received_by")
trv.heading(11, text="delivered_by")
trv.heading(12, text="relocated_flag")
trv.heading(13, text="user_id")


trv.bind('<Double 1>', getrow)

query = "select id, date, time, part_number, part_name, lot, qty, unit, job_lot, received_by, delivered_by, " \
        "relocated_flag, user_id from supplies"

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


#***************************************
#user data section
#***************************************

#Entry state = "normal", "disabled", or "readonly"
id_lbl = Label(wrapper3, text="id")
id_lbl.grid(row=0, column=0, padx=PADX, pady=PADY, sticky=W)
id_ent = Entry(wrapper3, textvariable=t1, state="normal")
id_ent.grid(row=0, column=1, padx=PADX, pady=PADY, sticky=W)
#pick_id_ent_job.insert(END,pick_id_new)

date_lbl = Label(wrapper3, text="Date")
date_lbl.grid(row=0, column=2, padx=PADX, pady=PADY, sticky=W)
date_ent = DateEntry(wrapper3, selectmode='day', textvariable=t2, locale='en_US', date_pattern='yyyy-MM-dd')
date_ent.grid(row=0, column=3, padx=PADX, pady=PADY, sticky=W)

time_lbl = Label(wrapper3, text="Time")
time_lbl.grid(row=1, column=0, padx=PADX, pady=PADY, sticky=W)
time_ent = Entry(wrapper3, textvariable=t3)
time_ent.grid(row=1, column=1, padx=PADX,pady=PADY, sticky=W)
time_ent.insert(END, time_now())

part_number_lbl = Label(wrapper3, text="Part Number")
part_number_lbl.grid(row=2, column=0, padx=PADX, pady=PADY, sticky=W)
part_number_ent = Entry(wrapper3, textvariable=t4)              # validate='focusout')
part_number_ent.grid(row=2, column=1, padx=PADX, pady=PADY, sticky=W)

part_name_lbl = Label(wrapper3, text="Part Name")
part_name_lbl.grid(row=2, column=2, padx=PADX, pady=PADY, sticky=W)
part_name_ent = Entry(wrapper3, textvariable=t5)
part_name_ent.grid(row=2, column=3, padx=PADX, pady=PADY, ipadx=100, sticky=W)

lot_lbl_job = Label(wrapper3, text="Lot")
lot_lbl_job.grid(row=1, column=2, padx=PADX, pady=PADY, sticky=W)
lot_ent = Entry(wrapper3, textvariable=t6)
lot_ent.grid(row=1, column=3, padx=PADX, pady=PADY, ipadx=100, sticky=W)

qty_lbl = Label(wrapper3, text="Qty")
qty_lbl.grid(row=3, column=2, padx=PADX, pady=PADY, sticky=W)
qty_ent = Entry(wrapper3, textvariable=t7)
qty_ent.grid(row=3, column=3, padx=PADX, pady=PADY, ipadx=50, sticky=W)

unit_lbl = Label(wrapper3, text="Unit")
unit_lbl.grid(row=3, column=0, padx=PADX, pady=PADY, sticky=W)
unit_ent = Entry(wrapper3, textvariable=t8)
unit_ent.grid(row=3, column=1, padx=PADX, pady=PADY, ipadx=20, sticky=W)

job_lot_lbl = Label(wrapper3, text="Job Lot")
job_lot_lbl.grid(row=4, column=2, padx=PADX, pady=PADY, sticky=W)
job_lot_ent = Entry(wrapper3, textvariable=t9)
job_lot_ent.grid(row=4, column=3, padx=PADX, pady=PADY, ipadx=50, sticky=W)

relocated_flag_ent = Checkbutton(wrapper3, text="Relocated ?", variable=t12)
relocated_flag_ent.grid(row=4, column=0, padx=PADX, pady=PADY, ipadx=100, sticky=W)

received_by_lbl = Label(wrapper3, text="Received by")
received_by_lbl.grid(row=5, column=2, padx=PADX, pady=PADY, sticky=W)
received_by_ent = Entry(wrapper3, textvariable=t10)
received_by_ent.grid(row=5, column=3, padx=PADX, pady=PADY, ipadx=100, sticky=W)

delivered_by_lbl = Label(wrapper3, text="Delivered by")
delivered_by_lbl.grid(row=6, column=2, padx=PADX, pady=PADY, sticky=W)
delivered_by_ent = Entry(wrapper3, textvariable=t11)
delivered_by_ent.grid(row=6, column=3, padx=PADX, pady=PADY, ipadx=100, sticky=W)

user_id_lbl = Label(wrapper3, text="User id")
user_id_lbl.grid(row=4, column=0, padx=PADX, pady=PADY, sticky=W)
user_id_ent = Entry(wrapper3, textvariable=t13)
user_id_ent.grid(row=4, column=1, padx=PADX, pady=PADY, ipadx=50, sticky=W)

save_pick_job_btn = Button(wrapper3, text="Update", command=update_element)
save_pick_job_btn.grid(row=1, column=7, padx=PADX, pady=PADY, sticky=W)

new_pick_job_btn = Button(wrapper3, text="Delete", command=delete_element)
new_pick_job_btn.grid(row=2, column=7, padx=PADX, pady=PADY, sticky=W)

close_btn = Button(wrapper3, text="Close", command=root.destroy, font=font_button)

close_btn.grid(row=7, column=2, padx=5, pady=3)

root.title("QSM Modify Supply Data")
root.geometry("1100x700")
root.mainloop()

