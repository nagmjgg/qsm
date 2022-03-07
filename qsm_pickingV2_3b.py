"""
Program to organize the picking process
Resources:
https://www.youtube.com/watch?v=i4qLI9lmkqw
Programa con marcos  y formulario con consulta a base de datos
#grids
https://pythonguides.com/python-tkinter-grid/
using Database norms
V2 Start using Mysql database
v2.2 stable version
"""
import csv
import subprocess
import mysql.connector
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry    #https://pypi.org/project/tkcalendar/
import datetime
import os
import pandas as pd
#from pandastable import Table
#import psycopg2
#import glob    #func last_filename
#from functions import *
#from sql_functions import select_command
from datetime import datetime
from ttkwidgets.autocomplete import AutocompleteCombobox

from tkcalendar import Calendar

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.colheader_justify', 'center')
pd.set_option('display.precision', 3)

folder = 'D:/shared_inventory/server files/'

#https://www.tutorialspoint.com/python_data_access/python_mysql_create_table.htm
db_name="qsm"
username='sql'
user_password='Quality01'
db_host='192.168.210.25'
db_port= '3306'

#establishing the connection
#conn = psycopg2.connect(database=db_name, user=username, password=user_password, host=db_host, port= db_port)
conn = mysql.connector.connect(database=db_name, user=username, password=user_password, host=db_host, port=db_port)

if conn:
    print("Mysql connection ok")
else:
    print("Mysql connection nok")

#Creating a cursor object using the cursor() method
cursor = conn.cursor(buffered=True)

#Fonts
font_columns_name = ('Arial',12,'bold') # normal or bold
font_wrap_title = ('Arial',12,'bold') # normal or bold
font_entry = ('Arial',11,'normal') # normal or bold
font_label = ('Arial',11,'bold') # normal or bold
font_button = ('Arial',11,'bold') # normal or bold
font_main_title = ('Arial',18,'bold') # normal or bold

#fixed value for logging porpuses
script_name = ""

print("line 69")

def date_now():
    date = datetime.now().strftime("%Y-%m-%d")
    return date

def time_now():
    time = datetime.now().strftime("%H:%M:%S")
    return time


def clear():
    query = "select id, part_number, description_x, location, qty, lot, expiration from onhand_ingredients"
    cursor.execute(query)
    rows = cursor.fetchall()
    update(rows)

def getrow(event):
    rowid = trv.identify_row(event.y)
    item = trv.item(trv.focus())
    id_sel.set(item['values'][0])  #id
    part_number_sel.set(item['values'][1])  #part_number
    description_sel.set(item['values'][2])  #description
    location_sel.set(item['values'][3])  #location
    qty_sel.set(item['values'][4])  #qty
    lot_sel.set(item['values'][5])  #lot
    expiration_sel.set(item['values'][6])  #expiration

print("line 88")

def update_element():
    id = id_sel.get()
    part_number = part_number_sel.get()
    description = description_sel.get()
    location = location_sel.get()
    qty = qty_sel.get()
    lot = lot_sel.get()
    expiration = expiration_sel.get()

    if messagebox.askyesno("confirm ?","Are you sure you want to update this element?"):
        query = "update onhand_ingredients set id = %s, part_number = %s, description_x = %s, location = %s, " \
                "qty = %s, lot = %s, expiration = %s where  id = %s"
        cursor.execute(query, (id, part_number, description, location, qty, lot, expiration, id))
        conn.commit()
        clear()
    else:
        return True

def add_new_element():
    id = id_sel.get()
    part_number = part_number_sel.get()
    description = description_sel.get()
    location = location_sel.get()
    qty = qty_sel.get()
    lot = lot_sel.get()
    expiration = expiration_sel.get()

    query = "insert into onhand_ingredients (id, part_number, description_x, location, qty, lot, expiration) " \
            "values(%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (id, part_number, description, location, qty, lot, expiration))
    conn.commit()
    clear()

print("line 123")

def delete_element():
    ingredient_id = t1_sel_data.get()
    if messagebox.askyesno("confirm Delete ?","Are you sure you want to delete this customer?"):
        query = "select id, part_number, description_x, location, qty, lot, expiration from onhand_ingredients"
        cursor.execute(query)
        conn.commit()
        clear()
    else:
        return True

