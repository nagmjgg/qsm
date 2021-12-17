import pandas as pd
from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilename

#main_window = Tk()

import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

DIRECTORY = "C:/Users/rosun/Desktop"

onhand = pd.DataFrame()

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)

onhand = pd.read_csv(filename, header=3)



onhand.columns

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
onhand_sorted=onhand.sort_values(by='Part Number')

#delete row 0
onhand = onhand.drop(labels=0, axis=0)

data = onhand.head(20)

onhand.sample(5)

onhand.describe()
#main_window.mainloop()
