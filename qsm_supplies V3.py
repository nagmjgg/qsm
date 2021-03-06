"""
Programm to input supplies devlivered to the different departments

V3 change of database from postgresql for mysql


"""

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import date,datetime
import logging


#https://www.tutorialspoint.com/python_data_access/python_mysql_create_table.htm
import mysql.connector

db_name="qsm"
username='supply'
user_password='SupplyQualityQsm'
db_host='192.168.210.25'
db_port= '3306'

#establishing the connection
conn = mysql.connector.connect(database=db_name, user=username, password=user_password, host=db_host, port=db_port)

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
    #part_index.set(item['values'][0])
    part_number_sel.set(item['values'][1])
    part_name_sel.set(item['values'][2])
    part_unit_sel.set(item['values'][3])

def update(rows):
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert('','end',values=i)

def search(event=None):
    q2 = q.get()

    query = "select part_index, part_number, part_name, part_unit from parts where part_number like '%" + q2.upper() \
            + "%' or part_name like '%" + q2 + "%'"
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
    date_ent.delete(0, END)
    date_ent.insert(0, date_now())
    time_ent.delete(0, END)
    time_ent.insert(0, time_now())
    part_number_ent.delete(0, END)
    part_name_ent.delete(0, END)
    part_lot_ent.delete(0, END)
    qty_ent.delete(0, END)
    unit_ent.delete(0, END)
    received_by_ent.delete(0, END)
    delivered_by_ent.delete(0, END)
    relocated_ent.delete(0, END)
    relocated_ent.insert(0,"PENDING")

def add_new_element():
    date_sel = date_ent.get()
    time_sel = time_ent.get()
    part_number_sel = part_number_ent.get()
    part_name_sel = part_name_ent.get()
    part_lot_sel = part_lot_ent.get()
    qty_sel = qty_ent.get()
    unit_sel = part_unit_sel.get()
    received_by_sel = received_by_ent.get()
    delivered_by_sel = delivered_by_ent.get()
    relocated_sel = relocated_ent.get()

    query = "insert into supplies (date, time, part_number, part_name, lot, qty, unit, received_by, " \
            "delivered_by, relocated_flag) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    cursor.execute(query, (date_sel, time_sel, part_number_sel.upper(), part_name_sel.upper(), part_lot_sel.upper(), qty_sel, unit_sel,
                           received_by_sel.upper(), delivered_by_sel.upper(), relocated_sel))
    conn.commit()
    clear()

def log(text):
    # Gets or creates a logger
    logger = logging.getLogger(__name__)

    # set log level
    logger.setLevel(logging.WARNING)

    # define file handler and set formatter
    file_handler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
    file_handler.setFormatter(formatter)

    # add file handler to logger
    logger.addHandler(file_handler)

    # Logs
    #logger.debug('A debug message')
    #logger.info('An info message')
    #logger.warning('Something is not right.')
    #logger.error('A Major error has happened.')
    #logger.critical('Fatal error. Cannot continue')

    query = "insert into logs (text) values (%s)"

    cursor.execute(query, (text))
    conn.commit()


#***************************** ROOT **********************************
#*********************************************************************

root = Tk()

root.title("Supplies")

"""#Get the current screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
screen_size = str(screen_width) + "x" + str(screen_height)
root.geometry(screen_size)
"""
root.geometry("640x510+600+200")

font_columns_name = ('Arial',12,'bold') # normal or bold
font_wrap_title = ('Arial',12,'bold') # normal or bold
font_entry = ('Arial',11,'normal') # normal or bold
font_label = ('Arial',12,'bold') # normal or bold
font_button = ('Arial',11,'bold') # normal or bold

wrapper0 = LabelFrame(root, text="Search", font=font_wrap_title)
wrapper1 = LabelFrame(root, text="List", font=font_wrap_title)
wrapper2 = LabelFrame(root, text="Input", font=font_wrap_title)

wrapper0.grid(row=0, column=0, padx=PADX, pady=PADY, sticky=EW)
wrapper1.grid(row=1, column=0, padx=PADX, pady=PADY, sticky=EW)
wrapper2.grid(row=2, column=0, padx=PADX, pady=PADY, sticky=EW)

#*********************** Search *****************************
#************************************************************

q = StringVar()

search_lbl = LabelFrame(wrapper0, text="Part or Description", font=font_label)
search_lbl.grid(row=0, column=0, padx=PADX, pady=PADY, sticky=W)
search_ent = Entry(wrapper0, textvariable=q, font=font_entry)
search_ent.grid(row=1, column=0, padx=PADX, pady=PADY, sticky=W)
search_ent.bind('<Return>',search)
search_btn = Button(wrapper0, text="Search", command=search, font=font_button)
search_btn.grid(row=1, column=1, padx=PADX, pady=PADY, sticky=W)

#*********************** List *******************************
#************************************************************

trv = ttk.Treeview(wrapper1, columns=(1,2,3,4), show="headings", height="3")

verscrlbar = ttk.Scrollbar(wrapper1, orient="vertical", command=trv.yview)
verscrlbar.pack(side="right",fill="y")
trv["yscrollcommand"] = verscrlbar.set

