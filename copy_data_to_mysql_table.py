"""
Programm to input supplies devlivered to the different departments

V3 change of database from postgresql for mysql
v3.1 insert logging to db

"""

import os
import socket
import tkinter as tk
#from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import date, datetime
import pandas as pd
#from tkcalendar import DateEntry
#from datetime import date,datetime
#https://www.tutorialspoint.com/python_data_access/python_mysql_create_table.htm
import mysql.connector

#import socket   #identify ip address

db_name="qsm"
username='sql'
user_password='Quality01'
db_host='192.168.210.25'
db_port= '3306'

#establishing the connection
conn = mysql.connector.connect(database=db_name, user=username, password=user_password, host=db_host, port=db_port)

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

def get_filename():
    filename_path = __file__
    filename = filename_path.split("/")
    filename = filename_path.split("\\")
    print(filename_path)
    return filename[-1]

def get_ip_address():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    return host_ip


#fixed value for logging porpuses
pc_login = os.getlogin()
file_name = get_filename()
ip_address = get_ip_address()

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
    unit_ent.insert(0, "ea")
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

    validate_if_empty(received_by_sel)
    validate_if_numeric(received_by_sel)
    validate_if_empty(delivered_by_sel)
    validate_if_numeric(delivered_by_sel)

    query = "insert into supplies (date, time, part_number, part_name, lot, qty, unit, received_by, " \
            "delivered_by, relocated_flag) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    cursor.execute(query, (date_sel, time_sel, part_number_sel.upper(), part_name_sel.upper(), part_lot_sel.upper(), qty_sel, unit_sel,
                           received_by_sel.upper(), delivered_by_sel.upper(), relocated_sel))
    conn.commit()
    clear()
    message = "add_new_element ok"
    log(message,"info")

def log(message_text,  level):
    global script_name
    global file_name
    date_log = date_now()
    time_log = time_now()
    login = pc_login


    query = "insert into logs (date, time, script_name, ip_address, pc_login, text, level) values (%s, %s, %s, %s, %s, %s, %s)"

    cursor.execute(query, (date_log, time_log, file_name, ip_address, login, message_text, level))
    conn.commit()

def validate_if_empty(widget):
    if len(widget) == 0:
        text = f"{widget} can not be empty"
        messagebox.showerror(title="Empty Field", message=text)
        return 0
    else:
        return 1

def validate_if_numeric(widget):
    if widget.isnumeric():
        text = f"{widget} can not be numeric"
        messagebox.showerror(title="Numeric Field", message=text)
        return 0
    else:
        return 1

def validate_if_empty_numeric(widget):
    empty_validation = validate_if_empty(widget)
    numeric_validation = validate_if_numeric(widget)

    validation_result = empty_validation + numeric_validation

    if validation_result == 2:
        return 1
    else:
        return 0


#***************************** ROOT **********************************
#*********************************************************************

root = tk.Tk()
log("mensaje de prueba","info")
root.title("Warehouse Outgoing Supplies")

"""#Get the current screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
screen_size = str(screen_width) + "x" + str(screen_height)
root.geometry(screen_size)
"""


font_columns_name = ('Arial',12,'bold') # normal or bold
font_wrap_title = ('Arial',12,'bold') # normal or bold
font_entry = ('Arial',11,'normal') # normal or bold
font_label = ('Arial',12,'bold') # normal or bold
font_button = ('Arial',11,'bold') # normal or bold

#*****

df = pd.DataFrame()

#Set data folder
folder = "D:/shared_inventory/server files/"

df = pd.read_csv(folder + 'Combined_Inventory_Onhand.csv', encoding='latin_1')
df.head()
print(df)
df.columns
print(df.columns)
df = df.drop(columns=['Unnamed: 0'])
print(df)
print(df.columns)


root.geometry("640x660+600+200")
root.mainloop()