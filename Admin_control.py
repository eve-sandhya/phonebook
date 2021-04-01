from Database_connect import *
from user_info import *
def admin_control():
    while True:
        print("1.Enter record\n2.Update Record")
        choice=int(input("Enter your Choice:"))
        if choice==1:
            insert_record()
            cont=input("Do you want to continue?[Y/N]")
            if cont=="Y"or cont=="y":
                continue
            else:
                break
        if choice==2:
            update_record()
            cont=input("Do you want to continue?[Y/N]")
            if cont=="Y" or cont=="y":
                continue
            else:
                break
        else:
            break
