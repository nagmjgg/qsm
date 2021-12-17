# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 12:54:28 2021

@author: mgarcia
"""

import pandas as pd
from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilename
import time
from datetime import date
import glob
import os
import math
import qsm_functions

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

def find_last_file(folder,initials):  #folder: 'D:/shared_inventory/server files/', initials: 'available'
    location = folder + initials
    list_of_files = glob.glob(location + '*.csv') # * means all if need specific format then *.csv
    filename = max(list_of_files, key=os.path.getctime)
    print(f"Last File > {filename}")
    return filename



def actual_date():
    date_initial_file = date.today().strftime("%Y-%m-%d") #fecha actual ... colocar formato... date.strftime("%d/%m/%y")
    date_final_file = date.today() #fecha actual ... colocar formato... date.strftime("%d/%m/%y")
    print(f" Actual date {date}")     #2021-08-10
    return str(date_final_file)


# *** Fill new column with information of other column
# Example: extract_text_to_new_column(data,'tracking','lot','Lot',27,47)

def extract_text_to_new_column(dataframe, old_column, new_column, text_to_find,
                               initial_space,spaces):
    #dataframe_index = dataframe + '.index'
    for i in dataframe.index:
        #print(data['tracking'][i])
        if not pd.isna(dataframe[old_column][i]):
            
            if text_to_find in dataframe[old_column][i]:
                text_position = dataframe[old_column][i].find(text_to_find)            
                text_initial_position = text_position + initial_space
                text_final_position = text_initial_position + spaces
                #print(f"{text_to_find} - text_position: {text_position}")
                #print(f"i: {i}, {dataframe[old_column][i]}")
                dataframe[new_column][i] = dataframe[old_column][i][text_initial_position : text_final_position]
                #print(f"expiration : {data['tracking'][i][9:19]}")
            else:
                pass

filename = "manufacturing_jobs.csv"
folder = "D:/shared_inventory/server files/"

#**********************************************
#   ************ Jobs File ***********
#**********************************************
print("")
print("***** Jobs  ******")

jobs = pd.DataFrame()


#*************** opening file automatically *****************

initial_filename = find_last_file('D:/shared_inventory/server files/','manufacturing_jobs')
print(f"opening file > {initial_filename}")


try:
    jobs = pd.read_csv(initial_filename, encoding='latin1')
except: 
    print(f"opening file > {initial_file_name}... doesn't exist")



#************************************************************
'''
onhand.columns
['date_deposit_paid', 'est_\ncompl_\ndate', 'wo_#', 'po_#', 'lot_#_', 
 'sales_rep', 'customer', 'total_count', 'bottle_fg_#', 'code', 
 'cap/tab_specs', 'product_bg_#', 'mfg_status', 'packaging_status', 
 'mg_per_cap/tab', 'bulkbottle_count']
'''

"""


#delete first row
#onhand = onhand.drop(labels=0, axis=0)

#delete unused columns
onhand = onhand.drop(labels=['Unnamed: 6', 'Unnamed: 7'], axis=1)

"""
#Normalize columns
jobs_columns = jobs.columns

#jobs_columns = [x.replace("Unnamed: 3","unit") for x in jobs_columns]
jobs_columns = [x.replace(" ","_") for x in jobs_columns]
jobs_columns = [x.replace("_/_","") for x in jobs_columns]
#jobs_columns = [[x = x.rstrip(x[-1])] for x in jobs_columns if x[-1] == "_"]
jobs_columns = [x.lower() for x in jobs_columns]


jobs.columns = jobs_columns
print(jobs_columns)

#delete last row
#onhand = onhand.iloc[:-2]

#Sort data for "Part Number"
jobs_sorted=jobs.sort_values(by='wo_#')
print("Data sorted ok")

#exportar archivo 
try:
    file_name = folder+'jobs_out_'+actual_date()+'.csv'
    jobs_sorted.to_csv(file_name)
    
except:
    print("Error... File Permision denied")
    
print(f"File exported ok... {file_name}")