from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_mail import Mail, Message
import database
from model import Create_Event

app = Flask(__name__)
CORS(app)

#Gmail wont work- you need to enable less secure apps in your google account
app.config['MAIL_SERVER']='smtp-mail.outlook.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'hpecalendar@outlook.com'
app.config['MAIL_PASSWORD'] = 'adminadmin12'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)


@app.route('/api/home', methods=['GET'])
def home():
    return jsonify({'message': 'Hello, World!'})

@app.route('/api/items', methods=['GET'])
def get_items():
    items = [
        {
            'id': 1,
            'name': 'Event1',
            'start_date': '2024-03-06',
            'end_date': '2024-03-07',
            'type': 'TypeA',
            'description': 'This is a description of the item',
            'picture': 'ulr to picture of the item'
        },
        {
            'id': 2,
            'start_date': '2024-03-07',
            'end_date': '2024-03-07',
            'type': 'TypeB',
            'description': 'This is a description of the item',
            'picture': 'ulr to picture of the item'
        }
        # Add more items as needed
    ]
    #after implementing the database, replace the above items with the following line
    #items = database.get_items_from_database()
    return jsonify(items)

@app.route('/api/items/<int:id>', methods=['GET'])
def get_item(id):
    items = [
        {
            'id': 1,
            'name': 'Event1',
            'start_date': '2024-03-06',
            'end_date': '2024-03-07',
            'type': 'TypeA',
            'description': 'This is a description of the item',
            'picture': 'ulr to picture of the item'
        },
        {
            'id': 2,
            'name': 'Event2',
            'start_date': '2024-03-07',
            'end_date': '2024-03-07',
            'type': 'TypeB',
            'description': 'This is a description of the item',
            'picture': 'ulr to picture of the item'
        }
        # Add more items as needed
    ]
    item = next((item for item in items if item['id'] == id), None)
    #after implementing the database, replace the above items with the following line
    # items = database.get_item_from_database(id)
    if item:
        return jsonify(item)
    return jsonify({'message': 'Item not found'}), 404

@app.route('/api/add', methods=['POST'])
#admin
def add_item():
    data = request.get_json()  # Get data from POST request
    name=data.get('name')
    start_date = data.get('start_date')
    end_date = data.get('end_date')
    type = data.get('type')
    description = data.get('description')
    picture = data.get('picture')
    event = Create_Event(name,start_date, end_date, type, description, picture)

    database.add_item_to_database(event)
    return jsonify({'message': 'Item added'}), 201

@app.route('/api/update/<int:id>', methods=['PUT'])
#admin
def update_item(id):
    event=get_item(id)
    data = request.get_json()  # Get data from PUT request
    name=data.get('name')
    start_date = data.get('start_date')
    end_date = data.get('end_date')
    type = data.get('type')
    description = data.get('description')
    picture = data.get('picture')
    event=Create_Event(name,start_date, end_date, type, description, picture)
    database.update_item_in_database(id, event)
    #can return new updated item if needed
    return jsonify({'message': 'Item updated'}), 200


@app.route('/api/delete/<int:id>', methods=['DELETE'])
#admin
def delete_item(id):
    #after implementing the database, call the delete_item_from_database function
    database.delete_item_from_database(id)
    return jsonify({'message': 'Item deleted'}), 200

@app.route('/api/feedback', methods=['POST'])
def send_feedback():
    data = request.get_json()
    customer_name = data.get('name')
    customer_email = data.get('email')
    feedback = data.get('feedback')

    # Our mailbox send the feedback to herself
    msg = Message('New Feedback', sender="hpecalendar@outlook.com", recipients=["hpecalendar@outlook.com"])
    msg.body = f"Name: {customer_name}\nEmail: {customer_email}\nFeedback: {feedback}"
    mail.send(msg)

    return jsonify({'message': 'Feedback sent'}), 200

@app.route('/api/legend', methods=['GET'])
def get_legend():
    legend = database.get_legend_from_DB()
    return jsonify(legend)

#update delete legend
if __name__ == '__main__':
    app.run(debug=True, port=8081)
