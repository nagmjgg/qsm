"""
Copy CSV file information to a Mysql Table...
Works with SqlAlchemy
Mysql restricts 'index' field

V1  First Version just extract "combined_inventory_onhand.csv" to table "onhand_ingredients" without asking
    append all the information to the table

"""


from sqlalchemy import create_engine
import pandas as pd
import glob
import os
import mysql.connector
import connection_file as con_file

#establishing the connection
conn = mysql.connector.connect(database=con_file.db_name, user=con_file.username, password=con_file.user_password, host=con_file.db_host, port=con_file.db_port)

if conn:
    print("Mysql connection ok")
else:
    print("Mysql connection nok")

#Creating a cursor object using the cursor() method
cursor = conn.cursor(buffered=True)


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
filename = find_last_file(folder,"Combined_inventory")
print(filename)

df = pd.read_csv(filename,index_col=False, encoding='latin-1')

delete_current_database("onhand_ingredients")
print(f"database deleted !")

# create sqlalchemy engine
engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                      .format(user="sql", pw="Quality01",
                      db="qsm"))

# Insert whole DataFrame into MySQL
df.to_sql('onhand_ingredients', con = engine, if_exists = 'replace', chunksize = 1000, index=False)    #if_exists='append' or 'replace'
print(f"database updated !")