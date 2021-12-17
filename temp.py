import pandas as pd
from tkinter import *
import tkinter as tk

main_window = Tk()

DIRECTORY = "C:/Users/rosun/Desktop"

onhand = pd.DataFrame()

onhand = pd.read_csv(DIRECTORY + '/' + 'OnHand 20210729.csv', header=3)

print(onhand.['Part Number'])

main_window.mainloop()
