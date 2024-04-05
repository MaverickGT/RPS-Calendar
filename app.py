from flask import Flask, jsonify, request, render_template
from flask_mail import Mail, Message
from flask_cors import CORS
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


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/api/items', methods=['GET'])
def get_items():
    items = database.get_items_from_database()
    return jsonify(items)

@app.route('/api/items/<int:id>', methods=['GET'])
def get_item(id):
    item = database.get_item_from_database(id)
    if item:
        return jsonify(item)
    return jsonify({'message': 'Item not found'}), 404

@app.route('/api/add', methods=['POST'])
#admin
def add_item():
    data = request.get_json()
    name=data.get('name')
    start_date = data.get('start_date')
    end_date = data.get('end_date')
    type = data.get('type')
    color = data.get('color')
    description = data.get('description')
    picture = data.get('picture')
    start_time = data.get('start_time')
    end_time = data.get('end_time')
    all_day = data.get('all_day')
    event = Create_Event(name,start_date, end_date, type, color, description, picture, start_time, end_time, all_day)
    if database.add_item_to_database(event):
        return jsonify({'message': 'Item added'}), 201
    return jsonify({'message': 'Item not added'}), 400

@app.route('/api/update/<int:id>', methods=['PUT'])
#admin
#TODO:validators
def update_item(id):
    event=get_item(id)
    data = request.get_json()
    name=data.get('name')
    start_date = data.get('start_date')
    end_date = data.get('end_date')
    type = data.get('type')
    color = data.get('color')
    description = data.get('description')
    picture = data.get('picture')
    start_time = data.get('start_time')
    end_time = data.get('end_time')
    all_day = data.get('all_day')
    event=Create_Event(name,start_date, end_date, type, color, description, picture, start_time, end_time, all_day)
    if database.update_item_in_database(id, event):
        return jsonify({'message': 'Item updated'}), 200
    else:
        return jsonify({'message': 'Item not updated'}), 400


@app.route('/api/delete/<int:id>', methods=['DELETE'])
#admin
#TODO:validators
def delete_item(id):
    if database.delete_item_from_database(id):
        return jsonify({'message': 'Item deleted'}), 200
    else:
        return jsonify({'message': 'Item not deleted'}), 400
    
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


if __name__ == '__main__':
    app.run(debug=True, port=8081)
