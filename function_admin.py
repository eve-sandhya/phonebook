import sys
from Admin_control import *
try:
    def admin_login():
        print("Enter Username : ")
        name = input()
        if name == "admin":
            print("password:", end="")
            password = int(input())
            if password==9840:
                admin_control()
            else:
                print("\033[31mLogin failed!!!Try Again!!\033[0m")
                admin_login()

        else:
            print("\033[31mLogin failed!!!Try Again!!\033[0m")
            admin_login()
    admin_login()
except:
    print("Error:",sys.exc_info())
