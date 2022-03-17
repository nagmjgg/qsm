import pandas as pd
from tkinter import *
import tkinter as tk
import time
from datetime import date,datetime
import glob
import os
import math
from tkcalendar import Calendar

def find_last_file(folder, initials):  # folder: 'D:/shared_inventory/server files/', initials: 'available'
    location = folder + initials
    list_of_files = glob.glob(location + '*.csv')  # * means all if need specific format then *.csv
    filename = max(list_of_files, key=os.path.getctime)
    print(f"Last File > {filename}")
    return filename


def actual_date():
    date_initial_file = date.today().strftime("%Y-%m-%d")  # fecha actual ... colocar formato... date.strftime("%d/%m/%y")
    date_final_file = date.today()  # fecha actual ... colocar formato... date.strftime("%d/%m/%y")
    print(f" Actual date {date}")  # 2021-08-10
    return str(date_final_file)


# *** Fill new column with information of other column
# Example: extract_text_to_new_column(data,'tracking','lot','Lot',27,47)


def extract_text_to_new_column(dataframe, old_column, new_column, text_to_find,
                               initial_space, spaces):
    # dataframe_index = dataframe + '.index'
    for i in dataframe.index:
        # print(data['tracking'][i])
        if not pd.isna(dataframe[old_column][i]):

            if text_to_find in dataframe[old_column][i]:
                text_position = dataframe[old_column][i].find(text_to_find)
                text_initial_position = text_position + initial_space
                text_final_position = text_initial_position + spaces
                # print(f"{text_to_find} - text_position: {text_position}")
                # print(f"i: {i}, {dataframe[old_column][i]}")
                dataframe[new_column][i] = dataframe[old_column][i][text_initial_position: text_final_position]
                # print(f"expiration : {data['tracking'][i][9:19]}")
            else:
                pass


def date_now():
    date = datetime.now().strftime("%Y-%m-%d")
    return date


def time_now():
    time = datetime.now().strftime("%H:%M")
    return time


def sel_date():
    # Create Object
    root = Tk()

    # Set geometry
    root.geometry("400x400")

    # Add Calendar
    cal = Calendar(root, selectmode='day',
                   year=2020, month=5,
                   day=22)

    cal.pack(pady=20)


def log(message_text,  level):
    global script_name
    date_log = date_now()
    time_log = time_now()

    query = "insert into logs (date, time, script_name, text, level) values (%s, %s, %s, %s, %s)"

    cursor.execute(query, (date_log, time_log, script_name, message_text, level))
    conn.commit()


def validate_if_empty(widget):
    var = widget.get()
    if len(str(var)) == 0:
        messagebox.showerror(title="Error", message="Can't be empty")
        #print(f"{var} validate_if_empty: {0}")
        return 0
    else:
        return 1

def validate_if_numeric(widget):
    var = widget.get()
    if any(ch.isdigit() for ch in var):
        messagebox.showerror(title="Error", message="Can't be numeric")
        return 0
    else:
        return 1

def validate_if_text(widget):
    var = widget.get()
    if any (ch.isalpha() for ch in var):
        messagebox.showerror(title="Error", message="Can't be text")
        return 0
    else:
        #messagebox.showerror(title="Warning", message="Can't be text")
        return 1


def validate_if_empty_numeric(widget):
    empty_validation = validate_if_empty(widget)
    numeric_validation = validate_if_numeric(widget)

    validation_result = empty_validation + numeric_validation

    if validation_result == 2:

        return 1
    else:
        messagebox.showerror(title="Error", message="Can't be empty or numeric")
        return 0

def validate_if_empty_text(widget):
    empty_validation = validate_if_empty(widget)
    text_validation = validate_if_text(widget)

    validation_result = empty_validation + text_validation

    if validation_result == 2:
        return 1
    else:
        messagebox.showerror(title="Warning", message="Can't be empty or text")
        return 0

def load_db_data(table, db_connection):
    data = pd.read_sql('select * from ' + table, db_connection)
    return data

def load_csv_data(dataframe):
    folder = "D:/shared_inventory/server files/"
    filename = find_last_file(folder, dataframe)
    print(filename)
    data = pd.read_csv(filename, index_col='id', encoding='latin-1')
    return data

def dataframe_to_dictionary(csv_file_initials):
    # load data from csv file
    df_data = load_csv_data(csv_file_initials)
    df_data = df_data.to_dict()
    return df_data

def dataframe_columns(csv_file_initials):
    df_data = load_csv_data(csv_file_initials)
    df_data = df_data.to_dict()
    columns = list(df_data.keys())
    #print(f"columns: {columns}")
    return columns

def dataframe_columns_count(csv_file_initials):
    df_data = load_csv_data(csv_file_initials)
    df_data = df_data.to_dict()
    columns = list(df_data.keys())
    #print(f"columns: {columns}")
    columns_len = len(columns)
    #print(f"columns length: {columns_len}")

def dataframe_rows_count(csv_file_initials):
    df_data = load_csv_data(csv_file_initials)
    df_data = df_data.to_dict()
    columns = list(df_data.keys())
    rows = len(df_data[columns[0]])
    return rows

def create_insert_query_for_table(db_dataframe, database_table):
    # this function works together with create_cursor_insert_query_for_table() as a complement to create the next sentences
    #     #query = "insert into parts (col1, col2, col3, ...) values (%s, %s, %s, %s, ... )"
    #     #cursor.execute(query, (%s,%s,%s,%s...))
    # it takes the database columns for creating columns in query

    print(f"<<<  Text for query ok...>>>")

    columns = db_dataframe.columns
    columns_len = len(columns)

    first_db_column = columns[0]

    rows = len(db_dataframe[first_db_column])
    print(f" len {len(db_dataframe[first_db_column])}")

    text1 = "insert into "

    text2 = " ("

    query_columns = ""
    values_symbol = ""

    count = 0
    for i in columns:
        query_columns = query_columns + i
        values_symbol = values_symbol + "%s"
        if count < (columns_len - 1):
            query_columns += ", "
            values_symbol += ", "
            count += 1
        else:
            query_columns += ") "
            values_symbol += ")"
            count += 1

    text3 = " values ("
    #print(query_columns)

    text_columns = query_columns
    query = text1 + database_table + text2 + text_columns + text3 + values_symbol
    return query

def create_cursor_insert_query_for_table(csv_dataframe, dataframe_name, table):
    #this function works together with create_insert_query_for_table() as a complement to create the next sentences
    #query = "insert into parts (col1, col2, col3, ...) values (%s, %s, %s, %s, ... )"
    #cursor.execute(query, (%s,%s,%s,%s...))

    print(f"<<< Cursor insert text for query ok...>>>")

    # load data from csv file
    columns = csv_dataframe.columns

    # columns count
    columns_len = len(columns)
    #print(f"columns length: {columns_len}")

    #first database column
    first_db_column = columns[0]

    #rows count
    rows = len(csv_dataframe[first_db_column])
    #print(f" len {len(df_data[first_db_column])}")

    cursor_columns = ""
    cursor = ""
    count = 0
    for i in columns:
        cursor_columns += dataframe_name +"['" + i + "'][i]"
        if count < (columns_len - 1):
            cursor_columns += ", "
            count += 1
        else:
            cursor_columns += ""
            count += 1

    return cursor_columns