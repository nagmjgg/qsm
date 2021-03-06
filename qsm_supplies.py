"""
Programm to input supplies devlivered to the different departments



"""

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import date,datetime

#https://www.tutorialspoint.com/python_data_access/python_mysql_create_table.htm
import psycopg2

db_name="qsm"
username='postgres'
user_password='Quality01'
db_host='127.0.0.1'
db_port= '5432'

#establishing the connection
conn = psycopg2.connect(database=db_name, user=username, password=user_password, host=db_host, port=db_port)

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Fonts
font_columns_name = ('Arial',10,'bold') # normal or bold
font_wrap_title = ('Arial',12,'bold') # normal or bold

#fixed values
PADX = 1
PADY = 1

def getrow(event):
    rowid = trv.identify_row(event.y)
    item = trv.item(trv.focus())
    date_ent
    time_ent
    part_number_ent
    part_name_ent
    part_lot_ent
    qty_ent
    unit_ent
    received_by_ent
    delivered_by_ent
    updated_ent
    
    rowid = trv.identify_row(event.y)
    item = trv.item(trv.focus())
    index_sel.set(item['values'][0])  #index
    part_number_sel.set(item['values'][1])  #part_number
    description_sel.set(item['values'][2])  #description
    location_sel.set(item['values'][3])  #location
    qty_sel.set(item['values'][4])  #qty
    lot_sel.set(item['values'][5])  #lot
    expiration_sel.set(item['values'][6])  #expiration

def update(rows):
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert('','end',values=i)

def search():
    q2 = q.get()

    query = "select part_index, part_number, part_name, part_unit from parts where part_number like '" + q2.upper() \
            + "' or part_name like '" + q2 + "'"
    cursor.execute(query)
    rows = cursor.fetchall()
    update(rows)

def date_now():
    date = datetime.now().strftime("%Y-%m-%d")
    return date

def time_now():
    time = datetime.now().strftime("%H:%M")
    return time

def clear():
    pass

def add_new_element():
    date_ent = date_ent.get()
    time_ent = time_ent.get()
    part_number_ent = part_number_ent.get()
    part_name_ent = part_name_ent.get()
    part_lot_ent = part_lot_ent.get()
    qty_ent = qty_ent.get()
    unit_ent = unit_ent.get()
    received_by_ent = received_by_ent.get()
    delivered_by_ent = delivered_by_ent.get()
    updated_ent = updated_ent.get()

    query = "insert into supplies (date, time, part_number, part_name, part_lot, qty, unit, received_by, " \
            "delivered_by, updated_flag) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    cursor.execute(query, (date_ent, time_ent, part_number_ent, part_name_ent, part_lot_ent, qty_ent, unit_ent,
                           received_by_ent, delivered_by_ent, updated_ent))
    conn.commit()
    #clear()

#***************************** ROOT **********************************
#*********************************************************************

root = Tk()

root.title("Supplies")

#Get the current screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

screen_size = str(screen_width) + "x" + str(screen_height)
root.geometry(screen_size)

font_columns_name = ('Arial',10,'bold') # normal or bold
font_wrap_title = ('Arial',12,'bold') # normal or bold
font_entry = ('Arial',8,'normal') # normal or bold
font_label = ('Arial',8,'bold') # normal or bold

wrapper0 = LabelFrame(root, text="Search", font=font_wrap_title)
wrapper1 = LabelFrame(root, text="List", font=font_wrap_title)
wrapper2 = LabelFrame(root, text="Input", font=font_wrap_title)

wrapper0.pack(fill="both", padx=PADX, pady=PADY)
wrapper1.pack(fill="both", padx=PADX, pady=PADY)
wrapper2.pack(fill="both", padx=PADX, pady=PADY)

#*********************** Search *****************************
#************************************************************

q = StringVar()

search_lbl = LabelFrame(wrapper0, text="Part or Description", font=font_label)
search_lbl.grid(row=0, column=0, padx=PADX, pady=PADY, sticky=W)
search_ent = Entry(wrapper0, textvariable=q, font=font_entry)
search_ent.grid(row=1, column=0, padx=PADX, pady=PADY, sticky=W)

search_btn = Button(wrapper0, text="Search", command=search)
search_btn.grid(row=1, column=1, padx=PADX, pady=PADY, sticky=W)

#*********************** List *******************************
#************************************************************

trv = ttk.Treeview(wrapper1, columns=(1,2,3,4), show="headings", height="3")

verscrlbar = ttk.Scrollbar(wrapper1, orient="vertical", command=trv.yview)
verscrlbar.pack(side="right",fill="y")
trv["yscrollcommand"] = verscrlbar.set


trv.column(1, width=80)
trv.column(2, width=200)
trv.column(3, width=200)
trv.column(4, width=80)
trv.pack()

