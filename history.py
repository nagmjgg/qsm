# -*- coding: utf-8 -*-
# *** Spyder Python Console History Log ***

## ---(Thu Jul 29 12:05:47 2021)---
import pandas as pd
runfile('C:/Users/rosun/.spyder-py3/temp.py', wdir='C:/Users/rosun/.spyder-py3')
debugfile('C:/Users/rosun/.spyder-py3/temp.py', wdir='C:/Users/rosun/.spyder-py3')

## ---(Tue Aug  3 11:51:26 2021)---
runfile('C:/Users/rosun/.spyder-py3/onhand.py', wdir='C:/Users/rosun/.spyder-py3')
debugfile('C:/Users/rosun/.spyder-py3/onhand.py', wdir='C:/Users/rosun/.spyder-py3')

## ---(Mon Aug  9 09:04:01 2021)---
onhand = pd.read_csv(filename, header=3)
runfile('C:/Users/rosun/.spyder-py3/onhand.py', wdir='C:/Users/rosun/.spyder-py3')

## ---(Mon Aug  9 09:17:08 2021)---
runfile('C:/Users/rosun/.spyder-py3/onhandV1_1.py', wdir='C:/Users/rosun/.spyder-py3')
import pandas as pd
from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilename
#main_window = Tk()
import pandas as pd
pd.set_option('display.max_rows', 500)
import pandas as pd
runcell(0, 'C:/Users/rosun/.spyder-py3/onhandV1_1.py')
import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
DIRECTORY = "C:/Users/rosun/Desktop"
onhand = pd.DataFrame()
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
onhand = onhand.drop(labels=1, axis=0)
onhand = onhand.drop(labels=0, axis=1)
#onhand = onhand.drop(labels=0, axis=1)
runfile('C:/Users/rosun/.spyder-py3/onhandV1_1.py', wdir='C:/Users/rosun/.spyder-py3')
onhand.write_csv('out.csv')
onhand.to_csv('out.csv')
os.getcwd()
import os
os.getcwd
os.getcwd()
onhand.unique()
onhand.unique
onhand['Location']]unique
onhand['Location']unique
onhand['Location'].unique
pd.set_option('display.max_rows', 500)
)
pd.set_option('display.width', 1000)
onhand['Location'].unique
onhand['Location'].unique()
runfile('C:/Users/rosun/.spyder-py3/onhandV1_1.py', wdir='C:/Users/rosun/.spyder-py3')
onhan_sorted = onhand_sorted.drop(labels=0, axis=0)
data = onhand_sorted.copy()
data.available = 0
for i in data:
    if data.Location in location_available:
        data.available=1
runfile('C:/Users/rosun/.spyder-py3/onhandV1_1.py', wdir='C:/Users/rosun/.spyder-py3')
onhand.drop(labels=0, axis=0)
onhand = onhand.drop(labels=0, axis=0)
onhand = onhand.iloc[:-1]
onhand = onhand.iloc[:-2]
runfile('C:/Users/rosun/.spyder-py3/onhandV1_1.py', wdir='C:/Users/rosun/.spyder-py3')

## ---(Tue Aug 10 06:34:47 2021)---
runfile('C:/Users/rosun/.spyder-py3/onhandV1_1.py', wdir='C:/Users/rosun/.spyder-py3')
onhand_sorted
data = onhand_sorted.copy()
s
onhand.to_csv(folder+'out.csv')
folder = "C:/Users/rosun/Desktop/"
onhand.to_csv(folder+'out.csv')
data["available"] = 0
for i in data:
    if data.Location in location_available:
        data.available=1
for i in data:
    if data["Location"] in location_available:
        data["available"]=1
if data["Location"][i] in location_available:
for i in data:
    if data["Location"][i] in location_available:
        data["available"]=1
print(i)
for i in data:
    print(i)
    if data["Location"][i] in location_available:
        data["available"]=1
data["Location"][1]
data["Location"][2]
if data["Location"][2] in location_available:
    print("ok")
if data["Location"][967] in location_available:
    print("ok")
for i in data:
    print(i)
data.describe()
data.shape()
data.shape
data.shape[0]
for i in range(qty):
    if data["Location"][i] in location_available:
        data["available"]=1
qty = data.shape[0]
for i in range(qty):
    if data["Location"][i] in location_available:
        data["available"]=1
