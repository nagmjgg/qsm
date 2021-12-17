# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 06:38:54 2021

@author: mgarcia
"""

import glob
import os

list_of_files = glob.glob('D:/shared_inventory/server files/onhand*.csv') # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)
print(latest_file)