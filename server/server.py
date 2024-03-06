from flask import Flask, jsonify
from flask_cors import CORS
import database

app = Flask(__name__)
CORS(app)

#define an app route to get home message
@app.route('/api/home', methods=['GET'])
def home():
    return jsonify({'message': 'Hello, World!'})

#define an app route to get items from database
@app.route('/api/items', methods=['GET'])
def get_items():
    items = [
        {
            'id': 1,
            'date': '2024-03-06',
            'type': 'TypeA'
        },
        {
            'id': 2,
            'date': '2024-03-07',
            'type': 'TypeB'
        }
        # Add more items as needed
    ]
    #after implementing the database, replace the above items with the following line
    #items = database.get_items_from_database()
    return jsonify(items)

#create app route to get item by id
@app.route('/api/items/<int:id>', methods=['GET'])
def get_item(id):
    items = [
        {
            'id': 1,
            'date': '2024-03-06',
            'type': 'TypeA'
        },
        {
            'id': 2,
            'date': '2024-03-07',
            'type': 'TypeB'
        }
        # Add more items as needed
    ]
    item = next((item for item in items if item['id'] == id), None)
    #after implementing the database, replace the above items with the following line
    # items = database.get_item_from_database(id)
    if item:
        return jsonify(item)
    return jsonify({'message': 'Item not found'}), 404

#create app route to add item to database
@app.route('/api/items', methods=['POST'])
def add_item():
    database.add_item_to_database('2024-03-08', 'TypeC')
    return jsonify({'message': 'Item added'}), 201

if __name__ == '__main__':
    app.run(debug=True, port=8081)