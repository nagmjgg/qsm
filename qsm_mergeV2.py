import pandas as pd
from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilename
import time
from datetime import date
import glob
import os

#texto en colores

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))

def find_last_file(folder,initials):  #folder: 'D:/shared_inventory/server files/', initials: 'available'
    location = folder + initials
    list_of_files = glob.glob(location + '*.csv') # * means all if need specific format then *.csv
    filename = max(list_of_files, key=os.path.getctime)
    print(f"Last File > {filename}")
    return filename


#main_window = Tk()

#Display parameters
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


date_initial_file = date.today().strftime("%Y-%m-%d") #fecha actual ... colocar formato... date.strftime("%d/%m/%y")
date_final_file = date.today() #fecha actual ... colocar formato... date.strftime("%d/%m/%y")
print(f" Actual date {date}")     #2021-08-10

#Set data folder
folder = "D:/shared_inventory/server files/"

#**********************************************
#   ************ OnHand File ***********
#**********************************************
print("***** Onhand  ******")

onhand = pd.DataFrame()

'''
#opening file 
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
print("Open file in progress")
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)
'''


#opening file automatically

initial_filename_onhand = find_last_file('D:/shared_inventory/server files/','onhand_report')
print(f"opening file > {initial_filename_onhand}")


try:
    onhand = pd.read_csv(initial_filename_onhand, encoding='latin1',header=3)
except: 
    print(f"opening file > {initial_file_name_onhand}... doesn't exist")


#onhand.columns

'''
onhand.columns
Index(['Part Number', 
       'Description', 
       'Qty', 
       'Unnamed: 3', 
       'Location', 
       'Tracking', 
       'Unnamed: 6', 
       'Unnamed: 7'], dtype='object')
'''

#delete first row
onhand = onhand.drop(labels=0, axis=0)

onhand = onhand.drop(labels=['Unnamed: 6', 'Unnamed: 7'], axis=1)

#delete last row
onhand = onhand.iloc[:-2]

#Sort data for "Part Number"
onhand_sorted=onhand.sort_values(by='Part Number')
print("Data sorted ok")

