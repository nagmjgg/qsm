import pandas as pd
from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilename
import time
from datetime import date
import glob
import os
import math

#texto en colores
#main_window = Tk()
#Display parameters
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

def find_last_file(folder,initials):  #folder: 'D:/shared_inventory/server files/', initials: 'available'
    location = folder + initials
    list_of_files = glob.glob(location + '*.csv') # * means all if need specific format then *.csv
    filename = max(list_of_files, key=os.path.getctime)
    print(f"Last File > {filename}")
    return filename

#Set data folder
folder = "D:/shared_inventory/server files/"

#**********************************************
#   ************ OnHand File ***********
#**********************************************
print("")
print("***** Combined  ******")

combined = pd.DataFrame()


#*************** opening file automatically *****************

initial_filename_combined = find_last_file('D:/shared_inventory/server files/','Combined_')
print(f"opening file > {initial_filename_combined}")

#*************** opening file automatically *****************


try:
    combined = pd.read_csv(initial_filename_combined, encoding='latin1')
except:
    print(f"opening file > {initial_file_name_combined}... doesn't exist")


#Total quantity and final locations with qty

#order by Part_# and Location
combined = combined.sort_values(by=['part_number','location'],ascending=True)
combined.reset_index()

#create column final_locations
combined['final_locations'] = ""

#create column qty_total
combined['qty_total'] = 0

#join data in new column 'final_locations'
for i in combined.index:
    
    try:
        if combined['location'][i-1]:
            if(combined['location'][i] == combined['location'][i-1] and combined['part_number'][i] == combined['part_number'][i+1]):
                combined['final_locations'][i] = combined['final_location'][i+1] + ", " + combined['location'][i] + "(" + combined['qty'][i] + ")"
            else:
                if (combined['location'][i] == combined['location'][i-1]):
                    combined['final_locations'][i] = combined['location'][i] + "(" + combined['qty'][i] + ")"
                else:
                    if(combined['location'][i] == combined['location'][i+1]):
                        combined['final_locations'][i] = combined['final_locations'][i+1] + ", " + combined['location'][i] + "(" + combined['qty'][i] + ")"
                    else:
                        combined['final_locations'][i] = combined['location'][i] + "(" + combined['qty'][i] + ")"
    except:
        pass
        




