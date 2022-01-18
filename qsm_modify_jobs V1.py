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

def clear():
    query = "select index, date_deposit_paid, est_compl_date, wo, po, lot, sales_rep, customer, total_count, " \
            "bottle_fg, code, cap_tab_specs, product_bg, job_name, mfg_status, packaging_status from jobs"
    cursor.execute(query)
    rows = cursor.fetchall()
    update(rows)

def getrow(event):
    rowid = trv.identify_row(event.y)
    item = trv.item(trv.focus())

    index.set(item['values'][0])
    date_deposit_paid.set(item['values'][1])
    est_compl_date.set(item['values'][2])
    wo.set(item['values'][3])
    po.set(item['values'][4])
    lot.set(item['values'][5])
    sales_rep.set(item['values'][6])
    customer.set(item['values'][7])
    total_count.set(item['values'][8])
    bottle_fg.set(item['values'][9])
    code.set(item['values'][10])
    cap_tab_specs.set(item['values'][11])
    product_bg.set(item['values'][12])
    job_name.set(item['values'][13])
    mfg_status.set(item['values'][14])
    packaging_status.set(item['values'][15])


def update_element():

    index_ = index.get()
    date_deposit_paid_ = date_deposit_paid.get()
    est_compl_date_ = est_compl_date.get()
    wo_ = wo.get()
    po_ = po.get()
    lot_ = lot.get()
    sales_rep_ = sales_rep.get()
    customer_ = customer.get()
    total_count_ = total_count.get()
    bottle_fg_ = bottle_fg.get()
    code_ = code.get()
    cap_tab_specs_ = cap_tab_specs.get()
    product_bg_ = product_bg.get()
    job_name_ = job_name.get()
    mfg_status_ = mfg_status.get()
    packaging_status_ = packaging_status.get()



    if messagebox.askyesno("confirm ?","Are you sure you want to update this element?"):
        query = "update jobs set date_deposit_paid = %s, est_compl_date = %s, wo = %s, " \
                "po = %s, lot = %s, sales_rep = %s, customer = %s, total_count = %s, bottle_fg = %s, code = %s," \
                "cap_tab_specs = %s, product_bg = %s, job_name = %s, mfg_status = %s, packaging_status = %s " \
                "where  index = %s"
        cursor.execute(query, (date_deposit_paid_, est_compl_date_, wo_, po_, lot_, sales_rep_, customer_,
                               total_count_, bottle_fg_, code_, cap_tab_specs_, product_bg_, job_name_, mfg_status_,
                               packaging_status_, index_))
        conn.commit()
        clear()
    else:
        return True

def add_new_element():
    index = index.get()
    date_deposit_paid = date_deposit_paid.get()
    est_compl_date = est_compl_date.get()
    wo = wo.get()
    po = po.get()
    lot = lot.get()
    sales_rep = sales_rep.get()
    customer = customer.get()
    total_count = total_count.get()
    bottle_fg = bottle_fg.get()
    code = code.get()
    cap_tab_specs = code.get()
    product_bg = cap_tab_specs.get()
    job_name = job_name.get()
    mfg_status = mfg_status.get()
    packaging_status = packaging_status.get()


    query2 = "select max(index) from jobs"
    cursor.execute(query2,(pick_id))
    max_index = cursor.fetchone()
    print(max_index)

    new_index = int(max_index[0]) + 1
    print(new_index)

    query = "insert into jobs (index, date_deposit_paid, est_compl_date, wo, po, lot, sales_rep, customer, " \
            "total_count, bottle_fg, code, cap_tab_specs, product_bg, job_name, mfg_status, packaging_status) " \
            "values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (new_index, date_deposit_paid, est_compl_date, wo, po, lot, sales_rep, customer,
                           total_count, bottle_fg, code, cap_tab_specs, product_bg, job_name, mfg_status, packaging_status))
    conn.commit()
    clear()

def delete_element():
    index = index.get()
    date_deposit_paid = date_deposit_paid.get()
    est_compl_date = est_compl_date.get()
    wo = wo.get()
    po = po.get()
    lot = lot.get()
    sales_rep = sales_rep.get()
    customer = customer.get()
    total_count = total_count.get()
    bottle_fg = bottle_fg.get()
    code = code.get()
    cap_tab_specs = cap_tab_specs.get()
    product_bg = product_bg.get()
    job_name = job_name.get()
    mfg_status = mfg_status.get()
    packaging_status = packaging_status.get()



    if messagebox.askyesno("confirm Delete ?","Are you sure you want to delete this element?"):
        query = "delete from jobs where index = '" + index + "'"
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
    q2 = search_data.get()
    if q2 != "":
        query = "select index, date_deposit_paid, est_compl_date, wo, po, lot, sales_rep, customer, total_count, " \
                "bottle_fg, cap_tab_specs, product_bg, job_name, mfg_status, packaging_status, job_name from jobs " \
                "where index = '"+q2+"' or lot like '%"+q2+"%'"
        cursor.execute(query)
        rows = cursor.fetchall()
        update(rows)
    else:
        pass




