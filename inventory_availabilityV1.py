import pandas as pd
from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilename
import time
from datetime import date

#main_window = Tk()

#Display parameters
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

date_initial_file = date.today().strftime("%Y%m%d") #fecha actual ... colocar formato... date.strftime("%d/%m/%y")
date_final_file = date.today() #fecha actual ... colocar formato... date.strftime("%d/%m/%y")
print(f" Actual date {date}")     #2021-08-10

#Set data folder
folder = "C:/Users/rosun/Desktop/"

inventory_availability = pd.DataFrame()

'''
#ask for the initial file
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
print("** inventory_availability File ** >> Open file in progress")
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)
'''


#opening file automatically
initial_filename = folder+'inventory_availability_'+str(date_initial_file)+'.csv'
print(f"opening file > {initial_filename}")


try:
    inventory_availability = pd.read_csv(initial_filename, encoding='latin1',header=3)
except: 
    print(f"opening file > {initial_filename}... doesn't exist")


#delete last row
print(f"Delete last row... ok")
inventory_availability = inventory_availability.iloc[:-2]

print(f"Rename Columns... ok")
inventory_availability.columns = ['Part', 'Description', 'UOM', 'OnHand', 'Allocated', 'NotAvailable', 
                'DropShip', 'Available', 'OnOrder', 'Committed', 'Short']

#Sort data for "Part Number"
inventory_availability_sorted=inventory_availability.sort_values(by='Part')
print("Data sorted ok")

#exportar archivo 
try:
    file_name = folder+'inventory_availability_'+str(date_final_file)+'.csv'
    inventory_availability_sorted.to_csv(file_name)
    print(f"filename: {file_name}")
    print(f"File exported ok... {file_name}")
except:
    print("Error... File Permision denied")
    print(f"File exported Not ok...")
    
inventory_availability.columns
''' 
inventory_availability.columns
Out[59]: Index(['Part', 'Description', 'UOM', 'OnHand', 'Allocated', 'NotAvailable', 'DropShip', 'Available', 'OnOrder', 'Committed', 'Short'], dtype='object')
'''

inventory_availability
inventory_availability["Commited_flag"]=0



'''
for i in inventory_availability.index:
    #print(i)
    print(data["Location"][i])
    if inventory_availability["Committed"][i] > 0:
        inventory_availability["Commited_flag"][i]=1
    else:
        pass
print("Active location flag  ok")

'''