from Database_connect import *
from function_admin import *
from user_display import *
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
dict={}
while True:
    print("                 ..................................................             ")
    print("                 ..................................................              ")

    print(color.BLUE+color.BOLD + '                             PHONE BOOK                      ' + color.END)
    print("                  ..................................................                ")
    print("                  ..................................................                ")
    print("1.User\n2.Admin\n3.Exit")
    choice = int(input("Identify Yourself first"))
    if choice ==1:
        if len(dict.keys())==0:
            print("nothing to show")
        else:
            select_records()
            display_records()
            name=input("Enter name to search required phone number : ")
            ph_no=dict.get(name,"NO data found")
            print(ph_no)
    elif choice ==2:
        admin_login()
    elif choice ==3:
        break
    else:
        print("Invalid choice")
