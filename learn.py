

# #staff table
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
        CREATE TABLE staff (
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



#Update

import pymysql.cursors


connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='learning',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    
    with connection.cursor() as cursor:
        sql = "UPDATE `staff` SET `age`=%s WHERE 'name'= %s"
        cursor.execute(sql,(35,'suma'))
        

        connection.commit()
        print("Update successful")

except pymysql.MySQLError as e:
    print(f"Error: {e}")
finally:
   
    connection.close()





import pymysql.cursors


connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='learning',
                             cursorclass=pymysql.cursors.DictCursor)


with connection:
    with connection.cursor() as cursor:
        sql = "INSERT INTO`staff` (`id`, `name`,`age`,`grade`) VALUES (%s,%s,%s,%s)"
        cursor.execute(sql, ('05', 'rani',24,'A'))
        connection.commit()