def update(rows):
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert('','end', values=i)

def update_picking(rows):
    trv_pick.delete(*trv_pick.get_children())
    for i in rows:
        trv_pick.insert('','end', values=i)

def search(event = None):
    q2 = q.get()
    if q2:
        query = "select id, part_number, description_x, location, qty, lot, expiration from onhand_ingredients " \
            "where part_number like '%"+q2.upper()+"%' or description_x like '%"+q2+"%'"
    else:
        query = "select id, part_number, description_x, location, qty, lot, expiration from onhand_ingredients"

    print(query)
    cursor.execute(query)

    rows = cursor.fetchall()
    update(rows)

    conn.commit()

print("line 153")

def search_picking():
    pick_id = pick_id_job.get()
    query = "select id, part_number, part_description, location, qty, part_lot, expiration from picking_data " \
            "where picking_job_id = '" +pick_id + "'"
    cursor.execute(query)
    rows = cursor.fetchall()
    update_picking(rows)

def new_picking_job():
    pick_id_ent_job.delete(0,END)
    creation_date_ent_job.delete(0,END)
    creation_date_ent_job.insert(0,date_now())
    time_ent_job.delete(0,END)
    time_ent_job.insert(END, time_now())
    job_number_ent_job.delete(0,END)
    product_name_ent_job.delete(0,END)
    received_by_ent_job.delete(0,END)
    delivered_by_ent_job.delete(0,END)
    destination_ent_job.delete(0,END)
    comments_ent_job.delete(0,END)
    delivery_date_ent_job.delete(0,END)
    delivery_date_ent_job.insert(0, '2000-01-01')
    moved_flag_ent_job = 0
    returned_flag_ent_job = 0
    return_date_ent_job.delete(0, END)
    return_date_ent_job.insert(0, '2000-01-01')

def pick_element():
    pick_id = pick_id_job.get()
    creation_date = creation_date_job.get()
    delivery_date = delivery_date_job.get()
    time = creation_time_job.get()
    job_number = job_number_job.get()
    product_name = product_name_job.get()
    received_by = received_by_job.get()
    delivered_by = delivered_by_job.get()
    delivered_flag = delivered_flag_job.get()
    moved_flag = moved_flag_job.get()
    returned_flag = returned_flag_job.get()
    return_date = returned_date_job.get()
    comments = comments_job.get()
    part_number = part_number_sel.get()
    part_description = description_sel.get()
    location = location_sel.get()
    qty = qty_sel.get()
    unit = "ea"
    #amount_each = t9_sel_data.get()
    part_lot = lot_sel.get()
    part_expiration = expiration_sel.get()

    query = "insert into picking_data (picking_job_id, location, part_number, part_description, part_lot, expiration, " \
            "qty, unit) values (%s, %s, %s, %s, %s, %s, %s, %s)"

    cursor.execute(query,(int(pick_id), location,part_number, part_description, part_lot, part_expiration, float(qty), unit))
    conn.commit()
    search_picking()

print("line 213")

def modify_picking_data():
    subprocess.call("qsm_modify_picking_dataV1.py", shell=True)

def modify_jobs_data():
    subprocess.call("qsm_modify_picking_jobsV3_1.py", shell=True)

def query_to_dataframe(conn, query, column_names):
   """
   turn query data to dataframe so it can be used for combobox or vlookup functions
   #df = postgresql_to_dataframe(conn, "select * from MonthlyTemp", column_names)
   #column_names = ["id", "source", "datetime", "mean_temp"]
   https://naysan.ca/2020/05/31/postgresql-to-pandas/
   Tranform a SELECT query into a pandas dataframe
   """
   cursor = conn.cursor()
   try:
      cursor.execute(query)
   except (Exception, psycopg2.DatabaseError) as error:
      print("Error: %s" % error)
      cursor.close()
      return 1

   # Naturally we get a list of tupples
   tupples = cursor.fetchall()
   cursor.close()

   # We just need to turn it into a pandas dataframe
   df = pd.DataFrame(tupples, columns=column_names)
   df = df.drop_duplicates()
   return df

