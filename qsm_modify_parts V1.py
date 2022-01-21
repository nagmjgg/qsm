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

columns = ['part_no','part_name','part_unit']
table = 'parts'

"""
#establishing the connection
conn = psycopg2.connect(database=db_name, user=username, password=user_password, host=db_host, port= db_port)

#Creating a cursor object using the cursor() method
cursor = conn.cursor()
"""

def clear():
    query = "select " + fields[0] + ", " + fields[1] + ", " + fields[2] + ", " + fields[3] + " from " + table
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

def update_element():

    part_index = t1.get()
    part_number = t2.get()
    part_name = t3.get()
    part_unit = t4.get()

    if messagebox.askyesno("confirm ?","Are you sure you want to update this element?"):
        query = "update " + table + " set " + fields[1] + " = %s, " + fields[2] + " = %s, " + fields[3] + " = %s" \
                " where  " + fields[0] + " = %s"
        cursor.execute(query, (part_number, part_name, part_unit, part_index))
        conn.commit()
        clear()

    else:
        return True

def add_new_element():

    part_index = t1.get()
    part_number = t2.get()
    part_name = t3.get()
    part_unit = t4.get()


    query = "insert into " + table + " (part_number, part_name, part_unit) values(%s, %s, %s)"
    cursor.execute(query, (part_number.upper(), part_name, part_unit.upper()))
    conn.commit()
    clear()

def delete_element():
    part_no = t1.get()
    part_name = t2.get()
    part_unit = t3.get()

    ingredient_id = t1.get()
    if messagebox.askyesno("confirm Delete ?","Are you sure you want to delete this element?"):
        query = "delete from " + table + " where " + fields[0] + " = '" + part_no + "'"
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
    query = "select " + fields[0] + ", " + fields[1] + ", " + fields[2] + ", " + fields[3] + " from " + table + " where part_number = '"+q2+"' or part_name like '%"+q2+"%'"
    cursor.execute(query)
    rows = cursor.fetchall()
    update(rows)




root = Tk()
q = StringVar()
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar()

fields = ['part_index','part_number','part_name','part_unit']
table = 'parts'

wrapper1 = LabelFrame(root, text="Database")
wrapper2 = LabelFrame(root, text="Search")
wrapper3 = LabelFrame(root, text="Selection")

wrapper1.pack(fill="both", expand="yes", padx=10, pady=10)
wrapper2.pack(fill="both", expand="yes", padx=10, pady=10)
wrapper3.pack(fill="both", expand="yes", padx=10, pady=10)

trv = ttk.Treeview(wrapper1, columns=(1,2,3,4), show="headings", height="10")

verscrlbar = ttk.Scrollbar(wrapper1, orient="vertical", command=trv.yview)
verscrlbar.pack(side="right", fill="y")

#columns width
trv.column(1,width=70)
trv.column(2,width=70)
trv.column(3,width=280)
trv.column(4,width=80)
trv.pack()

#index, 'part_number','location','expiration','qty', 'lot'
trv.heading(1, text=fields[0])
trv.heading(2, text=fields[1])
trv.heading(3, text=fields[2])
trv.heading(4, text=fields[3])
trv.bind('<Double 1>', getrow)

query = "select " + fields[0] + ", " + fields[1] + ", " + fields[2] + ", " + fields[3] + " from " + table
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

#part data section
lbl0 = Label(wrapper3, text=fields[0])
lbl0.grid(row=0, column=0, padx=5, pady=3)
ent0 = Entry(wrapper3, textvariable=t1, state='disabled')
ent0.grid(row=0, column=1, padx=5, pady=3, sticky='w')

lbl1 = Label(wrapper3, text=fields[1])
lbl1.grid(row=1, column=0, padx=5, pady=3)
ent1 = Entry(wrapper3, textvariable=t2)
ent1.grid(row=1, column=1, padx=5, pady=3, sticky='w')

lbl2 = Label(wrapper3, text=fields[2])
lbl2.grid(row=2, column=0, padx=5, pady=3)
ent2 = Entry(wrapper3, textvariable=t3)
ent2.grid(row=2, column=1, padx=5, pady=3, ipadx=100, sticky='w')

lbl2 = Label(wrapper3, text=fields[3])
lbl2.grid(row=3, column=0, padx=5, pady=3)
ent2 = Entry(wrapper3, textvariable=t4)
ent2.grid(row=3, column=1, padx=5, pady=3, sticky='w')


up_btn = Button(wrapper3, text="Update", command=update_element)
add_btn = Button(wrapper3, text="Add New", command=add_new_element)
delete_btn = Button(wrapper3, text="Delete", command=delete_element)

add_btn.grid(row=0, column=3, padx=5, pady=3, sticky='w')
up_btn.grid(row=1, column=3, padx=5, pady=3, sticky='w')
delete_btn.grid(row=2, column=3, padx=5, pady=3, sticky='w')

root.title("QSM Modify Parts")
root.geometry("1080x720")
root.mainloop()

