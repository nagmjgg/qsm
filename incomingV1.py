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

date = date.today() #fecha actual ... colocar formato... date.strftime("%d/%m/%y")
print(f" Actual date {date}")     #2021-08-10

#Set data folder
folder = "C:/Users/rosun/Desktop/"

incoming_ingredients = pd.DataFrame()

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
print("** Incoming_ingredients File ** >> Open file in progress")
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)

incoming_ingredients = pd.read_csv(filename, encoding='latin1') #,header=3)

#delete last row
print(f"Delete last row... ok")
incoming_ingredients = incoming_ingredients.iloc[:-2]

print(f"Rename Columns... ok")
incoming_ingredients.columns = ['Part', 'Description', 'UOM', 'OnHand', 'Allocated', 'NotAvailable','DropShip', 'Available', 'OnOrder', 'Committed', 'Short']

#Sort data for "Part Number"
incoming_ingredients_sorted=incoming_ingredients.sort_values(by='Part')
print("Data sorted ok")

#exportar archivo 
try:
    file_name = folder+'incoming_ingredients_'+str(date)+'.csv'
    incoming_ingredients_sorted.to_csv(file_name)
    print(f"filename: {file_name}")
    print(f"File exported ok... {file_name}")
except:
    print("Error... File Permision denied")
    print(f"File exported Not ok...")
    

