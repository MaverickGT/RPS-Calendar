import hashlib
from database import add_user_to_database

def hash_password(password, salt):
    password_hash = hashlib.sha256((password + salt).encode('utf-8')).hexdigest()
    return password_hash


username = input("Enter username: ")
password = input("Enter password: ")
salt = input("Enter salt: ")
hashed_password = hash_password(password, salt)
message = add_user_to_database(username, hashed_password, salt)

if message:
    print("User added successfully.")
else:
    print("Something went wrong.")