def new_job_name(event=None):
    global auto_job_name
    query = "select mfg_status from jobs where lot = '" + job_number_job.get() + "'"
    cursor.execute(query)
    df = query_to_dataframe(conn, query, ['mfg_status'])

    count = cursor.rowcount
    print(f"new_job_name -> Row Count: {count}")
    if count != 0:
        auto_job_name = df['mfg_status'][0]
        product_name_ent_job.delete(0,END)
        product_name_ent_job.insert(END, auto_job_name)
    else:
        pass

def new_pick_id_job(event=None):
    """
        Identify the new identifier for "Picking_Job_Id" for the specific job
    """
    query = "select id from picking_jobs where creation_date = '" + creation_date_job.get() + \
            "' and creation_time = '" + creation_time_job.get() + "' and job_number = '" + job_number_job.get() + "'"
    cursor.execute(query)

    print(f"new pick id job: {cursor.rowcount}")

    df = query_to_dataframe(conn, query, ['id'])
    if df['id'][0] is not None:
        pick_job_id = df['id'][0]
        print(f"df['id']: {pick_job_id}")
        pick_id_ent_job.delete(0, END)
        pick_id_ent_job.insert(END, pick_job_id)
    else:
        pass

    conn.commit()

def save_picking_job():
    pick_id = pick_id_job.get()
    creation_date = creation_date_job.get()
    delivery_date = delivery_date_job.get()
    time = creation_time_job.get()
    job_number = job_number_job.get()
    product_name = product_name_job.get()
    received_by = received_by_job.get()
    delivered_by = delivered_by_job.get()
    delivered_flag = delivered_flag_job.get()
    moved_flag = moved_flag_job.get()
    returned_flag = returned_flag_job.get()
    return_date = returned_date_job.get()
    comments = comments_job.get()
    destination = destination_job.get()

    query0 = "select creation_date, delivery_date, creation_time, job_number from picking_jobs where " \
            "creation_date = '" + creation_date + "' and delivery_date = '" + delivery_date + \
            "' and creation_time = '" + time + "' and job_number = '" + job_number + "'"

    cursor.execute(query0)

    row_count = cursor.rowcount

    if row_count == 0:

        query1 = "insert into picking_jobs (creation_date, delivery_date, creation_time, job_number, " \
                "product_name, received_by, delivered_by, delivered_flag, moved_flag, " \
                "returned_flag, return_date, comments, destination) " \
                "values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        cursor.execute(query1, (creation_date, delivery_date, time, job_number, product_name, received_by,
                               delivered_by, delivered_flag, moved_flag, returned_flag, return_date, comments, destination))
        conn.commit()
        new_pick_id_job()
    clear()
    #search_picking()

def log(message_text,  level):
    global script_name
    date_log = date_now()
    time_log = time_now()

    query = "insert into logs (date, time, script_name, text, level) values (%s, %s, %s, %s, %s)"

    cursor.execute(query, (date_log, time_log, script_name, message_text, level))
    conn.commit()

def import_data_from_csv_to_mysql(db_table,csv_file,command):
    csv_data = csv.reader(file(csv_file))
    for row in csv_data:
        cursor.execute(command)

print("line 300")

#************************************<<<< ROOT >>>>***********************************************
#*************************************************************************************************

root = Tk()

PADX = 2
PADY = 2

wrapper0 = LabelFrame(root, text="Job Data", font=font_wrap_title)
wrapper1 = LabelFrame(root, text="Database", font=font_wrap_title)
wrapper2 = LabelFrame(root, text="Search", font=font_wrap_title)
wrapper3 = LabelFrame(root, text="Selection", font=font_wrap_title)
wrapper4 = LabelFrame(root, text="Pick", font=font_wrap_title)

wrapper0.pack(fill="both", expand="yes", padx=3, pady=3)
wrapper2.pack(fill="both", expand="yes", padx=3, pady=3)
wrapper1.pack(fill="both", expand="yes", padx=3, pady=3)
wrapper3.pack(fill="both", expand="yes", padx=3, pady=3)
wrapper4.pack(fill="both", expand="yes", padx=3, pady=3)


trv = ttk.Treeview(wrapper1, columns=(1,2,3,4,5,6,7), show="headings", height="4")
verscrlbar = ttk.Scrollbar(wrapper1, orient="vertical", command=trv.yview)
verscrlbar.pack(side="right", fill="y")
trv['yscrollcommand'] = verscrlbar.set

