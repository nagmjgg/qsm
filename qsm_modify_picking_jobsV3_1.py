"""
https://www.youtube.com/watch?v=i4qLI9lmkqw

Programa con marcos  y formulario con consulta a base de datos

#grids
https://pythonguides.com/python-tkinter-grid/

V2 Stable using Postgresql database
V3 New database Mysql and connection file


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

#https://www.tutorialspoint.com/python_data_access/python_mysql_create_table.htm
#db_name="qsm"
#username='postgres'
#user_password='Quality01'
#db_host='127.0.0.1'
#db_port= '5432'

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
    query = "select id, creation_date, delivery_date, creation_time, job_number, product_name, received_by, " \
            "delivered_by, delivered_flag, moved_flag, returned_flag, return_date, comments, destination from picking_jobs"
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
    t14.set(item['values'][13])

def update_element():
    pick_id = t1.get()
    creation_date = t2.get()
    delivery_date = t3.get()
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
    destination = t14.get()

    if messagebox.askyesno("confirm ?","Are you sure you want to update this element?"):
        query = "update picking_jobs set creation_date = %s, delivery_date = %s, creation_time = %s, job_number = %s, " \
                "product_name = %s, received_by = %s, delivered_by = %s, delivered_flag = %s, moved_flag = %s, " \
                "returned_flag = %s, return_date = %s, comments = %s, destination = %s where id = %s"

        cursor.execute(query, (creation_date, delivery_date, creation_time, job_number, product_name,
                               received_by, delivered_by, delivered_flag, moved_flag, returned_flag, return_date,
                               comments, destination, pick_id ))
        conn.commit()
        clear()
    else:
        return True

def add_new_element():
    pick_id = t1.get()
    creation_date = t2.get()
    delivery_date = t3.get()
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
    destination = t14.get()

    query = "insert into picking_data (creation_date, delivery_date, creation_time, job_number, " \
            "product_name, received_by, delivered_by, delivered_flag, moved_flag, returned_flag, return_date, " \
            "comments, destination) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    cursor.execute(query, (creation_date, delivery_date, creation_time, job_number, product_name,
                           received_by, delivered_by, delivered_flag, moved_flag, returned_flag, return_date, comments,
                           destination))
    conn.commit()
    clear()

def delete_element():
    pick_id = t1.get()
    job_number = t5.get()

    if messagebox.askyesno("confirm Delete ?","Are you sure you want to delete this element?"):
        query = "delete from picking_jobs where id = " + pick_id + " and job_number = '" + job_number + "'"
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
    query = "select id, creation_date, delivery_date, creation_time, job_number, product_name, received_by, " \
            "delivered_by, delivered_flag, moved_flag, returned_flag, return_date, comments, destination from picking_jobs where " \
            "id = '"+q2.upper()+"' or job_number like '%"+q2+"%'"
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

wrapper1 = LabelFrame(root, text="Database")
wrapper2 = LabelFrame(root, text="Search")
wrapper3 = LabelFrame(root, text="Selection")

wrapper1.pack(fill="both", expand="yes", padx=10, pady=10)
wrapper2.pack(fill="both", expand="yes", padx=10, pady=10)
wrapper3.pack(fill="both", expand="yes", padx=10, pady=10)

trv = ttk.Treeview(wrapper1, columns=(1,2,3,4,5,6,7,8,9,10,11,12,13,14), show="headings", height="5")

verscrlbar = ttk.Scrollbar(wrapper1, orient="vertical", command=trv.yview)
verscrlbar.pack(side="right", fill="y")
trv['yscrollcommand']=verscrlbar.set

horscrlbar = ttk.Scrollbar(wrapper1, orient="horizontal", command=trv.xview)
horscrlbar.pack(side="bottom", fill="x")
trv['xscrollcommand']=horscrlbar.set


fields = ['id', 'creation_date', 'delivery_date', 'creation_time', 'job_number', 'product_name', 'received_by',
          'delivered_by', 'delivered_flag', 'moved_flag', 'returned_flag', 'return_date', 'comments', 'destination']

#columns width
trv.column(1,width=80)
trv.column(2,width=100)
trv.column(3,width=100)
trv.column(4,width=80)
trv.column(5,width=80)
trv.column(6,width=200)
trv.column(7,width=150)
trv.column(8,width=150)
trv.column(9,width=80)
trv.column(10,width=80)
trv.column(11,width=80)
trv.column(12,width=100)
trv.column(13,width=200)
trv.column(14,width=200)
trv.pack()
#index, 'part_number','location','expiration','qty', 'lot'
trv.heading(1, text="pick_id")
trv.heading(2, text="creation_date")
trv.heading(3, text="delivery_date")
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
trv.heading(14, text="destination")

trv.bind('<Double 1>', getrow)

query = "select id, creation_date, delivery_date, creation_time, job_number, product_name, received_by, " \
            "delivered_by, delivered_flag, moved_flag, returned_flag, return_date, comments, destination " \
        "from picking_jobs"

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

#Entry state = "normal", "disabled", or "readonly"
pick_id_lbl_job = Label(wrapper3, text="Pick id")
pick_id_lbl_job.grid(row=0, column=0, padx=PADX, pady=PADY)
pick_id_ent_job = Entry(wrapper3, textvariable=t1, state="normal")
pick_id_ent_job.grid(row=1, column=0, padx=PADX, pady=PADY, sticky=W)
#pick_id_ent_job.insert(END,pick_id_new)

creation_date_lbl_job = Label(wrapper3, text="Creation date")
creation_date_lbl_job.grid(row=0, column=1, padx=PADX, pady=PADY)
creation_date_ent_job = DateEntry(wrapper3, selectmode='day', textvariable=t2, locale='en_US', date_pattern='yyyy-MM-dd')
creation_date_ent_job.grid(row=1, column=1, padx=PADX, pady=PADY, sticky=W)

time_lbl_job = Label(wrapper3, text="Creation time")
time_lbl_job.grid(row=0, column=2, padx=PADX, pady=PADY)
time_ent_job = Entry(wrapper3, textvariable=t4)
time_ent_job.grid(row=1, column=2, padx=PADX,pady=PADY, sticky=W)
time_ent_job.insert(END, time_now())

job_number_lbl_job = Label(wrapper3, text="Job Number")
job_number_lbl_job.grid(row=0, column=3, padx=PADX, pady=PADY)
job_number_ent_job = Entry(wrapper3, textvariable=t5, validate='focusout')
job_number_ent_job.grid(row=1, column=3, padx=PADX, pady=PADY, sticky=W)

product_name_lbl_job = Label(wrapper3, text="Product Name")
product_name_lbl_job.grid(row=0, column=4, padx=PADX, pady=PADY)
product_name_ent_job = Entry(wrapper3, textvariable=t6)
product_name_ent_job.grid(row=1, column=4, padx=PADX, pady=PADY, ipadx=100)

received_by_lbl_job = Label(wrapper3, text="Received by")
received_by_lbl_job.grid(row=2, column=3, padx=PADX, pady=PADY)
received_by_ent_job = ttk.Combobox(wrapper3, textvariable=t7,
                               values=["Rafael",
                                       "Antonio",
                                       "Brenda",
                                       "Silvia"])
received_by_ent_job.grid(row=2, column=4, padx=PADX, pady=PADY, ipadx=100)

delivered_by_lbl_job = Label(wrapper3, text="Delivered by")
delivered_by_lbl_job.grid(row=3, column=3, padx=PADX, pady=PADY)
delivered_by_ent_job = ttk.Combobox(wrapper3, textvariable=t8,
                             values=["Juan Ruiz",
                                     "Carlos Jimenez",
                                     "Mauricio Garcia"]
                             )
delivered_by_ent_job.grid(row=3, column=4, padx=PADX, pady=PADY, ipadx=100)

destination_lbl_job = Label(wrapper3, text="Destination")
destination_lbl_job.grid(row=4, column=3, padx=PADX, pady=PADY)
destination_ent_job = ttk.Combobox(wrapper3, textvariable=t14,
                                   values=["Weight",
                                           "Packaging",
                                           "Blending",
                                           "Coating",
                                           "Other"]
                                   )

destination_ent_job.grid(row=4, column=4, padx=PADX, pady=PADY, ipadx=100, sticky=W)

comments_lbl_job = Label(wrapper3, text="Comments")
comments_lbl_job.grid(row=5, column=3, padx=PADX, pady=PADY)
comments_ent_job = Entry(wrapper3, textvariable=t13)
comments_ent_job.grid(row=5, column=4, padx=PADX, pady=PADY, ipadx=100, sticky=W)

delivered_flag_ent_job = Checkbutton(wrapper3, text="Delivered ?", variable=t9)
delivered_flag_ent_job.grid(row=2, column=0, padx=PADX, pady=PADY, sticky=W)

delivery_date_lbl_job = Label(wrapper3, text="Delivery_date")
delivery_date_lbl_job.grid(row=2, column=1, padx=PADX, pady=PADY)
#delivery_date_ent_job = Entry(wrapper3, textvariable=delivery_date_job)
delivery_date_ent_job = DateEntry(wrapper3, selectmode='day', textvariable=t3, locale='en_US', date_pattern='yyyy-MM-dd')
delivery_date_ent_job.grid(row=2, column=2, padx=PADX, pady=PADY, sticky=W)
delivery_date_ent_job.delete(0,END)
delivery_date_ent_job.insert(0,'2000-01-01')


moved_flag_ent_job = Checkbutton(wrapper3, text="Moved in FB ?", variable=t10)
moved_flag_ent_job.grid(row=3, column=0, padx=PADX, pady=PADY, sticky=W)

returned_flag_ent_job = Checkbutton(wrapper3, text="Returned ?", variable=t11)
returned_flag_ent_job.grid(row=4, column=0, padx=PADX, pady=PADY, sticky=W)

return_date_lbl_job = Label(wrapper3, text="Return date")
return_date_lbl_job.grid(row=4, column=1, padx=PADX, pady=PADY)
return_date_ent_job = DateEntry(wrapper3, selectmode='day', textvariable=t12, locale='en_US', date_pattern='yyyy-MM-dd')
return_date_ent_job.grid(row=4, column=2, padx=PADX, pady=PADY)
return_date_ent_job.delete(0,END)
return_date_ent_job.insert(0,'2000-01-01')

save_pick_job_btn = Button(wrapper3, text="Update", command=update_element)
save_pick_job_btn.grid(row=1, column=7, padx=PADX, pady=PADY, sticky=W)

new_pick_job_btn = Button(wrapper3, text="Delete", command=delete_element)
new_pick_job_btn.grid(row=2, column=7, padx=PADX, pady=PADY, sticky=W)

"""
new_pick_job_btn = Button(wrapper3, text="New")
new_pick_job_btn.grid(row=3, column=7, padx=PADX, pady=PADY, sticky=W)

modify_picking_data_btn = Button(wrapper3, text="Modify")
modify_picking_data_btn.grid(row=4, column=7, padx=PADX, pady=PADY, sticky=W)

modify_jobs_data_btn = Button(wrapper3, text="Modify Job Data")
modify_jobs_data_btn.grid(row=5, column=7, padx=PADX, pady=PADY, sticky=W)

"""
close_btn = Button(wrapper3, text="Close", command=root.destroy)

close_btn.grid(row=5, column=0, padx=5, pady=3)



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
root.title("QSM Modify Picking Data")
root.geometry("1000x600")
root.mainloop()

