import pandas as pd
import os

directory = "C:/Users/rosun/Desktop"
os.chdir(directory)
file = "OnHand 20210728.csv"

onhand = pd.DataFrame()
onhand = pd.read_csv(file,header=3)

onhandx = onhand.copy()

print(onhand.head())
onhand.['Part Number']



