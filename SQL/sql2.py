import pymysql.cursors

# Connect to the database
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='learning',
    cursorclass=pymysql.cursors.DictCursor
)

with connection:
    with connection.cursor() as cursor:
        # Rename table
        sql = "RENAME TABLE staff_table TO faculties;"
        cursor.execute(sql)
        print("Table renamed successfully")

        connection.commit()


import pymysql.cursors


connection=pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='learning',
    cursorclass=pymysql.cursors.DictCursor
)

with connection:
    with connection.cursor() as cursor:
        sql = "DELETE FROM `employeee` WHERE `id` = %s"
        cursor.execute(sql, ('14',))
        connection.commit()
       

import pymysql.cursors


connection=pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='learning',
    cursorclass=pymysql.cursors.DictCursor
)


with connection:
    with connection.cursor() as cursor:
        sql = "UPDATE `employeee` SET `deleted` = FALSE WHERE `id` = %s"
        cursor.execute(sql, (14,))
        connection.commit()
        print("Record restored for employeee with id = 14.")

    
#select

import pymysql.cursors
connection=pymysql.connect(
    host= 'localhost',
    user= 'root',
    password= '',  
    database= 'learning',
    cursorclass= pymysql.cursors.DictCursor
)


with connection:
    with connection.cursor() as cursor:
        sql = "SELECT * FROM `employeee` WHERE `name`=%s"
        cursor.execute(sql, ('usha',))
        connection.commit()

    
import pymysql.cursors
connection=pymysql.connect(
    host= 'localhost',
    user= 'root',
    password= '',  
    database= 'learning',
    cursorclass= pymysql.cursors.DictCursor
)
with connection:
    with connection.cursor() as cursor:
        
        sql = "INSERT INTO `employeee` (`id`, `name`, `age`,`deleted`) VALUES (%s, %s, %s, %s,)"
        cursor.execute(sql, (14, 'cherry', 25,'False'))
        
        sql = "UPDATE `employeee` SET `name` = %s WHERE `id` = %s"
        cursor.execute(sql, ('cherry', 14))
       
        connection.commit()
        
        
       