root = Tk()

search_data = StringVar()
index = StringVar()
date_deposit_paid = StringVar()
est_compl_date = StringVar()
wo = StringVar()
po = StringVar()
lot = StringVar()
sales_rep = StringVar()
customer = StringVar()
total_count = StringVar()
bottle_fg = StringVar()
code = StringVar()
cap_tab_specs = StringVar()
product_bg = StringVar()
job_name = StringVar()
mfg_status = StringVar()
packaging_status = StringVar()


wrapper1 = LabelFrame(root, text="Database")
wrapper2 = LabelFrame(root, text="Search")
wrapper3 = LabelFrame(root, text="Selection")

wrapper1.pack(fill="both", expand="yes", padx=10, pady=10)
wrapper2.pack(fill="both", expand="yes", padx=10, pady=10)
wrapper3.pack(fill="both", expand="yes", padx=10, pady=10)

trv = ttk.Treeview(wrapper1, columns=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16), show="headings", height="5")

verscrlbar = ttk.Scrollbar(wrapper1, orient="vertical", command=trv.yview)
verscrlbar.pack(side="right", fill="y")

horscrlbar = ttk.Scrollbar(wrapper1, orient="horizontal", command=trv.xview)
horscrlbar.pack(side="bottom", fill="x")

#columns width
trv.column(1,width=50 )
trv.column(2,width=80)
trv.column(3,width=80)
trv.column(4,width=50)
trv.column(5,width=80)
trv.column(6,width=80)
trv.column(7,width=60)
trv.column(8,width=80)
trv.column(9,width=70)
trv.column(10,width=60)
trv.column(11,width=50)
trv.column(12,width=60)
trv.column(13,width=60)
trv.column(14,width=60)
trv.column(15,width=120)
trv.column(16,width=120)
trv.pack()


#index, 'part_number','location','expiration','qty', 'lot'
trv.heading(1, text="index")
trv.heading(2, text="date deposit paid")
trv.heading(3, text="est compl date")
trv.heading(4, text="wo")
trv.heading(5, text="po")
trv.heading(6, text="Lot")
trv.heading(7, text="sales rep")
trv.heading(8, text="customer")
trv.heading(9, text="total count")
trv.heading(10, text="bottle fg")
trv.heading(11, text="code")
trv.heading(12, text="cap tab specs")
trv.heading(13, text="product bg")
trv.heading(14, text="job name")
trv.heading(15, text="mfg status")
trv.heading(16, text="packaging status")


trv.bind('<Double 1>', getrow)

query = "select index, date_deposit_paid, est_compl_date, wo, po, lot, sales_rep, customer, total_count, bottle_fg, code, cap_tab_specs, product_bg, job_name, mfg_status, packaging_status from jobs"
cursor.execute(query)
rows = cursor.fetchall()
update(rows)

#search section
lbl = Label(wrapper2, text="Search")
lbl.pack(side=tk.LEFT, padx=10)
ent = Entry(wrapper2, textvariable=search_data)
ent.pack(side=tk.LEFT, padx=6)
btn = Button(wrapper2, text="Search", command=search)
btn.pack(side=tk.LEFT, padx=6)
cbtn = Button(wrapper2, text="Clear", command=clear)
cbtn.pack(side=tk.LEFT, padx=6)

#user data section
index_data_lbl = Label(wrapper3, text="index")
index_data_lbl.grid(row=0, column=0, padx=5, pady=3)
index_data_ent = Entry(wrapper3, textvariable=index)
index_data_ent.grid(row=1, column=0, padx=5, pady=3, sticky='w')

date_deposit_paid_lbl = Label(wrapper3, text="date deposit paid")
date_deposit_paid_lbl.grid(row=0, column=1, padx=5, pady=3)
date_deposit_paid_ent = Entry(wrapper3, textvariable=date_deposit_paid)
date_deposit_paid_ent.grid(row=1, column=1, padx=5, pady=3, sticky='w')

est_compl_date_lbl = Label(wrapper3, text="est compl date")
est_compl_date_lbl.grid(row=0, column=2, padx=5, pady=3)
est_compl_date_ent = Entry(wrapper3, textvariable=est_compl_date)
est_compl_date_ent.grid(row=1, column=2, padx=5, pady=3, sticky='w')