for i in range(qty):
    if data["Location"][i] in location_available:
        data["available"][i]=1
data["available"][i]=1
data["available"][2]=1
data["available"][2]
data["available"][4]=1
for i in range(qty):
    print(i)
    if data["Location"][i] in location_available:
        data["available"][i]=1
for i in range(qty):
    print(i)
    data["available"][i]=1
for i in range(0,qty):
    print(i)
    if data["Location"][i] in location_available:
        data["available"][i]=1
    else:
        data["available"][i]=0
for i in range(0,qty):
    print(i)
    print(data["Location"][i])
    if data["Location"][i] in location_available:
        data["available"][i]=1
    else:
        data["available"][i]=0
for i in range(1,qty):
    print(i)
    print(data["Location"][i])
    if data["Location"][i] in location_available:
        data["available"][i]=1
    else:
        data["available"][i]=0
for i in data["Index"]:
    print(i)
    print(data["Location"][i])
    if data["Location"][i] in location_available:
        data["available"][i]=1
    else:
        data["available"][i]=0
data['Index'][0]
data['index'][0]
data[index][0]
data[265]
data.index
data[index]
data["index"]
data.index
for i in data.index:
    print(i)
    print(data["Location"][i])
    if data["Location"][i] in location_available:
        data["available"][i]=1
    else:
        data["available"][i]=0
onhand.to_csv(folder+'out.csv')
data.columns
onhand = onhand.drop(labels=['Unnamed: 6', 'Unnamed: 7'], axis=1)
runfile('C:/Users/rosun/.spyder-py3/onhandV1_1.py', wdir='C:/Users/rosun/.spyder-py3')
data.to_csv(folder+'out.csv')
data_filtered = data[data["available"]=1]
data_filtered = data[data["available"]==1]
data_filtered.to_csv(folder+'out.csv')
data.year
d.isoformat()
d = datetime
d.isoformat()
d = datetime.now()
import time
time
date.today
date.today()
from datetime import date
date.today()
date = date.today()
date
print(date)
data_filtered.to_csv(folder+'OnHand_'+date'.csv')
data_filtered.to_csv(folder+'OnHand_'+date+'.csv')
data_filtered.to_csv(folder+'OnHand_'+str(date)+'.csv')

## ---(Fri Aug 13 06:40:11 2021)---
runfile('C:/Users/rosun/.spyder-py3/onhandV1_1.py', wdir='C:/Users/rosun/.spyder-py3')