trv.heading(1, text="Index")
trv.heading(2, text="Part number")
trv.heading(3, text="Part name")
trv.heading(4, text="Part unit")

#*********************** Form *******************************
#************************************************************
date_ent = StringVar()
time_ent = StringVar()
part_number_ent = StringVar()
part_name_ent = StringVar()
part_lot_ent = StringVar()
qty_ent = StringVar()
unit_ent = StringVar()
received_by_ent = StringVar()
delivered_by_ent = StringVar()
updated_ent = StringVar()

frame = Frame(wrapper2)

frame_scrollbar = Scrollbar(frame, orient="horizontal")
frame_scrollbar.pack(side="right", fill="x")

"""verscrlbar = ttk.Scrollbar()
verscrlbar = ttk.Scrollbar(frame, orient="vertical", command=frame.yview)
verscrlbar.pack(side="right",fill="y")
frame["yscrollcommand"] = verscrlbar.set

horscrlbar = ttk.Scrollbar(frame, orient="horizontal", command=frame.xview)
horscrlbar.pack(side="right",fill="x")
frame["xscrollcommand"] = horscrlbar.set
"""



date_lbl = Label(wrapper2, text="Date", font=font_label)
date_lbl.grid(row=0, column=0, padx=PADX, pady=PADY)
date_ent = Entry(wrapper2, textvariable=date_ent, font=font_entry)
date_ent.grid(row=1, column=0, padx=PADX, pady=PADY, ipadx=10)
date_ent.insert(0,date_now())

time_lbl = Label(wrapper2, text="Time", font=font_label)
time_lbl.grid(row=0, column=1, padx=PADX, pady=PADY)
time_ent = Entry(wrapper2, textvariable=time_ent, font=font_entry)
time_ent.grid(row=1, column=1, padx=PADX, pady=PADY)
time_ent.insert(0,time_now())

part_number_lbl = Label(wrapper2, text="Part number", font=font_label)
part_number_lbl.grid(row=0, column=2, padx=PADX, pady=PADY)
part_number_ent = Entry(wrapper2, textvariable=part_number_ent, font=font_entry)
part_number_ent.grid(row=1, column=2, padx=PADX, pady=PADY)

part_name_lbl = Label(wrapper2, text="Part name", font=font_label)
part_name_lbl.grid(row=0, column=3, padx=PADX, pady=PADY)
part_name_ent = Entry(wrapper2, textvariable=part_name_ent, font=font_entry)
part_name_ent.grid(row=1, column=3, padx=PADX, pady=PADY, ipadx=100)

part_lot_lbl = Label(wrapper2, text="Lot", font=font_label)
part_lot_lbl.grid(row=0, column=4, padx=PADX, pady=PADY)
part_lot_ent = Entry(wrapper2, textvariable=part_lot_ent, font=font_entry)
part_lot_ent.grid(row=1, column=4, padx=PADX, pady=PADY)

qty_lbl = Label(wrapper2, text="Qty", font=font_label)
qty_lbl.grid(row=0, column=5, padx=PADX, pady=PADY)
qty_ent = Entry(wrapper2, textvariable=qty_ent, font=font_entry)
qty_ent.grid(row=1, column=5, padx=PADX, pady=PADY)

unit_lbl = Label(wrapper2, text="Unit", font=font_label)
unit_lbl.grid(row=0, column=6, padx=PADX, pady=PADY)
unit_ent = Entry(wrapper2, textvariable=unit_ent, font=font_entry)
unit_ent.grid(row=1, column=6, padx=PADX, pady=PADY)

received_by_lbl = Label(wrapper2, text="Received by", font=font_label)
received_by_lbl.grid(row=0, column=7, padx=PADX, pady=PADY)
received_by_ent = Entry(wrapper2, textvariable=received_by_ent, font=font_entry)
received_by_ent.grid(row=1, column=7, padx=PADX, pady=PADY, ipadx=100)

delivered_by_lbl = Label(wrapper2, text="Delivered by", font=font_label)
delivered_by_lbl.grid(row=0, column=8, padx=PADX, pady=PADY)
delivered_by_ent = Entry(wrapper2, textvariable=delivered_by_ent, font=font_entry)
delivered_by_ent.grid(row=1, column=8, padx=PADX, pady=PADY, ipadx=100)

updated_lbl = Label(wrapper2, text="Updated", font=font_label)
updated_lbl.grid(row=0, column=9, padx=PADX, pady=PADY)
updated_ent = Entry(wrapper2, textvariable=updated_ent, font=font_entry)
updated_ent.grid(row=1, column=9, padx=PADX, pady=PADY, ipadx=100)

trv.bind('<Double 1>', getrow)


root.mainloop()