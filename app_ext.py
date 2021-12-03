from tkinter import *
import os, subprocess

FONT = "Consolas 10"
color_flag = 0
text=""


#find text inside string
def find_text(text, text_to_find):
    result = text.find(text_to_find)
    return result

def extract_text(text, start, finish):
    result = text[start:finish]
    return result

#vent = Tk()
#vent.geometry("370x60+100+100")

text = "Hola como estas"
find = "como"
start = find_text(text,"como")
extracted = extract_text(text,start,start+3)
print(f'find word {find} in string {text}' )
print(f'extract {extracted}')

#vent.mainloop()