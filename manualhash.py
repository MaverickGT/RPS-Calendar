import hashlib
import database

def hash_password(password, salt):
    password_hash = hashlib.sha256((password + salt).encode('utf-8')).hexdigest()
    print(password_hash)
    return password_hash


username = input("Enter username: ")
password = input("Enter password: ")
salt = input("Enter salt: ")
hashed_password = hash_password(password, salt)
database.add_user_to_database(username, hashed_password, salt)