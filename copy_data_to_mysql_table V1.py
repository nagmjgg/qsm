"""
Copy CSV file information to a Mysql Table...
Works with SqlAlchemy
Mysql restricts 'index' field

V1  First Version just extract "combined_inventory_onhand.csv" to table "onhand_ingredients" without asking
    append all the information to the table

"""


from sqlalchemy import create_engine
import pandas as pd


#Set data folder
folder = "D:/shared_inventory/server files/"

df = pd.read_csv(folder + 'Combined_Inventory_Onhand.csv',index_col=False, encoding='latin-1')
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
df.to_sql('onhand_ingredients', con = engine, if_exists = 'append', chunksize = 1000,index=False)
