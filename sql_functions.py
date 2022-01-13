"""
At the end create Security for SQL Injection
https://realpython.com/prevent-python-sql-injection/

Postgresql Commands examples

#Preparing query to create a database
sql = '''CREATE database mydb''';

#Creating table as per requirement
sql_command = '''CREATE TABLE EMPLOYEE(
      FIRST_NAME CHAR(20) NOT NULL,
      LAST_NAME CHAR(20),
      AGE INT,
      SEX CHAR(1),
      INCOME FLOAT
   )'''

# Preparing SQL queries to INSERT a record into the database.
cursor.execute('''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX,
   INCOME) VALUES ('Ramya', 'Rama priya', 27, 'F', 9000)''')

#Retrieving data
cursor.execute('''SELECT * from EMPLOYEE''')

#Retrieving specific records using the where clause
cursor.execute("SELECT * from EMPLOYEE WHERE AGE <23")

#Retrieving specific records using the ORDER BY clause
cursor.execute("SELECT * from EMPLOYEE ORDER BY AGE")

#Updating the records
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = 'M'"
cursor.execute(sql)

#Deleting records
cursor.execute('''DELETE FROM EMPLOYEE WHERE AGE > 25''')

#Doping EMPLOYEE table if already exists
cursor.execute("DROP TABLE emp")

#Retrieving single row
sql = '''SELECT * from EMPLOYEE LIMIT 2 OFFSET 2'''

#Retrieving single row
sql = '''SELECT * from EMP INNER JOIN CONTACT ON EMP.CONTACT = CONTACT.ID'''

SELECT Cricketers.First_Name, Cricketers.Last_Name, Cricketers.Country,
OdiStats.matches, OdiStats.runs, OdiStats.centuries, OdiStats.halfcenturies
from Cricketers INNER JOIN OdiStats ON Cricketers.First_Name = OdiStats.First_Name;


Cursor class/object

Following are the various methods provided by the Cursor class/object.

Sr.No	Method & Description
1	callproc() This method is used to call existing procedures PostgreSQL database.

2	close() This method is used to close the current cursor object.

3	executemany() This method accepts a list series of parameters list. Prepares an MySQL query and executes it with all the parameters.

4	execute() This method accepts a MySQL query as a parameter and executes the given query.

5	fetchall() This method retrieves all the rows in the result set of a query and returns them as list of tuples. (If we execute this after retrieving few rows it returns the remaining ones)

6	fetchone() This method fetches the next row in the result of a query and returns it as a tuple.

7	fetchmany() This method is similar to the fetchone() but, it retrieves the next set of rows in the result set of a query, instead of a single row.

#Show table columns
SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'some_table';

#Example of command:
select_command("select column_name from information_schema.columns where table_name = 'onhand_ingredients'")

"""
import os

import pandas as pd
import tkinter as tk
from pandastable import Table
import psycopg2
import glob    #func last_filename
from tabulate import tabulate



pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.colheader_justify', 'center')
pd.set_option('display.precision', 3)

#https://www.tutorialspoint.com/python_data_access/python_mysql_create_table.htm
db_name="qsm"
username='postgres'
user_password='Quality01'
db_host='127.0.0.1'
db_port= '5432'

#establishing the connection
conn = psycopg2.connect(database=db_name, user=username, password=user_password, host=db_host, port= db_port)

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

def connect_db(database = db_name, user = username, password = user_password, host = db_host, port = db_port):
   global conn
   global cursor
   #establishing the connection
   conn = psycopg2.connect(
      database=database, user=user, password=password, host=host, port= port
   )

   #Executing an MYSQL function using the execute() method
   cursor.execute("select version()")

   # Fetch a single row using fetchone() method.
   data = cursor.fetchone()
   print("Connection established to: ",data)

def find_last_file(folder, initials):  # folder: 'D:/shared_inventory/server files/', initials: 'available'
   location = folder + initials
   list_of_files = glob.glob(location + '*.csv')  # * means all if need specific format then *.csv
   filename = max(list_of_files, key=os.path.getctime)
   print(f"Last File > {filename}")
   return filename

