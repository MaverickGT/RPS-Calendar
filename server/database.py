import mysql.connector
from mysql.connector import Error
from model import Create_Event, Event

host_name='localhost',
database_name='your_database_name',
username='your_username',
password_DB='your_password'

def connect_to_mariadb():
    """Connects to a MariaDB database and prints the database version."""
    try:
        # Connection parameters
        connection = mysql.connector.connect(
            host=host_name,
            database=database_name,
            user=username,
            password=password_DB
        )
        
        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"Successfully connected to MariaDB server version {db_info}")
            # Close the connection
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
            cursor.execute("INSERT INTO items (name,start_date, end_date, type, description, picture) VALUES (%s, %s, %s, %s, %s)", (event.name,event.start_date,event.end_date, event.type, event.description, event.picture))
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
            host=host_name,
            database=database_name,
            user=username,
            password=password_DB
        )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM items")
            rows = cursor.fetchall()
            items = []
            for row in rows:
                event = Event(
                    id=row[0],
                    name=row[1],
                    start_date=row[2],
                    end_date=row[3],
                    type=row[4],
                    description=row[5],
                    picture=row[6]
                )
                items.append(event)
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
            host=host_name,
            database=database_name,
            user=username,
            password=password_DB
        )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM items WHERE id = %s", (id,))
            row = cursor.fetchone()
            if row:
                item = Event(
                    id=row[0],
                    name=row[1],
                    start_date=row[2],
                    end_date=row[3],
                    type=row[4],
                    description=row[5],
                    picture=row[6]
                )
                cursor.close()
                connection.close()
                return item
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
            cursor.execute("UPDATE items SET name=%s,start_date=%s, end_date= %s, type= %s, description= %s, picture= %s WHERE id = %s", (event.name,event.start_date,event.end_date, event.type, event.description, event.picture, id))
            connection.commit()
            cursor.close()
            connection.close()
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
            delete_query = """DELETE FROM your_table_name WHERE id = %s"""  # Change 'your_table_name' to your table's name
            cursor.execute(delete_query, (id,))
            connection.commit()
            cursor.close()
            connection.close()
            print("Record deleted successfully")
    except Error as e:
        print(f"Error: {e}")

def get_legend_from_DB():
    #we will need a table for Type and their description
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
            cursor.execute("SELECT DISTINCT Type, description, color FROM events")
            rows = cursor.fetchall()
            legend = {row[0]: {'description': row[1], 'color': row[2]} for row in rows}
            cursor.close()
            connection.close()
            return legend
    except Error as e:
        print(f"Error: {e}")