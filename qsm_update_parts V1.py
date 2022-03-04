"""
Copy CSV file information to a Mysql Table...
Works with SqlAlchemy
Mysql restricts 'index' field

V1  First Version just extract "combined_inventory_onhand.csv" to table "onhand_ingredients" without asking
    append all the information to the table
    stable version ... succesfully update parts table with index as part_index

"""


from sqlalchemy import create_engine
import pandas as pd
import glob
import os


def find_last_file(folder,initials):  #folder: 'D:/shared_inventory/server files/', initials: 'available'
    location = folder + initials
    list_of_files = glob.glob(location + '*.csv') # * means all if need specific format then *.csv
    filename = max(list_of_files, key=os.path.getctime)
    print(f"Last File > {filename}")
    return filename


#Set data folder
folder = "D:/shared_inventory/server files/"
filename = find_last_file(folder,"elements_qsm")
print(filename)


df = pd.read_csv(filename ,index_col=False, encoding='latin-1')
df.head()

db_name="qsm"
username='sql'
user_password='Quality01'
db_host='localhost'
db_port= '3306'

# create sqlalchemy engine
engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                      .format(user="sql", pw="Quality01",
                      db="qsm"))
# Insert whole DataFrame into MySQL
df.to_sql('parts', con = engine, if_exists = 'replace', chunksize = 1000, index=False)    #if_exists='append' or 'replace'