#columns width
trv.column(1,width=50)
trv.column(2,width=80)
trv.column(3,width=280)
trv.column(4,width=200)
trv.column(5,width=100)
trv.column(6,width=200)
trv.column(7,width=100)
trv.pack()
#id, 'part_number','location','expiration','qty', 'lot'
trv.heading(1, text="id")
trv.heading(2, text="part_number")
trv.heading(3, text="Description")
trv.heading(4, text="Location")
trv.heading(5, text="Qty")
trv.heading(6, text="Lot")
trv.heading(7, text="Expiration")

trv.bind('<Double 1>', getrow)

#query = "select id, part_number, description_x, location, qty, lot, expiration from onhand_ingredients"
#cursor.execute(query)
#rows = cursor.fetchall()
#update(rows)

#******************  Tree View: Picking ***************
#******************************************************

trv_pick = ttk.Treeview(wrapper4, columns=(1,2,3,4,5,6,7), show="headings", height="8")
verscrlbar = ttk.Scrollbar(wrapper4, orient="vertical", command=trv_pick.yview)
verscrlbar.pack(side="right", fill="y")
trv_pick['yscrollcommand'] = verscrlbar.set

#columns width
trv_pick.column(1,width=50)
trv_pick.column(2,width=80)
trv_pick.column(3,width=280)
trv_pick.column(4,width=200)
trv_pick.column(5,width=100)
trv_pick.column(6,width=200)
trv_pick.column(7,width=100)
trv_pick.pack()
#id, 'part_number','location','expiration','qty', 'lot'
trv_pick.heading(1, text="pick_id")
trv_pick.heading(2, text="part_number")
trv_pick.heading(3, text="Description")
trv_pick.heading(4, text="Location")
trv_pick.heading(5, text="Qty")
trv_pick.heading(6, text="Lot")
trv_pick.heading(7, text="Expiration")

#*************** Job data section *******************
#****************************************************

pick_id_job = StringVar()
modified_job = StringVar()
creation_date_job = StringVar()
delivery_date_job = StringVar()
creation_time_job = StringVar()
job_number_job = StringVar()
product_name_job = StringVar()
received_by_job = StringVar()
delivered_by_job = StringVar()
delivered_flag_job = 0
delivered_flag_job = StringVar()
destination_job = StringVar()
comments_job = StringVar()
moved_flag_job = IntVar()
returned_flag_job = IntVar()
returned_date_job = StringVar()
auto_job_name = StringVar()
q = StringVar()


#Entry state = "normal", "disabled", or "readonly"
pick_id_lbl_job = Label(wrapper0, text="Pick id", font=font_label)
pick_id_lbl_job.grid(row=0, column=0, padx=PADX, pady=PADY)
pick_id_ent_job = Entry(wrapper0, textvariable=pick_id_job, state="normal")
pick_id_ent_job.grid(row=1, column=0, padx=PADX, pady=PADY, sticky=W)
#pick_id_ent_job.insert(END,pick_id_new)

creation_date_lbl_job = Label(wrapper0, text="Creation date", font=font_label)
creation_date_lbl_job.grid(row=0, column=1, padx=PADX, pady=PADY)
creation_date_ent_job = DateEntry(wrapper0, selectmode='day', textvariable=creation_date_job, locale='en_US', date_pattern='yyyy-MM-dd')
creation_date_ent_job.grid(row=1, column=1, padx=PADX, pady=PADY, sticky=W)

time_lbl_job = Label(wrapper0, text="Creation time", font=font_label)
time_lbl_job.grid(row=0, column=2, padx=PADX, pady=PADY)
time_ent_job = Entry(wrapper0, textvariable=creation_time_job)
time_ent_job.grid(row=1, column=2, padx=PADX,pady=PADY, sticky=W)
time_ent_job.insert(END, time_now())

job_number_lbl_job = Label(wrapper0, text="Job Number", font=font_label)
job_number_lbl_job.grid(row=0, column=3, padx=PADX, pady=PADY)
job_number_ent_job = Entry(wrapper0, textvariable=job_number_job, validate='focusout', validatecommand=new_job_name)
job_number_ent_job.grid(row=1, column=3, padx=PADX, pady=PADY, sticky=W)
job_number_ent_job.bind('<Return>',new_job_name)