## ---(Mon Aug 16 06:35:24 2021)---
runfile('C:/Users/rosun/.spyder-py3/onhandV1_1.py', wdir='C:/Users/rosun/.spyder-py3')
onhand['Location'].unique()
location_available = ['Expired Powders','PS Stock Bin In Process', 'Quarantine Packaging Materials', 
location_available = ['Expired Powders','PS Stock Bin In Process', 'Quarantine Packaging Materials',
                      'Quarantine Powders/ Receiving','Refrigerator', 'Stock Bin # A0', 'Stock Bin # A1',
       'Stock Bin # A10', 'Stock Bin # A11', 'Stock Bin # A13',
       'Stock Bin # A17', 'Stock Bin # A18', 'Stock Bin # A21',
       'Stock Bin # A22', 'Stock Bin # A23', 'Stock Bin # A25',
       'Stock Bin # A26', 'Stock Bin # A27', 'Stock Bin # A28',
       'Stock Bin # A29', 'Stock Bin # A30', 'Stock Bin # A33',
       'Stock Bin # A34', 'Stock Bin # A35', 'Stock Bin # A36',
       'Stock Bin # A37', 'Stock Bin # A38', 'Stock Bin # A39',
       'Stock Bin # A40', 'Stock Bin # A6', 'Stock Bin # A9',
       'Stock Bin # B10', 'Stock Bin # B11', 'Stock Bin # B12',
       'Stock Bin # B13', 'Stock Bin # B14', 'Stock Bin # B15',
       'Stock Bin # B16', 'Stock Bin # B17', 'Stock Bin # B18',
       'Stock Bin # B19', 'Stock Bin # B2', 'Stock Bin # B21',
       'Stock Bin # B22', 'Stock Bin # B23', 'Stock Bin # B24',
       'Stock Bin # B25', 'Stock Bin # B26', 'Stock Bin # B28',
       'Stock Bin # B3', 'Stock Bin # B34', 'Stock Bin # B35',
       'Stock Bin # B36', 'Stock Bin # B38', 'Stock Bin # B4',
       'Stock Bin # B40', 'Stock Bin # B5', 'Stock Bin # B6',
       'Stock Bin # B7', 'Stock Bin # B8', 'Stock Bin # B9',
       'Stock Bin # C1', 'Stock Bin # C10', 'Stock Bin # C11',
       'Stock Bin # C12', 'Stock Bin # C13', 'Stock Bin # C14',
       'Stock Bin # C15', 'Stock Bin # C16', 'Stock Bin # C17',
       'Stock Bin # C18', 'Stock Bin # C19', 'Stock Bin # C2',
       'Stock Bin # C21', 'Stock Bin # C22', 'Stock Bin # C23',
       'Stock Bin # C24', 'Stock Bin # C25', 'Stock Bin # C26',
       'Stock Bin # C27', 'Stock Bin # C28', 'Stock Bin # C29',
       'Stock Bin # C30', 'Stock Bin # C31', 'Stock Bin # C32',
       'Stock Bin # C33', 'Stock Bin # C35', 'Stock Bin # C36',
       'Stock Bin # C37', 'Stock Bin # C38', 'Stock Bin # C39',
       'Stock Bin # C4', 'Stock Bin # C40', 'Stock Bin # C41',
       'Stock Bin # C5', 'Stock Bin # C6', 'Stock Bin # C7',
       'Stock Bin # C8', 'Stock Bin # C9', 'Stock Bin # D1',
       'Stock Bin # D10', 'Stock Bin # D11', 'Stock Bin # D12',
       'Stock Bin # D13', 'Stock Bin # D14', 'Stock Bin # D15',
       'Stock Bin # D16', 'Stock Bin # D17', 'Stock Bin # D18',
       'Stock Bin # D19', 'Stock Bin # D2', 'Stock Bin # D20',
       'Stock Bin # D21', 'Stock Bin # D22', 'Stock Bin # D23',
       'Stock Bin # D24', 'Stock Bin # D3', 'Stock Bin # D4',
       'Stock Bin # D5', 'Stock Bin # D6', 'Stock Bin # D7',
       'Stock Bin # D8', 'Stock Bin # D9', 'Stock Bin # E1',
       'Stock Bin # E10', 'Stock Bin # E11', 'Stock Bin # E12',
       'Stock Bin # E13', 'Stock Bin # E14', 'Stock Bin # E15',
       'Stock Bin # E16', 'Stock Bin # E17', 'Stock Bin # E18',
       'Stock Bin # E19', 'Stock Bin # E2', 'Stock Bin # E20',
       'Stock Bin # E21', 'Stock Bin # E22', 'Stock Bin # E23',
       'Stock Bin # E24', 'Stock Bin # E3', 'Stock Bin # E4',
       'Stock Bin # E5', 'Stock Bin # E6', 'Stock Bin # E7',
       'Stock Bin # E8', 'Stock Bin # E9', 'Stock Bin In Process','Warehouse Floor']
data = onhand_sorted.copy()
print("Data copied ok")
data["available"] = 0
#Totals
qty = data.shape[0]
date = date.today() #fecha actual ... colocar formato... date.strftime("%d/%m/%y")
print(f" Actual date {date}")     #2021-08-10
#columns
data.columns
data.drop
for i in data.index:
#print(i)
for i in data.index:
    #print(i)
    print(data["Location"][i])
    if data["Location"][i] in location_available:
        data["available"][i]=1
    else:
        data["available"][i]=0
print("Active location flag  ok")
data_filtered = data[data["available"]==1]
print("Data filtered ok")
#onhand.describe()
#main_window.mainloop()
#exportar archivo 
data_filtered.to_csv(folder+'OnHand_'+str(date)+'.csv')
print("File exported ok")
data_filtered.to_csv(folder+'OnHand_'+str(date)+'.csv')

try:
    data_filtered.to_csv(folder+'OnHand_'+str(date)+'.csv')
except:
    print("Error... File Permision denied")

## ---(Wed Aug 18 09:28:49 2021)---
runfile('C:/Users/rosun/.spyder-py3/onhandV1_1.py', wdir='C:/Users/rosun/.spyder-py3')
data_filtered.sort_values(by="Part_Number")
data_filtered.sort_values(by='Part_Number')
data_filtered.sort_values(by='Part Number')
runfile('C:/Users/rosun/.spyder-py3/onhandV1_1.py', wdir='C:/Users/rosun/.spyder-py3')
data_location = data(data["Location"]=='Stock Bin In Process')
data_location = data(data["Location"]='Stock Bin In Process')
data
data["Location"]
data(data["Location"]='Warehouse Floor')
data[data["Location"]='Warehouse Floor']
data[data["Location"]=='Warehouse Floor']
data_location = data[data["Location"]='Stock Bin In Process']
data_location = data[data["Location"]=='Stock Bin In Process']
data_location.sort_values(by="Part Number")
runfile('C:/Users/rosun/.spyder-py3/onhandV1_1.py', wdir='C:/Users/rosun/.spyder-py3')
onhand['Location'].unique()
runfile('C:/Users/rosun/.spyder-py3/onhandV1_1.py', wdir='C:/Users/rosun/.spyder-py3')
runfile('C:/Users/rosun/.spyder-py3/incomingV1.py', wdir='C:/Users/rosun/.spyder-py3')
incoming_ingredients.columns
incoming_ingredients.columns = ['id', 'PO Date', 'PO No', 'Vendor', 'Part #', 'Ingredient/Component', 
        'Qty Ordered', 'Un', 'Date/Time Recvd', 'Qty Recvd', 'Lot No Recvd', 
        'Recvd By', 'AFL POs', 'Quality Date', 'Quantem POs', 'Identitity Confirmed (above 80%) Date', 
        'Summit - Vitamins / Minerals / Amino Acids', 'Quality Confirmed Date', 
        'Product Checked', 'CoA/CoC Recvd', 'Inventory Added']
runfile('C:/Users/rosun/.spyder-py3/incomingV1.py', wdir='C:/Users/rosun/.spyder-py3')
runfile('C:/Users/rosun/.spyder-py3/onhandV1_1.py', wdir='C:/Users/rosun/.spyder-py3')
runcell(0, 'C:/Users/rosun/.spyder-py3/onhandV1_1.py')
onhand = onhand.drop(labels=0, axis=0)
runfile('C:/Users/rosun/.spyder-py3/incomingV1.py', wdir='C:/Users/rosun/.spyder-py3')
incoming_ingredients = incoming_ingredients.drop(labels=[0,1], axis=0)
runfile('C:/Users/rosun/.spyder-py3/incomingV1.py', wdir='C:/Users/rosun/.spyder-py3')
incoming_ingredients = incoming_ingredients.iloc[:-2]
incoming_ingredients.columns
incoming_ingredients.columns = ['Part', 'Description', 'UOM', 'OnHand', 'Allocated', 'NotAvailable', 
                'DropShip', 'Available', 'OnOrder', 'Committed', 'Short']
runfile('C:/Users/rosun/.spyder-py3/incomingV1.py', wdir='C:/Users/rosun/.spyder-py3')
try:
    file_name = folder+'incoming_ingredients_'+str(date)+'.csv'
    incoming_ingredients_sorted.to_csv(file_name)
    print(f"filename: {file_name}")

except:
    print("Error... File Permision denied")
runfile('C:/Users/rosun/.spyder-py3/incomingV1.py', wdir='C:/Users/rosun/.spyder-py3')
runfile('C:/Users/rosun/.spyder-py3/onhandV1_1.py', wdir='C:/Users/rosun/.spyder-py3')
runfile('C:/Users/rosun/.spyder-py3/inventory_availabilityV1.py', wdir='C:/Users/rosun/.spyder-py3')
inventory_availability.columns
data_inventory = inventory_availability.copy()
onhand.columns
data_onhand = data_filtered.copy()
merge_inner = pd.merge(left=onhand, right=data_inventory, left_on="Part Number", right_on="Part")
date_init = date.today().strftime("%y%m%d") #fecha actual ... colocar formato... date.strftime("%d/%m/%y")
date_init = date.today().strftime("%yy%m%d") #fecha actual ... colocar formato... date.strftime("%d/%m/%y")
date_init = date.today().strftime("%Y%m%d") #fecha actual ... colocar formato... date.strftime("%d/%m/%y")
runfile('C:/Users/rosun/.spyder-py3/onhandV1_1.py', wdir='C:/Users/rosun/.spyder-py3')
runfile('C:/Users/rosun/.spyder-py3/inventory_availabilityV1.py', wdir='C:/Users/rosun/.spyder-py3')
runfile('C:/Users/rosun/.spyder-py3/onhandV1_1.py', wdir='C:/Users/rosun/.spyder-py3')
runfile('C:/Users/rosun/.spyder-py3/inventory_availabilityV1.py', wdir='C:/Users/rosun/.spyder-py3')

## ---(Tue Sep  7 07:22:01 2021)---
runfile('C:/Users/rosun/.spyder-py3/onhandV1_1.py', wdir='C:/Users/rosun/.spyder-py3')
runfile('C:/Users/rosun/.spyder-py3/inventory_availabilityV1.py', wdir='C:/Users/rosun/.spyder-py3')
runfile('C:/Users/rosun/.spyder-py3/onhandV1_1.py', wdir='C:/Users/rosun/.spyder-py3')
onhand_available[data_available] = 0
onhand_available["data_available"] = 0
onhand_available["data_available_flag"] = 0
onhand_available.reindex
onhand_available.reset_index
onhand_available.reset_index(inplace=True)

## ---(Thu Sep  9 15:36:20 2021)---
runfile('C:/Users/rosun/.spyder-py3/onhandV1_1.py', wdir='C:/Users/rosun/.spyder-py3')
runfile('C:/Users/rosun/.spyder-py3/inventory_availabilityV1.py', wdir='C:/Users/rosun/.spyder-py3')
runfile('C:/Users/rosun/.spyder-py3/onhandV1_1.py', wdir='C:/Users/rosun/.spyder-py3')
runfile('C:/Users/rosun/.spyder-py3/inventory_availabilityV1.py', wdir='C:/Users/rosun/.spyder-py3')
runfile('C:/Users/rosun/.spyder-py3/onhandV1_1.py', wdir='C:/Users/rosun/.spyder-py3')
runfile('C:/Users/rosun/.spyder-py3/inventory_availabilityV1.py', wdir='C:/Users/rosun/.spyder-py3')
runfile('C:/Users/rosun/.spyder-py3/onhandV1_1.py', wdir='C:/Users/rosun/.spyder-py3')
runfile('C:/Users/rosun/.spyder-py3/inventory_availabilityV1.py', wdir='C:/Users/rosun/.spyder-py3')

## ---(Thu Sep 16 06:55:04 2021)---
runfile('C:/Users/rosun/.spyder-py3/onhandV1_1.py', wdir='C:/Users/rosun/.spyder-py3')
runfile('C:/Users/rosun/.spyder-py3/inventory_availabilityV1.py', wdir='C:/Users/rosun/.spyder-py3')
runfile('C:/Users/rosun/.spyder-py3/onhandV1_1.py', wdir='C:/Users/rosun/.spyder-py3')
runfile('C:/Users/rosun/.spyder-py3/inventory_availabilityV1.py', wdir='C:/Users/rosun/.spyder-py3')
runfile('C:/Users/rosun/.spyder-py3/qsm_merge.py', wdir='C:/Users/rosun/.spyder-py3')

## ---(Tue Sep 21 14:57:45 2021)---
runfile('C:/Users/rosun/.spyder-py3/onhandV1_1.py', wdir='C:/Users/rosun/.spyder-py3')
onhand['Location'].unique()
runfile('C:/Users/rosun/.spyder-py3/qsm_merge.py', wdir='C:/Users/rosun/.spyder-py3')
data_location.sort_values(by=["Part Number","Location")
data_location.sort_values(by=("Part Number","Location"))
data_location.sort_values(by=["Part Number","Location"])
print(data["Location"][i][0:5])
runfile('C:/Users/rosun/.spyder-py3/onhandV1_1.py', wdir='C:/Users/rosun/.spyder-py3')
runfile('C:/Users/rosun/.spyder-py3/qsm_merge.py', wdir='C:/Users/rosun/.spyder-py3')
runfile('C:/Users/rosun/.spyder-py3/incomingV1.py', wdir='C:/Users/rosun/.spyder-py3')
incoming_ingredients = pd.read_csv(filename, encoding='latin1',header=3)
incoming_ingredients = incoming_ingredients.iloc[:-2]
incoming_ingredients = pd.read_csv(filename, encoding='latin1',header=3)
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
incoming_ingredients = pd.read_csv(filename, encoding='latin1',header=3)
incoming_ingredients = pd.read_csv(filename, encoding='latin1') #,header=3)
runfile('C:/Users/rosun/.spyder-py3/incomingV1.py', wdir='C:/Users/rosun/.spyder-py3')
runfile('C:/Users/rosun/.spyder-py3/qsm_merge.py', wdir='C:/Users/rosun/.spyder-py3')

## ---(Wed Sep 29 07:35:12 2021)---
runfile('C:/Users/rosun/.spyder-py3/qsm_merge.py', wdir='C:/Users/rosun/.spyder-py3')

## ---(Thu Sep 30 07:43:21 2021)---
runfile('C:/Users/rosun/.spyder-py3/qsm_merge.py', wdir='C:/Users/rosun/.spyder-py3')

## ---(Tue Oct  5 13:47:59 2021)---
print('\x1b[6;30;42m' + '***** Onhand  ******' + 'x1b[0m')
runfile('C:/Users/rosun/.spyder-py3/qsm_merge.py', wdir='C:/Users/rosun/.spyder-py3')
print('\x1b[6;30;42m' + '***** Onhand & availability Joined ******' + 'x1b]0m') 
runfile('C:/Users/rosun/.spyder-py3/qsm_merge.py', wdir='C:/Users/rosun/.spyder-py3')

## ---(Wed Oct  6 12:37:18 2021)---
runfile('C:/Users/rosun/.spyder-py3/qsm_merge.py', wdir='C:/Users/rosun/.spyder-py3')
runfile('C:/Users/rosun/.spyder-py3/onhandV1_2.py', wdir='C:/Users/rosun/.spyder-py3')
runfile('C:/Users/rosun/.spyder-py3/qsm_merge.py', wdir='C:/Users/rosun/.spyder-py3')

## ---(Mon Oct 11 14:05:17 2021)---
runfile('C:/Users/rosun/.spyder-py3/qsm_merge.py', wdir='C:/Users/rosun/.spyder-py3')

## ---(Fri Oct 15 12:34:23 2021)---
import glob
import os
list_of_files=glob.glob('')
os.getcwd()
list_of_files=glob.glob('C:\\Users\\rosun')
list_of_files
latest_file = max(list_of_files, key=os.path.getctime)
latest_file
list_of_files=glob.glob('C:/Users/rosun')
latest_file = max(list_of_files, key=os.path.getctime)
runfile('C:/Users/rosun/.spyder-py3/qsm_merge.py', wdir='C:/Users/rosun/.spyder-py3')
runfile('C:/Users/rosun/.spyder-py3/untitled0.py', wdir='C:/Users/rosun/.spyder-py3')
runfile('C:/Users/rosun/.spyder-py3/latest_file.py', wdir='C:/Users/rosun/.spyder-py3')
import os
os.path.getctime
runfile('C:/Users/rosun/.spyder-py3/qsm_mergeV2.py', wdir='C:/Users/rosun/.spyder-py3')

## ---(Mon Oct 25 10:32:32 2021)---
runfile('C:/Users/rosun/.spyder-py3/qsm_mergeV2.py', wdir='C:/Users/rosun/.spyder-py3')

## ---(Thu Oct 28 07:37:41 2021)---
runfile('C:/Users/rosun/.spyder-py3/qsm_mergeV2.py', wdir='C:/Users/rosun/.spyder-py3')

## ---(Tue Nov  2 12:28:59 2021)---
runfile('C:/Users/rosun/.spyder-py3/qsm_mergeV2.py', wdir='C:/Users/rosun/.spyder-py3')

## ---(Wed Nov  3 08:24:08 2021)---
runfile('C:/Users/rosun/.spyder-py3/qsm_mergeV2.py', wdir='C:/Users/rosun/.spyder-py3')
runfile('C:/Users/rosun/.spyder-py3/qsm_mergeV3.py', wdir='C:/Users/rosun/.spyder-py3')

## ---(Tue Nov  9 06:42:01 2021)---
runfile('C:/Users/rosun/.spyder-py3/qsm_mergeV3.py', wdir='C:/Users/rosun/.spyder-py3')
runfile('C:/Users/rosun/.spyder-py3/incomingV1.py', wdir='C:/Users/rosun/.spyder-py3')
runfile('C:/Users/rosun/.spyder-py3/qsm_mergeV3.py', wdir='C:/Users/rosun/.spyder-py3')
import django

## ---(Fri Nov 12 07:57:49 2021)---
runfile('C:/Users/rosun/.spyder-py3/qsm_mergeV3.py', wdir='C:/Users/rosun/.spyder-py3')

## ---(Tue Nov 30 06:36:11 2021)---
runfile('C:/Users/rosun/.spyder-py3/qsm_mergeV3.py', wdir='C:/Users/rosun/.spyder-py3')

## ---(Wed Dec  1 07:13:32 2021)---
runfile('C:/Users/rosun/.spyder-py3/qsm_mergeV3.py', wdir='C:/Users/rosun/.spyder-py3')

## ---(Wed Dec  1 13:21:26 2021)---
runfile('C:/Users/rosun/.spyder-py3/qsm_mergeV4.py', wdir='C:/Users/rosun/.spyder-py3')
columns_onhand_available = onhand_available.columns
columns_onhand = columns_onhand_available.lower().replace([" ":"_",":":""], inplace=True)
columns_onhand = columns_onhand_available.lower()
columns_onhand_available = columns_onhand_available.lower()
columns_onhand = columns_onhand_available.replace([" ":"_",":":""], inplace=True)
columns_onhand = columns_onhand_available.replace([{" ":"_",":":""}, inplace=True)
columns_onhand = columns_onhand_available.replace({" ":"_",":":""})
columns_onhand_available = columns_onhand_available.lower()
columns_onhand = columns_onhand_available.replace(" ","_")
columns_onhand_available = columns_onhand_available.islower()
columns_onhand_available = columns_onhand_available.replace(" ","_")
columns_onhand_available = [columns_onhand_available.lower() for list in columns_onhand_available]
print(columns_onhand_available)
columns = ['Bottle Packaging', 'Building F', 'Expired Powders',
       'Finished Good/ Bulk Good', 'Missing/Not Found', 'Office, QA',
       'Office, QC', 'PS Stock Bin # 08', 'PS Stock Bin # 11',
       'PS Stock Bin # 14', 'PS Stock Bin # 15',
       'PS Stock Bin In Process', 'Shipping', 'Staging, Pull and weigh', 'Stock Bin # 01',
       'Stock Bin # 02', 'Stock Bin # 03', 'Stock Bin # 04',
       'Stock Bin # 05', 'Stock Bin # 06', 'Stock Bin # 07',
       'Stock Bin # 08', 'Stock Bin # 09', 'Stock Bin # 10',
       'Stock Bin # 14', 'Stock Bin # 15', 'Stock Bin # 17',
       'Stock Bin # 19', 'Stock Bin # 21', 'Stock Bin # 22',
       'Stock Bin # 24', 'Stock Bin # 25', 'Stock Bin # 26',
       'Stock Bin In Process','Expired D51', 'Expired D52',
       'Expired D54', 'Expired D55', 'Expired D58', 'Expired E51',
       'Expired E52', 'Expired E54', 'Expired E55', 'Expired E58']
columns = columns.replace(" ","_")
columns = [x.replace(" ","_") for x in columns]
columns
onhand_columns = onhand.columns
print(onhand_columns)
onhand_columns = [x.replace(" ","_") for x in onhand_columns]
print(onhand_columns)
onhand_columns = onhand.columns
onhand_columns = [x.replace(" ","_") for x in onhand_columns]
print(onhand_columns)
onhand_columns = [x.replace(":","") for x in onhand_columns]
print(onhand_columns)
onhand_columns = [x.lower() for x in onhand_columns]
print(onhand_columns)
onhand.columns
onhand.columns = onhand_columns
onhand.columns
runfile('C:/Users/rosun/.spyder-py3/qsm_mergeV4.py', wdir='C:/Users/rosun/.spyder-py3')
runfile('C:/Users/rosun/.spyder-py3/qsm_mergeV3.py', wdir='C:/Users/rosun/.spyder-py3')
runfile('C:/Users/rosun/.spyder-py3/qsm_mergeV4.py', wdir='C:/Users/rosun/.spyder-py3')
data['tracking']
data['expiration'] = 0
data['lot'] = 0
runfile('C:/Users/rosun/.spyder-py3/qsm_mergeV4_1.py', wdir='C:/Users/rosun/.spyder-py3')
data['tracking'][i]
i
data['tracking'][i].isnan()
float(data['tracking'][i]).isnan()
import math
math.isnan(data['tracking'][i])
data['tracking'][i].find("nan")
runfile('C:/Users/rosun/.spyder-py3/qsm_mergeV4_1.py', wdir='C:/Users/rosun/.spyder-py3')
type(data['tracking'][i])
i
i=1108
type(data['tracking'][i])
pd.isna(data['tracking'][i])
i=1109
pd.isna(data['tracking'][i])
runfile('C:/Users/rosun/.spyder-py3/qsm_mergeV4_1.py', wdir='C:/Users/rosun/.spyder-py3')
data['tracking'][i][9:15]
data['tracking'][i][9:18]
data['tracking'][i][9:19]
runfile('C:/Users/rosun/.spyder-py3/qsm_mergeV4_1.py', wdir='C:/Users/rosun/.spyder-py3')
i=253
data['tracking'][i][9:19]
runfile('C:/Users/rosun/.spyder-py3/qsm_mergeV4_1.py', wdir='C:/Users/rosun/.spyder-py3')
i=1007
data['tracking'][i]
runfile('C:/Users/rosun/.spyder-py3/qsm_mergeV4_1.py', wdir='C:/Users/rosun/.spyder-py3')
data['tracking'][i]
data['tracking'][i].find("ExpDate")
data['tracking'][i].find("Lot")
'Exp' in data['tracking'][i]
'axp' in data['tracking'][i]
runfile('C:/Users/rosun/.spyder-py3/qsm_mergeV4_1.py', wdir='C:/Users/rosun/.spyder-py3')
data['tracking'][i]
data['tracking'][i].len()
len(data['tracking'][i])
runfile('C:/Users/rosun/.spyder-py3/qsm_mergeV4_1.py', wdir='C:/Users/rosun/.spyder-py3')
runfile('C:/Users/rosun/.spyder-py3/qsm_mergeV4_2.py', wdir='C:/Users/rosun/.spyder-py3')

## ---(Wed Dec  8 14:59:01 2021)---
runfile('C:/Users/rosun/.spyder-py3/qsm_mergeV4_2.py', wdir='C:/Users/rosun/.spyder-py3')

## ---(Thu Dec  9 11:56:46 2021)---
runfile('C:/Users/rosun/.spyder-py3/qsm_mergeV4_2.py', wdir='C:/Users/rosun/.spyder-py3')

## ---(Mon Dec 13 10:54:05 2021)---
runfile('C:/Users/rosun/.spyder-py3/qsm_mergeV4_2.py', wdir='C:/Users/rosun/.spyder-py3')
runfile('C:/Users/rosun/.spyder-py3/qsm_pivot_table_V1.py', wdir='C:/Users/rosun/.spyder-py3')
combined[1]
combined['location'1][1]
combined['location'][1]
if combined['location'][1].notnull():
    print("not null")
    
if combined['location'][1-1]:
    print("not null")
    
combined['location'][0]
i=1
combined['location'][i-1]
combined['location'][i-2]
if combined['location'][i-2]:
    print("ok")
else
if combined['location'][i-2]:
    print("ok")
else:
    pass
    
try:
    if combined['location'][i-2]:
        print("ok")
except:
    pass
    
runfile('C:/Users/rosun/.spyder-py3/qsm_pivot_table_V1.py', wdir='C:/Users/rosun/.spyder-py3')
combined['part_number'][1]
runfile('C:/Users/rosun/.spyder-py3/qsm_pivot_table_V1.py', wdir='C:/Users/rosun/.spyder-py3')
runfile('C:/Users/rosun/.spyder-py3/qsm_mergeV4_2.py', wdir='C:/Users/rosun/.spyder-py3')
runfile('C:/Users/rosun/.spyder-py3/mfg_jobs.py', wdir='C:/Users/rosun/.spyder-py3')
x = "gato_"
x[-1]
runfile('C:/Users/rosun/.spyder-py3/mfg_jobs.py', wdir='C:/Users/rosun/.spyder-py3')
x[-1] = ""
x[-1].replace("")
x[-1].replace("*")
x[-1].replace("_","")
x
x[-1].replace("_","")
x = x[-1].replace("_","")
x
x = "gato_"
x
x.rstrip(x[-1])
x
runfile('C:/Users/rosun/.spyder-py3/mfg_jobs.py', wdir='C:/Users/rosun/.spyder-py3')