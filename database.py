import mysql.connector
from mysql.connector import Error
from model import Create_Event, Event

host_name='78.128.76.186'
database_name='event_calendar'
username='alex'
password_DB='SwyQcGYvKEXubkjXfCJEMLnRB'

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
            cursor.execute("INSERT INTO event_calendar.Event (name,start_date, end_date, type, description, picture) VALUES (%s, %s, %s, %s, %s, %s)", (event.name,event.start_date,event.end_date, event.type, event.description, event.picture))
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
            rows = cursor.fetchall()
            cursor.close()
            connection.close()
            return rows
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
            row = cursor.fetchone()
            cursor.close()
            connection.close()
            return row
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
            cursor.execute("UPDATE event_calendar.Event SET name=%s,start_date=%s, end_date= %s, type= %s, description= %s, picture= %s WHERE id = %s", (event.name,event.start_date,event.end_date, event.type, event.description, event.picture, id))
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
        