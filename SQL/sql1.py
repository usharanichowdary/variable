#Delete

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
        sql = "DELETE FROM `staff` WHERE `id` = %s"
        cursor.execute(sql, ('05',))
        connection.commit()




#Created Table
import pymysql.cursors


connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='learning',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with connection.cursor() as cursor:
        
        create_table_query = """
        CREATE TABLE employeee (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50),
            age INT,
            dept VARCHAR(10)
        )
        """
       
        cursor.execute(create_table_query)
   
    connection.commit()
finally:
    connection.close()



#Drop
import pymysql.cursors

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='learning',
    cursorclass=pymysql.cursors.DictCursor
)

with connection:
    with connection.cursor() as cursor:
       
        sql = "DROP TABLE  `employee3`"
        cursor.execute(sql)
        connection.commit()




#Alter

import pymysql.cursors

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='learning',
    cursorclass=pymysql.cursors.DictCursor
)


with connection:
    with connection.cursor() as cursor:
       
        sql = "ALTER TABLE `employeee` ADD COLUMN `email` VARCHAR(100)"
        cursor.execute(sql)
        connection.commit()
        print("Column 'email' added to the 'employeee' table.")


#Update
import pymysql.cursors

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='learning',
    cursorclass=pymysql.cursors.DictCursor
)
with connection:
    with connection.cursor() as cursor:
        sql = "UPDATE `employeee` SET `email` = %s WHERE `dept` = %s"
        sql = "UPDATE `employeee` SET `email` = %s WHERE `dept` = %s"
        sql = "UPDATE `employeee` SET `email` = %s WHERE `dept` = %s"
        sql = "UPDATE `employeee` SET `email` = %s WHERE `dept` = %s"
        sql = "UPDATE `employeee` SET `email` = %s WHERE `dept` = %s"
        cursor.execute(sql, ('chowdary@gmail.com', 'ece'))
        cursor.execute(sql, ('chinna@gmail.com', 'mech'))
        cursor.execute(sql, ('gopal@gmail.com', 'cse'))
        cursor.execute(sql, ('cherry@gmail.com', 'eee'))
        cursor.execute(sql, ('murthy@gmail.com', 'civil'))
        connection.commit()


#Truncate

import pymysql.cursors


connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='learning',
    cursorclass=pymysql.cursors.DictCursor
)

with connection:
    with connection.cursor() as cursor:
            
        sql = "TRUNCATE TABLE `student`"
        cursor.execute(sql)
        connection.commit()
        print("Table 'employee' truncated successfully.")
