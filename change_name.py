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

import os, subprocess
import time
import random
import schedule
from shutil import copyfile
from sys import exit
from datetime import datetime

#date_initial_file = date.today().strftime("%Y%m%d") #fecha actual ... colocar formato... date.strftime("%d/%m/%y")
#date_final_file = date.today() #fecha actual ... colocar formato... date.strftime("%d/%m/%y")
#print(f" Actual date {date}")     #2021-08-10

folder = "D:/shared_inventory/server files/"

new_datetime = datetime.now().strftime("%Y%m%d_%I")

#initial_filename = folder+'OnHand '+str(date_initial_file)+'.csv'

source = folder + "onhand_report.csv"
target = folder + "onhand_report_" + new_datetime + ".csv"

print(f"source : {source}")
print(f"target : {target}")

# adding exception handling

try:
    copyfile(source, target)
except IOError as e:
    print("Unable to copy file. %s" % e)
    exit(1)
except:
    print("Unexpected error:", sys.exc_info())
    exit(1)

print("\nFile copy done!\n")