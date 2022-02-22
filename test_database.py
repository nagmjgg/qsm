import psycopg2

#https://www.tutorialspoint.com/python_data_access/python_mysql_create_table.htm
db_name="qsm"
username='postgres'
user_password='Quality01'
db_host='localhost'
db_port= '5432'

def postgres_test():

    try:
        #conn = psycopg2.connect("dbname='mydb' user='myuser' host='my_ip' password='mypassword' connect_timeout=1 ")
        conn = psycopg2.connect(database=db_name, user=username, password=user_password, host=db_host, port=db_port, connect_timeout=1)
        conn.close()
        return True
    except:
        return False

if postgres_test():
    print("Conexio'n exitosa")
else:
    print("Conexio'n Fallida")