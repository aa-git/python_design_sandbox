
import sys
sys.path.append("../")

from interface.wallet_interface import  wallet_interface

class wallet(wallet_interface):
    def __init__(self, initial_balance):
        self.balance = initial_balance

    def get_balance(self):
        return self.balance
    
    
    def debit_money(self, debit_amt):
        if self.is_debit_possible(debit_amt):
            self.balance -= debit_amt
            return True
        return False
    
    def credit_money(self, credit_amt):
        if credit_amt<=0:
            raise debit_exception("credit amt <=0")
        self.balance += credit_amt
        return True
    
    def is_debit_possible(self, debit_amt):
        if debit_amt<=0:
            raise debit_exception("debit amt <=0")
        if self.balance<debit_amt:
            raise debit_exception("debit amt "+str(debit_amt)+" more than balance "+str(self.balance))
        return True
    
class debit_exception(Exception):
    pass
