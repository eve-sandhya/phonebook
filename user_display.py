from Database_connect import *
def select_records():
    db_info = read_db_config()
    sql_query = """SELECT * FROM person"""
    try:
        conn = mysql.connector.connect(**db_info)
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(sql_query)
            rows = cursor.fetchall()
            print("Total rows : ", cursor.rowcount)

            for row in rows:
                print(row)
    except:
        print("Error : " + sys.exc_info()[1])
    finally:
        cursor.close()
        conn.close()
def display_records():
    db_info = {'host': 'localhost', 'database': 'project', 'user': 'root', 'password': ''}
    sql_query = """SELECT * FROM person"""
    try:
        conn = mysql.connector.connect(**db_info)
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(sql_query)
            rows = cursor.fetchall()
            print("Total rows : ", cursor.rowcount)

            for row in rows:
                print(row)
    except:
        print("Error : " + sys.exc_info()[1])
    finally:
        cursor.close()
        conn.close()