product_name_lbl_job = Label(wrapper0, text="Product Name", font=font_label)
product_name_lbl_job.grid(row=0, column=4, padx=PADX, pady=PADY)
product_name_ent_job = Entry(wrapper0, textvariable=product_name_job)
product_name_ent_job.grid(row=1, column=4, padx=PADX, pady=PADY, ipadx=100)

received_by_lbl_job = Label(wrapper0, text="Received by", font=font_label)
received_by_lbl_job.grid(row=2, column=3, padx=PADX, pady=PADY)
received_by_ent_job = ttk.Combobox(wrapper0, textvariable=received_by_job,
                               values=["Rafael",
                                       "Antonio",
                                       "Brenda",
                                       "Silvia"])
received_by_ent_job.grid(row=2, column=4, padx=PADX, pady=PADY, ipadx=100)

delivered_by_lbl_job = Label(wrapper0, text="Delivered by", font=font_label)
delivered_by_lbl_job.grid(row=3, column=3, padx=PADX, pady=PADY)
delivered_by_ent_job = ttk.Combobox(wrapper0, textvariable=delivered_by_job,
                             values=["Juan Ruiz",
                                     "Carlos Jimenez",
                                     "Mauricio Garcia"]
                             )
delivered_by_ent_job.grid(row=3, column=4, padx=PADX, pady=PADY, ipadx=100)

destination_lbl_job = Label(wrapper0, text="Destination", font=font_label)
destination_lbl_job.grid(row=4, column=3, padx=PADX, pady=PADY)
destination_ent_job = ttk.Combobox(wrapper0, textvariable=destination_job,
                                   values=["Weight",
                                           "Packaging",
                                           "Blending",
                                           "Coating",
                                           "Other"]
                                   )

destination_ent_job.grid(row=4, column=4, padx=PADX, pady=PADY, ipadx=100, sticky=W)

comments_lbl_job = Label(wrapper0, text="Comments", font=font_label)
comments_lbl_job.grid(row=5, column=3, padx=PADX, pady=PADY)
comments_ent_job = Entry(wrapper0, textvariable=comments_job)
comments_ent_job.grid(row=5, column=4, padx=PADX, pady=PADY, ipadx=100, sticky=W)

delivered_flag_ent_job = Checkbutton(wrapper0, text="Delivered ?", variable=delivered_flag_job, font=font_label)
delivered_flag_ent_job.grid(row=2, column=0, padx=PADX, pady=PADY, sticky=W)

delivery_date_lbl_job = Label(wrapper0, text="Delivery_date", font=font_label)
delivery_date_lbl_job.grid(row=2, column=1, padx=PADX, pady=PADY)
#delivery_date_ent_job = Entry(wrapper0, textvariable=delivery_date_job)
delivery_date_ent_job = DateEntry(wrapper0, selectmode='day', textvariable=delivery_date_job, locale='en_US', date_pattern='yyyy-MM-dd')
delivery_date_ent_job.grid(row=2, column=2, padx=PADX, pady=PADY, sticky=W)
delivery_date_ent_job.delete(0,END)
delivery_date_ent_job.insert(0,'2000-01-01')


moved_flag_ent_job = Checkbutton(wrapper0, text="Moved in FB ?", variable=moved_flag_job, font=font_label)
moved_flag_ent_job.grid(row=3, column=0, padx=PADX, pady=PADY, sticky=W)

returned_flag_ent_job = Checkbutton(wrapper0, text="Returned ?", variable=returned_flag_job, font=font_label)
returned_flag_ent_job.grid(row=4, column=0, padx=PADX, pady=PADY, sticky=W)

return_date_lbl_job = Label(wrapper0, text="Return date", font=font_label)
return_date_lbl_job.grid(row=4, column=1, padx=PADX, pady=PADY)
return_date_ent_job = DateEntry(wrapper0, selectmode='day', textvariable=returned_date_job, locale='en_US', date_pattern='yyyy-MM-dd')
return_date_ent_job.grid(row=4, column=2, padx=PADX, pady=PADY)
return_date_ent_job.delete(0,END)
return_date_ent_job.insert(0,'2000-01-01')

