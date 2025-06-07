import sys
sys.path.append("../")


from interface.transaction_interface import  transaction_interface
from .database import database

class transaction(transaction_interface):
    MENU = 'what action you want to perform\n\
    s: see transaction history\n\
    t: see transaction history sorted by time \n\
    a: see transaction history sorted by amt \n\
    b: back\n'
    
    SEND_MONEY = 'money received: from -> to'
    LOAD_MONEY = 'load money'
    RECEIVE_MONEY = 'receive money'
    SELF ='self'

    def send_money(from_user_id, to_user_id, amt):
        from_ = database.get_user(from_user_id)
        to_ = database.get_user(to_user_id)

        if from_.get_balance() >= amt and amt>0:
            from_.wallet.balance -= amt
            to_.wallet.balance += amt

        database.log(from_user_id, to_user_id, amt, transaction.SEND_MONEY)
        database.log(to_user_id, from_user_id, amt, transaction.RECEIVE_MONEY)
    
    def menu(user_id):    
        flag=True
        while flag:
            action = input(transaction.MENU)
            try:
                match action:
                    case 's':
                        passbook = database.get_user_passbook_history(user_id)
                        for entry in passbook:
                            print (entry)
                        print("\n-------------------------------------\n")

                    case 't':
                        pass
                        
                    case 'a':
                        pass

                    case 'b':
                        return
                    
                    case default:
                        print("enter valid action")        
            except Exception as e:
                print(e)
        

    def load_money(user, amt):
        
        if amt<=0:
            raise InvalidAmount("amount should be more than 0")
        user.wallet.balance += amt

        database.log(user.id, transaction.SELF, amt, transaction.LOAD_MONEY)

class InvalidAmount(Exception):
    ...

        


