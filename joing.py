# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 07:16:04 2021

@author: rosun
"""


#merge with inventory_availability
data_inventory = inventory_availability.copy()
data_onhand = data_filtered.copy()
merge_inner = pd.merge(left=onhand, right=data_inventory, left_on="Part Number", right_on="Part")

