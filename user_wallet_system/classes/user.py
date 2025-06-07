import sys
sys.path.append("..")


from interface.user_interface import  user_interface
import constants

from .transaction import transaction
from .wallet import wallet
from .database import database



class user(user_interface):
    counter = 0
    user_menu = 'what user action you want to perform\n\
    lb: loab balance\n\
    sm: send money\n\
    b: back\n\
    fb: fetch balance\n\
    th: transaction history\n'

    def menu():
        user_id = (int)(input("give user id: "))
        fetched_user = database.get_user(user_id)
        flag=True
        while flag:
            print("\n-------------------------------------------------------\n")
            user_action = input("user id = "+str(user_id)+"\n"+user.user_menu)
            try:
                match user_action:
                    case 'lb':
                        amt = (float)(input("enter amt to load: "))
                        fetched_user.load_money_to_wallet(amt)
                        print("amount loaded")

                    case 'sm':
                        to_user_id = (int)(input("enter user id to send money to: "))
                        database.user_exists(to_user_id)
                        amt = (float)(input("enter amt to be sent: "))
                        fetched_user.send_money(to_user_id, amt)
                        print("money sent")
                        
                    case 'fb':
                        print("balance = "+str(fetched_user.get_balance()))
                    
                    case 'th':
                        transaction.menu(user_id)

                    case 'b': #back
                        return
                    
                    case default:
                        print("enter valid action")        
            except Exception as e:
                print(e)
                

    def give_id(): #static method, class level
        user.counter += 1
        return user.counter

    def __init__(self, name_):
        self.name = name_
        self.id = user.give_id()
        self.wallet = wallet(0)
        self.registered = False
    
    def send_money(self, to_user_id, amt):
        transaction.send_money(self.id, to_user_id, amt)
        return True
    
    def load_money_to_wallet(self, amt):
        transaction.load_money(self, amt)
    
    def register(self):
        self.registered = True
    
    def get_balance(self):
        return self.wallet.balance
        