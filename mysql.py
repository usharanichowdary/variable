import pymysql.cursors


connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='sql learning',
                             cursorclass=pymysql.cursors.DictCursor)

try:
       with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `fruits` (`colour`, `name`,`price`,`exp_date`) VALUES (%s,%s,%s,%s)"
            cursor.execute(sql, ('green', 'grapes',87,'2024-06-05'))
        connection.commit()

except pymysql.error as e:
    print(f"error: {e}")

finally:
    connection.close()
    

import pymysql.cursors


connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='sql learning',
                             cursorclass=pymysql.cursors.DictCursor)


with connection:
    with connection.cursor() as cursor:
        sql = "INSERT INTO`fruits` (`colour`, `name`,`price`,`exp_date`) VALUES (%s,%s,%s,%s)"
        cursor.execute(sql, ('blue', 'berry',89,'2024-05-06'))
        connection.commit()




#student table
import pymysql.cursors


connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='sql learning',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with connection.cursor() as cursor:
        
        create_table_query = """
        CREATE TABLE student (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50),
            age INT,
            grade VARCHAR(10)
        )
        """
       
        cursor.execute(create_table_query)
   
    connection.commit()
finally:
    connection.close()


#for inserting student data

import pymysql.cursors


connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='sql learning',
                             cursorclass=pymysql.cursors.DictCursor)


with connection:
    with connection.cursor() as cursor:
        sql = "INSERT INTO`student` (`id`, `name`,`age`,`grade`) VALUES (%s,%s,%s,%s)"
        cursor.execute(sql, (4, 'chinna',26,'C'))
        cursor.execute(sql, (5, 'leela',29,'D'))

        connection.commit()