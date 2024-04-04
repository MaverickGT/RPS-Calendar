import hashlib
from database import get_user_from_database

def hash_password(password, salt):
    password_hash = hashlib.sha256((password + salt).encode('utf-8')).hexdigest()
    return password_hash

def check_username_and_password(username, password):
    
    if get_user_from_database(username) == None:
        return False
    
    salt = get_user_from_database(username)[3]
    password_hash = hashlib.sha256((password + salt).encode('utf-8')).hexdigest()
    db_password = get_user_from_database(username)[2]
    db_username = get_user_from_database(username)[1]
    
    if db_password == password_hash and username == db_username:
        return True
    else:
        return False

