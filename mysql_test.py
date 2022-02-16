import mysql.connector

cnx = mysql.connector.connect(user='root', password='Quality01',host="127.0.0.1",database='qsm', port=3306)
if cnx:
    print("Conexion Exitosa")
else:
    print("Conexion Fallida")


cnx.close()