save_pick_job_btn = Button(wrapper0, bg="#7cb7b7", text="Save", command=save_picking_job)
save_pick_job_btn.grid(row=1, column=7, padx=PADX, pady=PADY, sticky=W)

new_pick_job_btn = Button(wrapper0, bg="#7c85b7", text="Load")
new_pick_job_btn.grid(row=2, column=7, padx=PADX, pady=PADY, sticky=W)

new_pick_job_btn = Button(wrapper0, bg="#ba7c7c", text="New", command=new_picking_job)
new_pick_job_btn.grid(row=3, column=7, padx=PADX, pady=PADY, sticky=W)

modify_picking_data_btn = Button(wrapper0, bg="#B7B7B7", text="Modify Picking Data", command=modify_picking_data)
modify_picking_data_btn.grid(row=4, column=7, padx=PADX, pady=PADY, sticky=W)

modify_jobs_data_btn = Button(wrapper0, bg="#B7B7B7", text="Modify Job Data", command=modify_jobs_data)
modify_jobs_data_btn.grid(row=5, column=7, padx=PADX, pady=PADY, sticky=W)


#******************** Search section ********************
#********************************************************

def set_search_section():
    search_lbl = Label(wrapper2, text="Search")
    search_lbl.pack(side=tk.LEFT, padx=PADX)
    search_ent = Entry(wrapper2, textvariable=q)
    search_ent.pack(side=tk.LEFT, padx=PADX)
    search_ent.bind('<Return>',search)
    search_btn = Button(wrapper2, text="Search", command=search)
    search_btn.pack(side=tk.LEFT, padx=PADX)
    clear_btn = Button(wrapper2, text="Clear", command=clear)
    clear_btn.pack(side=tk.LEFT, padx=PADX)


#******************* Data selection ******************
#**********************************************************

id_sel = StringVar()
part_number_sel = StringVar()
description_sel = StringVar()
location_sel = StringVar()
qty_sel = StringVar()
lot_sel = StringVar()
expiration_sel = StringVar()

def set_data_selection_section():


    id_lbl = Label(wrapper3, text="Id", font=font_label)
    id_lbl.grid(row=0, column=0, padx=PADX, pady=PADY, ipadx=2)
    id_ent = Entry(wrapper3, textvariable=id_sel)
    id_ent.grid(row=1, column=0, padx=PADX, pady=PADY, sticky=W)

    part_number_lbl = Label(wrapper3, text="Part number", font=font_label)
    part_number_lbl.grid(row=0, column=1,padx=PADX, pady=PADY)
    part_number_ent = Entry(wrapper3, textvariable=part_number_sel)
    part_number_ent.grid(row=1, column=1, padx=PADX, pady=PADY, sticky=W)

    description_lbl = Label(wrapper3, text="Description", font=font_label)
    description_lbl.grid(row=0, column=2, padx=PADX, pady=PADY)
    description_ent = Entry(wrapper3, textvariable=description_sel)
    description_ent.grid(row=1, column=2, padx=PADX, pady=PADY, ipadx=120, sticky=W)

    location_lbl = Label(wrapper3, text="Location", font=font_label)
    location_lbl.grid(row=0, column=3, padx=PADX, pady=PADY)
    location_ent = Entry(wrapper3, textvariable=location_sel)
    location_ent.grid(row=1, column=3, padx=PADX, pady=PADY, ipadx=50, sticky=W)

    qty_lbl = Label(wrapper3, text="Qty", font=font_label)
    qty_lbl.grid(row=0, column=4, padx=PADX, pady=PADY)
    qty_ent = Entry(wrapper3, textvariable=qty_sel)
    qty_ent.grid(row=1, column=4, padx=PADX, pady=PADY, sticky=W)

    lot_lbl = Label(wrapper3, text="Lot", font=font_label)
    lot_lbl.grid(row=2, column=3, padx=PADX, pady=PADY)
    lot_ent = Entry(wrapper3, textvariable=lot_sel)
    lot_ent.grid(row=3, column=3, padx=PADX, pady=PADY, ipadx=50, sticky=W)

    expiration_lbl = Label(wrapper3, text="Expiration", font=font_label)
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

    search()

set_search_section()
set_data_selection_section()

root.title("Picking")
root.geometry("1080x720+50+50")
root.mainloop()