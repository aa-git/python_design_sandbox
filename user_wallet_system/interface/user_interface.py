from abc import ABC, abstractmethod

class user_interface(ABC):

    @abstractmethod
    def menu():
        raise NotImplemented()
                
    @abstractmethod
    def give_id():
        raise NotImplemented()

    @abstractmethod
    def send_money(self, to_user_id, amt):
        raise NotImplemented()
    
    @abstractmethod
    def load_money_to_wallet(self, amt):
        raise NotImplemented()
    
    @abstractmethod
    def register(self):
        raise NotImplemented()
    
    @abstractmethod
    def get_balance(self):
        raise NotImplemented()