#Unique values for location
#onhand['Location'].unique()
'''
'Bottle Packaging', 'Building F', 'Expired D51', 'Expired D52',
       'Expired D54', 'Expired D55', 'Expired D58', 'Expired E51',
       'Expired E52', 'Expired E54', 'Expired E55', 'Expired E58',
       'Finished Good/ Bulk Good', 'Missing/Not Found', 'Office, QA',
       'Office, QC', 'PS Stock Bin # 08', 'PS Stock Bin # 15',
       'PS Stock Bin In Process', 'Quarantine Labels',
       'Quarantine Packaging Materials', 'Quarantine Powders/ Receiving',
       'Shipping', 'Staging, Pull and weigh', 'Stock Bin # 01',
       'Stock Bin # 02', 'Stock Bin # 03', 'Stock Bin # 04',
       'Stock Bin # 05', 'Stock Bin # 06', 'Stock Bin # 07',
       'Stock Bin # 08', 'Stock Bin # 09', 'Stock Bin # 10',
       'Stock Bin # 14', 'Stock Bin # 15', 'Stock Bin # 17',
       'Stock Bin # 21', 'Stock Bin # 22', 'Stock Bin # 24',
       'Stock Bin # 25', 'Stock Bin # 26', 'Stock Bin # A0',
       'Stock Bin # A10', 'Stock Bin # A11', 'Stock Bin # A12',
       'Stock Bin # A13', 'Stock Bin # A14', 'Stock Bin # A15',
       'Stock Bin # A16', 'Stock Bin # A17', 'Stock Bin # A18',
       'Stock Bin # A19', 'Stock Bin # A2', 'Stock Bin # A20',
       'Stock Bin # A21', 'Stock Bin # A22', 'Stock Bin # A23',
       'Stock Bin # A24', 'Stock Bin # A25', 'Stock Bin # A27',
       'Stock Bin # A28', 'Stock Bin # A3', 'Stock Bin # A31',
       'Stock Bin # A32', 'Stock Bin # A34', 'Stock Bin # A35',
       'Stock Bin # A36', 'Stock Bin # A37', 'Stock Bin # A38',
       'Stock Bin # A39', 'Stock Bin # A4', 'Stock Bin # A40',
       'Stock Bin # A5', 'Stock Bin # A6', 'Stock Bin # A7',
       'Stock Bin # A8', 'Stock Bin # A9', 'Stock Bin # B10',
       'Stock Bin # B11', 'Stock Bin # B12', 'Stock Bin # B13',
       'Stock Bin # B14', 'Stock Bin # B15', 'Stock Bin # B16',
       'Stock Bin # B17', 'Stock Bin # B18', 'Stock Bin # B19',
       'Stock Bin # B2', 'Stock Bin # B21', 'Stock Bin # B22',
       'Stock Bin # B23', 'Stock Bin # B24', 'Stock Bin # B25',
       'Stock Bin # B26', 'Stock Bin # B28', 'Stock Bin # B3',
       'Stock Bin # B30', 'Stock Bin # B34', 'Stock Bin # B35',
       'Stock Bin # B36', 'Stock Bin # B38', 'Stock Bin # B39',
       'Stock Bin # B4', 'Stock Bin # B40', 'Stock Bin # B45',
       'Stock Bin # B5', 'Stock Bin # B6', 'Stock Bin # B7',
       'Stock Bin # B8', 'Stock Bin # B9', 'Stock Bin # C1',
       'Stock Bin # C10', 'Stock Bin # C11', 'Stock Bin # C12',
       'Stock Bin # C13', 'Stock Bin # C14', 'Stock Bin # C15',
       'Stock Bin # C16', 'Stock Bin # C17', 'Stock Bin # C18',
       'Stock Bin # C19', 'Stock Bin # C2', 'Stock Bin # C21',
       'Stock Bin # C22', 'Stock Bin # C23', 'Stock Bin # C24',
       'Stock Bin # C25', 'Stock Bin # C26', 'Stock Bin # C27',
       'Stock Bin # C28', 'Stock Bin # C29', 'Stock Bin # C3',
       'Stock Bin # C30', 'Stock Bin # C31', 'Stock Bin # C32',
       'Stock Bin # C33', 'Stock Bin # C35', 'Stock Bin # C36',
       'Stock Bin # C37', 'Stock Bin # C38', 'Stock Bin # C39',
       'Stock Bin # C4', 'Stock Bin # C40', 'Stock Bin # C41',
       'Stock Bin # C42', 'Stock Bin # C44', 'Stock Bin # C45',
       'Stock Bin # C5', 'Stock Bin # C6', 'Stock Bin # C7',
       'Stock Bin # C8', 'Stock Bin # C9', 'Stock Bin # D1',
       'Stock Bin # D10', 'Stock Bin # D11', 'Stock Bin # D12',
       'Stock Bin # D13', 'Stock Bin # D14', 'Stock Bin # D15',
       'Stock Bin # D16', 'Stock Bin # D17', 'Stock Bin # D18',
       'Stock Bin # D19', 'Stock Bin # D2', 'Stock Bin # D20',
       'Stock Bin # D21', 'Stock Bin # D22', 'Stock Bin # D23',
       'Stock Bin # D24', 'Stock Bin # D25', 'Stock Bin # D26',
       'Stock Bin # D27', 'Stock Bin # D28', 'Stock Bin # D3',
       'Stock Bin # D31', 'Stock Bin # D34', 'Stock Bin # D4',
       'Stock Bin # D43', 'Stock Bin # D46', 'Stock Bin # D5',
       'Stock Bin # D52', 'Stock Bin # D6', 'Stock Bin # D7',
       'Stock Bin # D8', 'Stock Bin # D9', 'Stock Bin # E1',
       'Stock Bin # E10', 'Stock Bin # E11', 'Stock Bin # E12',
       'Stock Bin # E13', 'Stock Bin # E14', 'Stock Bin # E15',
       'Stock Bin # E16', 'Stock Bin # E17', 'Stock Bin # E18',
       'Stock Bin # E19', 'Stock Bin # E2', 'Stock Bin # E20',
       'Stock Bin # E21', 'Stock Bin # E22', 'Stock Bin # E23',
       'Stock Bin # E24', 'Stock Bin # E25', 'Stock Bin # E26',
       'Stock Bin # E27', 'Stock Bin # E3', 'Stock Bin # E30',
       'Stock Bin # E31', 'Stock Bin # E33', 'Stock Bin # E34',
       'Stock Bin # E4', 'Stock Bin # E43', 'Stock Bin # E44',
       'Stock Bin # E45', 'Stock Bin # E46', 'Stock Bin # E5',
       'Stock Bin # E6', 'Stock Bin # E7', 'Stock Bin # E8',
       'Stock Bin # E9', 'Stock Bin In Process', 'Warehouse 2',
       'Warehouse Floor'], dtype=object)'''



