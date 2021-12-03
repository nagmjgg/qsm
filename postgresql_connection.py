import psycopg2
#https://www.tutorialspoint.com/python_data_access/python_mysql_create_table.htm
db_name="qsm"
username='postgres'
user_password='Quality01'
db_host='127.0.0.1'
db_port= '5432'



def connect_db(database = db_name, user = username, password = user_password, host = db_host, port = db_port):
   #establishing the connection
   conn = psycopg2.connect(
      database=database, user=user, password=password, host=host, port= port
   )
   #Creating a cursor object using the cursor() method
   cursor = conn.cursor()

   #Executing an MYSQL function using the execute() method
   cursor.execute("select version()")

   # Fetch a single row using fetchone() method.
   data = cursor.fetchone()
   print("Connection established to: ",data)

connect_db()

def create_table(sql_command):
   # Doping EMPLOYEE table if already exists.
   #cursor.execute("DROP TABLE IF EXISTS " + table + "")

   # Creating table as per requirement

   cursor.execute(sql_command)
   print("Table created successfully........")

   # Commit your changes in the database
   conn.commit()



connect_db()

sql_command = '''CREATE TABLE EMPLOYEE(
      FIRST_NAME CHAR(20) NOT NULL,
      LAST_NAME CHAR(20),
      AGE INT,
      SEX CHAR(1),
      INCOME FLOAT
   )'''

create_table(sql_command)

#Closing the connection
conn.close()

