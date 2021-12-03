"""

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


"""


import psycopg2
#https://www.tutorialspoint.com/python_data_access/python_mysql_create_table.htm
db_name="qsm"
username='postgres'
user_password='Quality01'
db_host='127.0.0.1'
db_port= '5432'

#establishing the connection
conn = psycopg2.connect(
   database=db_name, user=username, password=user_password, host=db_host, port= db_port
)

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

#connect_db()

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
   print(result)

   #Fetching 1st row from the table
   result = cursor.fetchall();
   print(result)

   # Commit your changes in the database
   conn.commit()

#connect_db()

#************** MAIN APP ******************

sql_command = '''CREATE TABLE EMPLOYEE(
      FIRST_NAME CHAR(20) NOT NULL,
      LAST_NAME CHAR(20),
      AGE INT,
      SEX CHAR(1),
      INCOME FLOAT
   )'''



#create_table(sql_command)
#select_command("select FIRST_NAME, INCOME from employee")

#command = '''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX,
#      INCOME) VALUES ('Ramya', 'Rama priya', 27, 'F', 9000)'''
#insertData_command(command)

#Closing the connection
conn.close()
print(f"Connection closed !")