location_unavailable = ['Bottle Packaging', 'Building F', 'Expired Powders',
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

#delete row 0
#onhan_sorted = onhand_sorted.drop(labels=0, axis=0)
#onhand = onhand.drop(labels=0, axis=1)


data = onhand_sorted.copy()
print("Data copied ok")

#data in location 'Stock Bin In Process'
data_location = data[data["Location"]!='Stock Bin In Process']
data_location.sort_values(by="Part Number")

#****** create column available *******

data["available"] = 0

#Totals
qty = data.shape[0]


#columns
data.columns

data.drop

for i in data.index:
    #print(i)
    #print(data["Location"][i])
    if data["Location"][i] in location_unavailable:
        data["available"][i]=0
    else:
        data["available"][i]=1
print("Active location flag  ok")


onhand_available = data[data["available"]==1]
print("Data filtered ok")

onhand_available = onhand_available.sort_values(by='Part Number')
#onhand.describe()
#main_window.mainloop()


#***************************************
#onhand available data (location + qty)
#***************************************

onhand_available["data_available"] = 0
onhand_available["data_available_flag"] = 0

#exportar archivo 
try:
    file_name = folder+'onhand_out_'+str(date_final_file)+'.csv'
    onhand_available.to_csv(file_name)
    
except:
    print("Error... File Permision denied")
    
print(f"File exported ok... {file_name}")


#**********************************************
#   ************ Inventory Availabilty ********
#**********************************************

inventory_availability = pd.DataFrame()
print('***** Inventory availability ******') 
prGreen('***** Inventory availability ******')
'''
#ask for the initial file
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
print("** inventory_availability File ** >> Open file in progress")
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)
'''

initial_filename_available = find_last_file('D:/shared_inventory/server files/','available')
print(f"opening file > {initial_filename_available}")


try:
    inventory_availability = pd.read_csv(initial_filename_available, encoding='latin1',header=3)
except: 
    print(f"opening file > {initial_filename_available}... doesn't exist")


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


#**********************************************
#   ***** Onhand & availability Joined ********
#**********************************************
print('***** Onhand & availability Joined ******') 
prRed('***** Onhand & availability Joined ******')


#main_window = Tk()

#Display parameters
#merge with inventory_availability
data_inventory = inventory_availability.copy()
data_onhand = onhand_available.copy()

merge_inner = pd.merge(left=data_onhand, right=data_inventory, left_on="Part Number", right_on="Part")

#exportar archivo 
try:
    file_name = folder+'Combined_Inventory_Onhand_'+str(date_final_file)+'.csv'
    merge_inner.to_csv(file_name)
    
except:
    print("Error... File Permision denied")
    
print(f"File exported ok... {file_name}")