trv.column(1, width=80)
trv.column(2, width=100)
trv.column(3, width=350)
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
part_number_sel = StringVar()
part_name_sel = StringVar()
part_lot_ent = StringVar()
qty_ent = StringVar()
part_unit_sel = StringVar()
received_by_ent = StringVar()
delivered_by_ent = StringVar()
relocated_ent = StringVar()


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
date_ent = DateEntry(wrapper2, selectmode='day', textvariable=date_ent, font=font_entry)
date_ent.grid(row=0, column=1, padx=PADX, pady=PADY, ipadx=10, sticky=W)
date_ent.insert(0,date_now())

time_lbl = Label(wrapper2, text="Time", font=font_label)
time_lbl.grid(row=1, column=0, padx=PADX, pady=PADY)
time_ent = Entry(wrapper2, textvariable=time_ent, font=font_entry)
time_ent.grid(row=1, column=1, padx=PADX, pady=PADY, sticky=W)
time_ent.insert(0,time_now())

part_number_lbl = Label(wrapper2, text="Part number", font=font_label)
part_number_lbl.grid(row=2, column=0, padx=PADX, pady=PADY)
part_number_ent = Entry(wrapper2, textvariable=part_number_sel, font=font_entry)
part_number_ent.grid(row=2, column=1, padx=PADX, pady=PADY, sticky=W)

part_name_lbl = Label(wrapper2, text="Part name", font=font_label)
part_name_lbl.grid(row=3, column=0, padx=PADX, pady=PADY)
part_name_ent = Entry(wrapper2, textvariable=part_name_sel, font=font_entry)
part_name_ent.grid(row=3, column=1, padx=PADX, pady=PADY, ipadx=100, sticky=W)

part_lot_lbl = Label(wrapper2, text="Lot", font=font_label)
part_lot_lbl.grid(row=4, column=0, padx=PADX, pady=PADY)
part_lot_ent = Entry(wrapper2, textvariable=part_lot_ent, font=font_entry)
part_lot_ent.grid(row=4, column=1, padx=PADX, pady=PADY, sticky=W)

qty_lbl = Label(wrapper2, text="Qty", font=font_label)
qty_lbl.grid(row=5, column=0, padx=PADX, pady=PADY)
qty_ent = Entry(wrapper2, textvariable=qty_ent, font=font_entry)
qty_ent.grid(row=5, column=1, padx=PADX, pady=PADY, sticky=W)

unit_lbl = Label(wrapper2, text="Unit", font=font_label)
unit_lbl.grid(row=6, column=0, padx=PADX, pady=PADY)
unit_ent = Entry(wrapper2, textvariable=part_unit_sel, font=font_entry)
unit_ent.grid(row=6, column=1, padx=PADX, pady=PADY, sticky=W)

list_received_by = ["ADRIANA","ALVARO","ANGEL","ANTONIO","BENITO","BRENDA","CERAFIN","CHAPO","CONCHA","DANIEL","DENIS"
    ,"FELIX","FELIPE","JAIME","JAVIER","JORGE","MARIA","MANUEL","OMAR","SILVERIO","SILVIA","RUBEN","RAFAEL",
                    "VILMAR","WILL"]

received_by_lbl = Label(wrapper2, text="Received by", font=font_label)
received_by_lbl.grid(row=7, column=0, padx=PADX, pady=PADY)
received_by_ent = ttk.Combobox(wrapper2, values=list_received_by, textvariable=received_by_ent, font=font_entry)
received_by_ent.grid(row=7, column=1, padx=PADX, pady=PADY, ipadx=100, sticky=W)

list_warehouse = ["CARLOS JIMENEZ","JUAN RUIZ","MAURICIO GARCIA"]

delivered_by_lbl = Label(wrapper2, text="Delivered by", font=font_label)
delivered_by_lbl.grid(row=8, column=0, padx=PADX, pady=PADY)
delivered_by_ent = ttk.Combobox(wrapper2, values=list_warehouse, textvariable=delivered_by_ent, font=font_entry)
delivered_by_ent.grid(row=8, column=1, padx=PADX, pady=PADY, ipadx=100, sticky=W)

list_relocated = ["PENDING","OK"]
relocated_lbl = Label(wrapper2, text="Relocated ?", font=font_label)
relocated_lbl.grid(row=9, column=0, padx=PADX, pady=PADY)
relocated_ent = ttk.Combobox(wrapper2, values=list_relocated, textvariable=relocated_ent, font=font_entry)
relocated_ent.grid(row=9, column=1, padx=PADX, pady=PADY, ipadx=50, sticky=W)
relocated_ent.insert(0,"PENDING")

add_btn = Button(wrapper2, text="OK", command=add_new_element, font=font_button, width=10)
add_btn.grid(row=10, column=0, padx=5, pady=3, sticky=EW)

clear_btn = Button(wrapper2, text="Clear", command=clear, font=font_button, width=10)
clear_btn.grid(row=10, column=1, padx=5, pady=3, sticky=W)


#delete_btn.grid(row=10, column=1, padx=5, pady=3, sticky=W)

trv.bind('<Double 1>', getrow)


root.mainloop()