import mysql.connector
from mysql.connector import Error

def connect():
    """ Connect to Mysql Database"""
    try:
        conn = mysql.connector.connect(host='localhost', database='learn_python', user='root', password='123456')
        if conn.is_connected():
            print("Connected to MySQL Database")

    except Error as e:
        print(e)
    finally:
        conn.close()

if __name__ == 'main':
    connect()
