import sys
from Database_connect import *
def insert_record():
    db_info={"host":"localhost","database":"project","user":"root","password":""}
    sql_query_insert="""insert into person(Person_name,Phone_no)values(%s, %s)"""
    Person_name=input("Enter name : ")
    Phone_number=int(input("Enter Number : "))
    values_insert=(Person_name,Phone_number)
    try:
        conn = mysql.connector.connect(**db_info)
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(sql_query_insert, values_insert)
            conn.commit()
            print("Insertion complete!!!")
    except:
        print("Error : ",sys.exc_info())
    finally:
        cursor.close()
        conn.close()
def update_record():
    db_info = {"host": "localhost", "database": "project", "user": "root", "password": ""}
    sql_query_update = """UPDATE `person` SET `Person_name`=%s,`Phone_no`=%s WHERE Person_name=%s """
    Person_name_old=input("Enter the name to be update : ")
    Person_name_new=input("Enter Updated name : ")
    Phone_no_new=int(input("Enter updated Number : "))
    values_update=(Person_name_new,Phone_no_new,Person_name_old)
    try:
        conn = mysql.connector.connect(**db_info)
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(sql_query_update,values_update)
            print("Update record successfully")
            conn.commit()
    except:
        print("Error : " ,sys.exc_info()[1])
    finally:
        cursor.close()
        conn.close()

