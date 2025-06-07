from datetime import datetime
class database():
    '''
    data structure: is a dict/hashmap, user_id as key, value as [ user object, record of transactions ]
    the second value ' record of transactions' is a simple list as of now
    '''
    store = {}

    def get_user(id):
        if database.store.__contains__(id):
            return database.store[id][0]
        raise NotFoundInDatabase("user not in DB with id:"+str(id))

    def get_user_passbook_history(user_id):
        return database.store[user_id][1]

        
    def add_new_user(user):
        database.store[user.id] = [user, []]
        return
    
    def user_exists(user_id):
        if database.store.__contains__(user_id):
            return True
        raise NotFoundInDatabase("user not in DB with id:"+str(id))

    def log(user_id, to_user_id, amt, action):
        database.store[user_id][1] += [ [user_id, to_user_id, amt, action, datetime.now().strftime("%Y-%m-%d %H:%M:%S")]   ]

class NotFoundInDatabase(Exception):
    pass