wo_lbl = Label(wrapper3, text="wo")
wo_lbl.grid(row=0, column=3, padx=5, pady=3)
wo_ent = Entry(wrapper3, textvariable=wo)
wo_ent.grid(row=1, column=3, padx=5, pady=3, sticky='w')

po_lbl = Label(wrapper3, text="po")
po_lbl.grid(row=0, column=4, padx=5, pady=3)
po_ent = Entry(wrapper3, textvariable=po)
po_ent.grid(row=1, column=4, padx=5, pady=3, sticky='w')

lot_lbl = Label(wrapper3, text="lot")
lot_lbl.grid(row=0, column=5, padx=5, pady=3)
lot_ent = Entry(wrapper3, textvariable=lot)
lot_ent.grid(row=1, column=5, padx=5, pady=3, sticky='w')

customer_lbl = Label(wrapper3, text="customer")
customer_lbl.grid(row=0, column=6, padx=5, pady=3)
customer_ent = Entry(wrapper3, textvariable=customer)
customer_ent.grid(row=1, column=6, padx=5, pady=3, ipadx=60, sticky='w')

sales_rep_lbl = Label(wrapper3, text="sales rep")
sales_rep_lbl.grid(row=2, column=0, padx=5, pady=3)
sales_rep_ent = Entry(wrapper3, textvariable=sales_rep)
sales_rep_ent.grid(row=3, column=0, padx=5, pady=3, sticky='w')

total_count_lbl = Label(wrapper3, text="total count")
total_count_lbl.grid(row=2, column=1, padx=5, pady=3)
total_count_ent = Entry(wrapper3, textvariable=total_count)
total_count_ent.grid(row=3, column=1, padx=5, pady=3, sticky='w')

bottle_fg_lbl = Label(wrapper3, text="bottle fg")
bottle_fg_lbl.grid(row=2, column=2, padx=5, pady=3)
bottle_fg_ent = Entry(wrapper3, textvariable=bottle_fg)
bottle_fg_ent.grid(row=3, column=2, padx=5, pady=3, sticky='w')

code_lbl = Label(wrapper3, text="code")
code_lbl.grid(row=2, column=3, padx=5, pady=3)
code_ent = Entry(wrapper3, textvariable=code)
code_ent.grid(row=3, column=3, padx=5, pady=3, sticky='w')

cap_tab_specs_lbl = Label(wrapper3, text="cap tab specs")
cap_tab_specs_lbl.grid(row=2, column=4, padx=5, pady=3)
cap_tab_specs_ent = Entry(wrapper3, textvariable=cap_tab_specs)
cap_tab_specs_ent.grid(row=3, column=4, padx=5, pady=3, sticky='w')

product_bg_lbl = Label(wrapper3, text="product bg")
product_bg_lbl.grid(row=2, column=5, padx=5, pady=3)
product_bg_ent = Entry(wrapper3, textvariable=product_bg)
product_bg_ent.grid(row=3, column=5, padx=5, pady=3, sticky='w')

job_name_lbl = Label(wrapper3, text="job name")
job_name_lbl.grid(row=2, column=6, padx=5, pady=3)
job_name_ent = Entry(wrapper3, textvariable=job_name)
job_name_ent.grid(row=3, column=6, padx=5, pady=3, ipadx=60, sticky='w')

mfg_status_lbl = Label(wrapper3, text="mfg status")
mfg_status_lbl.grid(row=4, column=0, padx=5, pady=3)
mfg_status_ent = Entry(wrapper3, textvariable=mfg_status)
mfg_status_ent.grid(row=5, column=0, padx=5, pady=3, sticky='w')

packaging_status_lbl = Label(wrapper3, text="packaging_status")
packaging_status_lbl.grid(row=4, column=1, padx=5, pady=3)
packaging_status_ent = Entry(wrapper3, textvariable=packaging_status)
packaging_status_ent.grid(row=5, column=1, padx=5, pady=3, sticky='w')

up_btn = Button(wrapper3, text="Update", command=update_element)
add_btn = Button(wrapper3, text="Add New", command=add_new_element)
delete_btn = Button(wrapper3, text="Delete", command=delete_element)

add_btn.grid(row=6, column=0, padx=5, pady=3)
up_btn.grid(row=6, column=1, padx=5, pady=3)
delete_btn.grid(row=6, column=2, padx=5, pady=3)


root.title("QSM Modify Jobs")
root.geometry("1080x720")
root.mainloop()

