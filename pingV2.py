#!/usr/bin/env python
# -*- coding: latin-1 -*-

# Solucion de caracteres especiales tildes y ñ con coding: latin-1

# Aplicación para agilizar proceso de asignación de Direcciones IP en el equipo
# Nota: se necesita tener el nombre de la conexión de area local sin tildes

'''
determinar tiempo por secuencia
$ python3 -m timeit -n 3 "import time; time.sleep(3)"
3 loops, best of 5: 3 sec per loop
'''

from tkinter import *
import os, subprocess
import tkinter
import tkinter.font as tk_font
import time
import random

#https://realpython.com/python-sleep/
import threading


#ping
import platform    # For getting the operating system name


FONT = "Consolas 10"
color_flag = 0
ip_ping = "192.168.210.5"

retval = os.getcwd()
print(retval)

def find_text_variable(variable,text):
    #print(text)
    value = variable.find(text)
    #print("value:", value)
    return value


def extract_text(file,start_char,number_of_chars):
    file = open(file, "r+")
    text=file.read()
    #print(text)
    text_extracted=text[start_char:start_char + number_of_chars]
    #print("value:", value)
    return text_extracted

def VentanaTemp(archivo):
    temp = Toplevel()
    temp.geometry("600x200")
    texto = Text(temp, width=90, height=12, wrap='none', font=FONT)
    texto.grid(row=6, column=1, columnspan=2, sticky=W)
    texto.insert(0.0, archivo)
    botonTemp = Button(temp, text="Cerrar", command=temp.destroy, takefocus=0)
    botonTemp.grid(row=15, column=1)
    botonTemp.focus_set()

def ping_online(host="8.8.8.8"):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    result = subprocess.run(command,check=True, stdout=subprocess.PIPE, universal_newlines=True)
    #print(result.stdout)
    try:
        return result.stdout
    except ValueError:
        print("pass value error [ping_online]")
        pass

def ping_box(x, color_timebox):
    #https://stackoverflow.com/questions/2953462/pinging-servers-in-python

    button_ok = Label(vent, text="ok", fg="white", bg='green', width=2, height=1)
    button_nok = Label(vent, text="nok", fg="white", bg='red', width=2, height=1)

    colors=("light blue","light green")

    result = ping_online(ip_ping)
    #print(result[1:8])
    text="time="

    print(result)
    print(result.find(text))

    #if result.find(text) == True:
    find_text = result.find(text)
    count_text = len(text)
    start_char = find_text + count_text
    find_final = result.find("ms ")
    #print("start char", start_char)
    #print("find final", find_final)
    time = result[ start_char : find_final]
    text = Label(vent, text= time, width=2, height=1, bg=colors[color_timebox])
    #print("time",time)

    #print(result)
    #print(find_text , " " , count_text , " " , start_char , " " , time)
    #print(type(time))

    x_value = 5

    try:
        if int(time) > 0:
            button_ok.place(x=x, y=10)
            text.place(x=x,y=30)
        else:
            button_nok.place(x=x, y=5)
    except:
        pass

def ping_extendido(qty=10):
    #default initial x:140
    x_value=5
    x_increment = 20
    color_flag = 1
    i=0
    while i < qty:
        ping_box(x_value, color_flag)
        event = threading.Event()
        event.wait(1)
        x_value=x_value+x_increment
        vent.update()

        flag = int(ping_flag.get())
        print(flag)
        print(i)
        print(qty)

        tmp_qty = qty-1
        if flag == 1 and i == tmp_qty:
            print("igual")
            i=0
            x_value = 5

            if color_flag == 1:
                color_flag = 0
            elif color_flag == 0:
                color_flag = 1
            vent.after(5000)
        else:
            i += 1

        print(i)

        ontop_flag = int(allways_ontop_flag.get())
        if ontop_flag == 1:
            vent.lift()


def google():
    outf = open("out.txt", "w+")
    errf = open("error.txt", "w+")
    subprocess.call('ping 8.8.8.8 -n 1', shell=True, stdout=outf, stderr=errf)
    outf.close()
    errf.close()
    fd = open("out.txt", "r")
    output = fd.read()
    fd.close()

    fd = open("error.txt", "r")
    err = fd.read()
    fd.close()

    VentanaTemp(output)



def centrar(ventana):
    ventana.update_idletasks()
    w = ventana.winfo_width()
    h = ventana.winfo_height()
    extraW = ventana.winfo_screenwidth() - w
    extraH = ventana.winfo_screenheight() - h
    ventana.geometry("%dx%d%+d%+d" % (w, h, extraW / 2, extraH / 2))


def JustAbajo(ventana):
    ventana.update_idletasks()
    w = ventana.winfo_width()
    h = ventana.winfo_height()
    extraW = ventana.winfo_screenwidth() - w
    extraH = ventana.winfo_screenheight() - h
    ventana.geometry("%dx%d%+d%+d" % (w, h, extraW - 50, extraH - 100))

vent = Tk()
vent.geometry("370x60+100+100")
#vent.title("SOLES IP")
#vent.overrideredirect(1) #sin ventana de titulo invisible pero no se puede cerrar
# centrar(vent)


JustAbajo(vent)


ping_btn = Button(vent, text="Ping", command=ping_extendido)
ping_btn.place(x=250,y=5)

ping_flag=IntVar()
check_ping = Checkbutton(vent, text="Loop", variable=ping_flag)
check_ping.place(x=300, y=5)

allways_ontop_flag=IntVar()
allways_ontop = Checkbutton(vent, text="OnTop", variable=allways_ontop_flag)
allways_ontop.place(x=300, y=30)

ping_extendido()

vent.mainloop()
