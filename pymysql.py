

import pymysql

try:
    # Establish connection to the MySQL database
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='sql learning'
    )

    # Create a cursor object
    cursor = connection.cursor()

    # Execute a query
    cursor.execute("SELECT VERSION()")

    # Fetch one result
    version = cursor.fetchone()

    print("pymysql database version:", version)

    # Close the connection
    connection.close()
except pymysql.MySQLError as e:
    print(f"Error connecting to pymysql: {e}")

