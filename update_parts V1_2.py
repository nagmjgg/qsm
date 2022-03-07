"""
Copy CSV file information to a Mysql Table...
Works with SqlAlchemy
Mysql restricts 'index' field

V1  First Version just extract "combined_inventory_onhand.csv" to table "onhand_ingredients" without asking
    append all the information to the table
    stable version ... succesfully update parts table with index as part_index

"""

from sqlalchemy import create_engine, types, INTEGER, FLOAT, VARCHAR, DATE
import pandas as pd
import glob
import os
import mysql.connector
import connection_file as con_file

#establishing the connection
conn = mysql.connector.connect(database=con_file.db_name, user=con_file.username, password=con_file.user_password, host=con_file.db_host, port=con_file.db_port)

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

def find_last_file(folder,initials):  #folder: 'D:/shared_inventory/server files/', initials: 'available'
    location = folder + initials
    list_of_files = glob.glob(location + '*.csv') # * means all if need specific format then *.csv
    filename = max(list_of_files, key=os.path.getctime)
    print(f"Last File > {filename}")
    return filename

def delete_current_database(table):
    query = "delete from " + table

    cursor.execute(query)

#Set data folder
folder = "D:/shared_inventory/server files/"
filename = find_last_file(folder,"elements_qsm")
print(filename)

df = pd.read_csv(filename ,index_col=False, encoding='latin-1')
csv_count = df['part_number'].count()
print(f"csv_count: {csv_count}")

delete_current_database("parts")
print(f"database deleted !")

#create_future_database(csv_count)
#print(f"database created !")

# create sqlalchemy engine
engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                      .format(user="sql", pw="Quality01",
                      db="qsm"))

# Insert whole DataFrame into MySQL
df.to_sql('parts', con = engine, if_exists = 'append', chunksize = 1000, index=False)    #if_exists='append' or 'replace'
print(f"database updated !")