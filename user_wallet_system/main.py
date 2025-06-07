import constants
import sys
import os
import time
sys.path.append('..')
from classes.user import user
from classes.database import database

main_menu = 'what action you want to do\n\
    '+constants.ADD_USER[constants.text]+'\n\
    '+constants.USER_OPTIONS[constants.text]+'\n\
    '+constants.EXIT[constants.text]+'\n'

def homepage():
    flag=True
    while flag:
        print("\n-------------------------------------------------------\n")
        try:
            action = input(main_menu)
            match action:
                case 'a':
                    name = input("enter name for new user: ")
                    user_created = user(name)
                    database.add_new_user(user_created)
                    print("user added, with id="+str(user_created.id))
                    
                case 'u':
                    user.menu()
                        
                case 'e':
                    print("exiting")
                    flag=False

                case default:
                    print("enter valid action")
        except Exception as e:
            print(e)

if __name__ == '__main__':
    homepage()