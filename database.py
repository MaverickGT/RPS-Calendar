import mysql.connector # type: ignore
from mysql.connector import Error # type: ignore
from model import Create_Event
import json
import os
from dotenv import load_dotenv

load_dotenv()
host_name=os.getenv('DB_HOST')
database_name=os.getenv('DB_NAME')
username=os.getenv('DB_USER')
password_DB=os.getenv('DB_PASSWORD')

def connect_to_mariadb():
    """Connects to a MariaDB database and prints the database version."""
    try:
        connection = mysql.connector.connect(
            host=host_name,
            database=database_name,
            user=username,
            password=password_DB
        )
        
        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"Successfully connected to MariaDB server version {db_info}")
            connection.close()
    except Error as e:
        print(f"Error: {e}")

def add_item_to_database(event: Create_Event):
    """Adds an item to the database."""
    try:
        connection = mysql.connector.connect(
            host=host_name,
            database=database_name,
            user=username,
            password=password_DB
        )
        if connection.is_connected():
            cursor = connection.cursor()
            if event.type == "QTO":
                event.color = "#17EBA0"
            elif event.type == "ALT":
                event.color = "#FFBC44"
            elif event.type == "CHC":
                event.color = "#00C8FF"
            cursor.execute("INSERT INTO event_calendar.Event (name,start_date, end_date, type, color, description,start_time, end_time, all_day, location) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (event.name,event.start_date,event.end_date, event.type, event.color,event.description,event.start_time, event.end_time, event.all_day, event.location))
            connection.commit()
            if cursor.rowcount > 0:
                cursor.close()
                connection.close()
                return True
            else:
                cursor.close()
                connection.close()
                return False
            
    except Error as e:
        print(f"Error: {e}")

def get_items_from_database():
    """Gets all items from the database."""
    try:
        connection = mysql.connector.connect(
            host=host_name,
            database=database_name,
            user=username,
            password=password_DB
        )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM event_calendar.Event")
            columns = [column[0] for column in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
            cursor.close()
            connection.close()
            # print(data)
            return data
    except Error as e:
        print(f"Error: {e}")
        return []

def get_item_from_database(id):
    """Gets an item from the database by its id."""
    try:
        connection = mysql.connector.connect(
            host=host_name,
            database=database_name,
            user=username,
            password=password_DB
        )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM event_calendar.Event WHERE id = %s", (id,))
            columns = [column[0] for column in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
            return data[0]
    except Error as e:
        print(f"Error: {e}")
    return None
        
def update_item_in_database(id, event:Create_Event):
    """Updates an item in the database by its id."""
    try:
        connection = mysql.connector.connect(
            host=host_name,
            database=database_name,
            user=username,
            password=password_DB
        )
        if connection.is_connected():
            cursor = connection.cursor()
            if event.type == "QTO":
                event.color = "#17EBA0"
            elif event.type == "ALT":
                event.color = "#FFBC44"
            elif event.type == "CHC":
                event.color = "#00C8FF"
            cursor.execute("UPDATE event_calendar.Event SET name=%s,start_date=%s, end_date= %s, type= %s,color=%s, description= %s, start_time= %s, end_time= %s, all_day= %s , location=%s WHERE id = %s", (event.name,event.start_date,event.end_date, event.type, event.color,event.description,event.start_time, event.end_time, event.all_day, event.location, id)) 
            connection.commit()
            if cursor.rowcount > 0:
                cursor.close()
                connection.close()
                return True
            else:
                cursor.close()
                connection.close()
                return False
    except Error as e:
        print(f"Error: {e}")

def delete_item_from_database(id):
    """Deletes an item from the database by its id."""
    try:
        connection = mysql.connector.connect(
            host=host_name,
            database=database_name,
            user=username,
            password=password_DB
        )
        if connection.is_connected():
            cursor = connection.cursor()
            delete_query = """DELETE FROM event_calendar.Event WHERE id = %s""" 
            cursor.execute(delete_query, (id,))
            connection.commit()
            if cursor.rowcount > 0:
                cursor.close()
                connection.close()
                return True
            else:
                cursor.close()
                connection.close()
                return False
    except Error as e:
        print(f"Error: {e}")

def get_legend_from_DB():
    """Gets the legend from the database and returns a JSON object."""
    try:
        connection = mysql.connector.connect(
            host=host_name,
            database=database_name,
            user=username,
            password=password_DB
        )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT DISTINCT Type FROM event_calendar.Event")
            rows = cursor.fetchall()
            legend=[row[0] for row in rows]
            cursor.close()
            connection.close()
            return legend
    except Error as e:
        print(f"Error: {e}")

def add_user_to_database(admin_username, admin_password, salt):
    """Adds an admin user to the database."""
    try:
        connection = mysql.connector.connect(
            host=host_name,
            database=database_name,
            user=username,
            password=password_DB
        )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("INSERT INTO event_calendar.users (username,password,salt) VALUES (%s, %s, %s)", (admin_username, admin_password, salt))
            connection.commit()
            if cursor.rowcount > 0:
                cursor.close()
                connection.close()
                return True
            else:
                cursor.close()
                connection.close()
                return False
    except Error as e:
        print(f"Error: {e}")

def get_user_from_database(admin_username):
    """Gets an admin user from the database by its username."""
    try:
        connection = mysql.connector.connect(
            host=host_name,
            database=database_name,
            user=username,
            password=password_DB
        )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM event_calendar.users WHERE username = %s", (admin_username,))
            row = cursor.fetchone()
            cursor.close()
            connection.close()
            return row
    except Error as e:
        print(f"Error: {e}")
    return None

def add_feedback_to_database(name, email, description):
    """Adds feedback to the database."""
    try:
        connection = mysql.connector.connect(
            host=host_name,
            database=database_name,
            user=username,
            password=password_DB
        )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("INSERT INTO event_calendar.Feedback (name, email, description) VALUES (%s, %s, %s)", (name, email, description))
            connection.commit()
            if cursor.rowcount > 0:
                cursor.close()
                connection.close()
                return True
            else:
                cursor.close()
                connection.close()
                return False
    except Error as e:
        print(f"Error: {e}")

def get_feedback_items_from_database():
    """Gets all items from the Feedback table."""
    try:
        connection = mysql.connector.connect(
            host=host_name,
            database=database_name,
            user=username,
            password=password_DB
        )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM event_calendar.Feedback")
            columns = [column[0] for column in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
            cursor.close()
            connection.close()
            return data
    except Error as e:
        print(f"Error: {e}")
        return []

def get_feedback_from_database(id):
    """Gets an item from the database by its id."""
    try:
        connection = mysql.connector.connect(
            host=host_name,
            database=database_name,
            user=username,
            password=password_DB
        )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM event_calendar.Event WHERE id = %s", (id,))
            name = cursor.fetchone()[0]
            return name
    except Error as e:
        print(f"Error: {e}")
    return None
        
def delete_all_feedback_from_database():
    """Deletes all items from the database."""
    try:
        connection = mysql.connector.connect(
            host=host_name,
            database=database_name,
            user=username,
            password=password_DB
        )
        if connection.is_connected():
            cursor = connection.cursor()
            delete_query = """DELETE FROM event_calendar.Feedback"""
            cursor.execute(delete_query)
            connection.commit()
            if cursor.rowcount > 0:
                cursor.close()
                connection.close()
                return True
            else:
                cursor.close()
                connection.close()
                return False
    except Error as e:
        print(f"Error: {e}")

def delete_feedback_from_database_by_id(id):
    """Deletes an item from the database by its id."""
    try:
        connection = mysql.connector.connect(
            host=host_name,
            database=database_name,
            user=username,
            password=password_DB
        )
        if connection.is_connected():
            cursor = connection.cursor()
            delete_query = """DELETE FROM event_calendar.Feedback WHERE id = %s"""
            cursor.execute(delete_query, (id,))
            connection.commit()
            if cursor.rowcount > 0:
                cursor.close()
                connection.close()
                return True
            else:
                cursor.close()
                connection.close()
                return False
    except Error as e:
        print(f"Error: {e}")