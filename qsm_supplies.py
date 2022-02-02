"""
Programm to input supplies devlivered to the different departments



"""

import tkinter as tk
from tkinter import *
from tkinter import ttk

# Fonts
font_columns_name = ('Arial',10,'bold') # normal or bold
font_wrap_title = ('Arial',12,'bold') # normal or bold

#fixed values
PADX = 1
PADY = 1

root = Tk()

root.title("Supplies")
root.geometry("1080x720")

wrapper0 = LabelFrame(root, text="Search", font=font_wrap_title)
wrapper1 = LabelFrame(root, text="List", font=font_wrap_title)
wrapper2 = LabelFrame(root, text="Input", font=font_wrap_title)

wrapper0.pack(fill="both", expand="yes", padx=PADX, pady=PADY)
wrapper1.pack(fill="both", expand="yes", padx=PADX, pady=PADY)
wrapper2.pack(fill="both", expand="yes", padx=PADX, pady=PADY)

trv = ttk.Treeview(wrapper0, columns=(1,2,3), show="headings", height="3")











root.mainloop()