def create_table(sql_command):
   global conn
   global cursor
   # Doping EMPLOYEE table if already exists.
   #cursor.execute("DROP TABLE IF EXISTS " + table + "")

   # Creating table as per requirement

   cursor.execute(sql_command)
   print("Table created successfully........")

   # Commit your changes in the database
   conn.commit()

""" select the last file, starting with 'Combined_' ... filename_combined = find_last_file('D:/shared_inventory/server files/', 'Combined_') ....
# create_table_from_csv('onhand_ingredients',filename_combined)
#https://stackoverflow.com/questions/2987433/how-to-import-csv-file-data-into-a-postgresql-table """
def create_table_from_csv(table_name, csv_filename):

   df = pd.read_csv(csv_filename)
   df.columns = [c.lower() for c in df.columns]  # postgres doesn't like capitals or spaces

   from sqlalchemy import create_engine
   engine = create_engine('postgresql://' + username + ':' + user_password + '@localhost:5432/' + db_name + '')
   print(engine)
   df.to_sql(table_name, engine)
   print(f"exporting file > {csv_filename}")

def create_table_from_csv_replace(table_name, csv_filename):

   df = pd.read_csv(csv_filename)
   df.columns = [c.lower() for c in df.columns]  # postgres doesn't like capitals or spaces

   from sqlalchemy import create_engine
   engine = create_engine('postgresql://' + username + ':' + user_password + '@localhost:5432/' + db_name + '')
   print(engine)
   df.to_sql(table_name, engine, if_exists='replace')
   print(f"exporting file > {csv_filename}")

def insertData_command(command_text):
   cursor.execute(command_text)

   # Commit your changes in the database
   conn.commit()
   print("Records inserted........")

   conn.close()

def select_command(command_text):   # text format : '''SELECT * from EMPLOYEE'''
   # Retrieving data
   cursor.execute(command_text)

   # Fetching 1st row from the table
   result = cursor.fetchone();
   #print(result)

   #Fetching 1st row from the table
   #result = cursor.fetchall();
   #print(result)
   return result

   # Commit your changes in the database
   conn.commit()

def postgresql_to_dataframe(conn, select_query, column_names):
   """
   #df = postgresql_to_dataframe(conn, "select * from MonthlyTemp", column_names)
   #column_names = ["id", "source", "datetime", "mean_temp"]

   https://naysan.ca/2020/05/31/postgresql-to-pandas/
   Tranform a SELECT query into a pandas dataframe
   """
   cursor = conn.cursor()
   try:
      cursor.execute(select_query)
   except (Exception, psycopg2.DatabaseError) as error:
      print("Error: %s" % error)
      cursor.close()
      return 1

   # Naturally we get a list of tupples
   tupples = cursor.fetchall()
   cursor.close()

   # We just need to turn it into a pandas dataframe
   df = pd.DataFrame(tupples, columns=column_names)
   return df

#return Column names
def table_column_names(table_name):
   command = "SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '" + table_name + "'"
   columns = select_command(command)
   return columns

def update_table_combined_inventory():
   filename_combined = find_last_file('D:/shared_inventory/server files/', 'Combined_')
   print(f"importing file > {filename_combined}")
   create_table_from_csv_replace('onhand_ingredients',filename_combined)

def update_table_combined_inventory_history():
   filename_combined = find_last_file('D:/shared_inventory/server files/', 'Combined_')
   print(f"importing file > {filename_combined}")
   create_table_from_csv('onhand_ingredients_history',filename_combined)

def show_info(command_text, columns):
   #command_text example: "select part_number, location, expiration, qty from onhand_ingredients"
   #columns could be like this: ['part_number','location','expiration','qty']
   window = tk.Tk()
   frame = tk.Frame(window)
   frame.pack(fill='both', expand=True)

   command_text = "select part_number, location, expiration, qty from onhand_ingredients"
   df = postgresql_to_dataframe(conn, command_text, columns)

   pt = Table(frame, dataframe=df)
   pt.show()

