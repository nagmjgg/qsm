import pandas as pd
from tkinter import *
import tkinter as tk
import time
from datetime import date
import glob
import os
import math


def find_last_file(folder, initials):  # folder: 'D:/shared_inventory/server files/', initials: 'available'
    location = folder + initials
    list_of_files = glob.glob(location + '*.csv')  # * means all if need specific format then *.csv
    filename = max(list_of_files, key=os.path.getctime)
    print(f"Last File > {filename}")
    return filename


def actual_date():
    date_initial_file = date.today().strftime(
        "%Y-%m-%d")  # fecha actual ... colocar formato... date.strftime("%d/%m/%y")
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

