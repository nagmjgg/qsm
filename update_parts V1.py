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

db_name="qsm"
username='supply'
user_password='SupplyQualityQsm'
db_host='192.168.210.25'
db_port= '3306'

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

def delete_current_database():
    query = "delete from parts"

    cursor.execute(query)

def create_future_database(count_rows):
    rows = count_rows + 1
    for i in range(rows):
        query = "insert into parts (product_name) values (%s)"

        cursor.execute(query, (i))

    conn.commit()

#Set data folder
folder = "D:/shared_inventory/server files/"
filename = find_last_file(folder,"elements_qsm")
print(filename)


df = pd.read_csv(filename ,index_col=False, encoding='latin-1')
csv_count = df['part_number'].count()
print(f"csv_count: {csv_count}")



# create sqlalchemy engine
engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                      .format(user="sql", pw="Quality01",
                      db="qsm"))
# Insert whole DataFrame into MySQL
df.to_sql('parts', con = engine, if_exists = 'append', chunksize = 1000, index=False)    #if_exists='append' or 'replace'