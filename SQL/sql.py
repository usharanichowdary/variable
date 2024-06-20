import mysql.connector
from mysql.connector import errorcode

try:
   
    connection = mysql.connector.connect(
        host='localhost',      
        user='root',   
        password='',
        database='learning'
    )

    cursor = connection.cursor()

    # Create a new database
    cursor.execute("select version();")
    version=cursor.fetchone()
    print(version)
    

except mysql.connector.Error as err:
    print(f"Error:{err}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("connection closed")