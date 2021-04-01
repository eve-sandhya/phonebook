import mysql.connector
import sys

def connect_db():
    # Connect MySQL Database Server
    try:
        conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password =''
        )

        conn.close()
    except:
        print("Error :", sys.exc_info()[1])
connect_db()