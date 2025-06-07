from abc import ABC, abstractmethod

class database(ABC):

    @abstractmethod
    def get_user(id):
        raise NotImplemented()

    @abstractmethod
    def get_user_passbook_history(user_id):
        raise NotImplemented()

    @abstractmethod
    def add_new_user(user):
        raise NotImplemented()
    
    @abstractmethod
    def user_exists(user_id):
        raise NotImplemented()

    @abstractmethod
    def log(user_id, to_user_id, amt, action):
        raise NotImplemented()