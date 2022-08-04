import mysql.connector

inf = input('введіть дані: ')

def datab(inf):   
    connection = mysql.connector.connect(host='localhost',
                                     database='',
                                    user='',
                                    password='')
    cursor = connection.cursor()
    cursor.execute("insert into test (title) VALUES ('%s')"%(inf))
    connection.commit()
    cursor.close()

datab(inf)