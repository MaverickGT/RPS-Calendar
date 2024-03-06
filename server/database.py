import mysql.connector
from mysql.connector import Error

def connect_to_mariadb():
    """Connects to a MariaDB database and prints the database version."""
    try:
        # Connection parameters
        connection = mysql.connector.connect(
            host='localhost',
            database='your_database_name',
            user='your_username',
            password='your_password'
        )
        
        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"Successfully connected to MariaDB server version {db_info}")
            # Close the connection
            connection.close()
    except Error as e:
        print(f"Error: {e}")

def add_item_to_database(item):
    """Adds an item to the database."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='your_database name',
            user='your_username',
            password='your_password'
        )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("INSERT INTO items (date, type) VALUES (%s, %s)", item)
            connection.commit()
            print(f"Item added to database with id {cursor.lastrowid}")
            cursor.close()
            connection.close()
    except Error as e:
        print(f"Error: {e}")

def get_items_from_database():
    """Gets all items from the database."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='your_database_name',
            user='your_username',
            password='your_password'
        )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM items")
            rows = cursor.fetchall()
            items = []
            for row in rows:
                items.append({
                    'id': row[0],
                    'date': row[1],
                    'type': row[2]
                })
            cursor.close()
            connection.close()
            return items
    except Error as e:
        print(f"Error: {e}")
        return []

def get_item_from_database(id):
    """Gets an item from the database by its id."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='your_database_name',
            user='your_username',
            password='your_password'
        )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM items WHERE id = %s", (id,))
            row = cursor.fetchone()
            if row:
                item = {
                    'id': row[0],
                    'date': row[1],
                    'type': row[2]
                }
                cursor.close()
                connection.close()
                return item
    except Error as e:
        print(f"Error: {e}")
    return None

        
