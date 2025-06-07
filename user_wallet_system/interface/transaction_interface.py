from abc import ABC, abstractmethod

class transaction_interface(ABC):

    @abstractmethod
    def send_money(from_user_id, to_user_id, amt):
        raise NotImplemented()
    
    @abstractmethod
    def menu(user_id):    
        raise NotImplemented()
        
    @abstractmethod
    def load_money(user, amt):
        raise NotImplemented()
