import mysql.connector

cnx = mysql.connector.connect(user='sql_user', password='Quality01qsm',
                          host='127.0.0.1',
                          database='qsm')
if cnx:
    print("Conexion Exitosa")
else:
    print("Conexion Fallida")


cnx.close()