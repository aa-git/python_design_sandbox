from abc import ABC, abstractmethod

class wallet_interface(ABC):

    @abstractmethod
    def get_balance(self):
        raise NotImplemented()
    
    @abstractmethod
    def debit_money(self, debit_amt):
        raise NotImplemented()
    
    @abstractmethod
    def credit_money(self, credit_amt):
        raise NotImplemented()
    
    @abstractmethod
    def is_debit_possible(self, debit_amt):
        raise NotImplemented()
