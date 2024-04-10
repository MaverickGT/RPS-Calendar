from flask import Flask, jsonify, request, render_template
from flask_mail import Mail, Message # type: ignore
from flask_cors import CORS # type: ignore
import database
import os
from model import Create_Event
from manager import check_username_and_password
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity # type: ignore

app = Flask(__name__)
CORS(app)
app.config['JWT_SECRET_KEY'] =  os.urandom(64)
jwt = JWTManager(app)

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

@app.route('/api/admin/login', methods=['GET','POST'])
def admin_login():
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not check_username_and_password(username, password):
            return jsonify({'message': 'Bad credentials'}), 401

        access_token = create_access_token(identity=username)

        return jsonify(access_token=access_token), 200
    else:
        return render_template('login.html')

@app.route('/api/admin', methods=['GET'])
def admin():
    return render_template('admin.html')

@app.route('/api/items', methods=['GET'])
def get_items():
    items = database.get_items_from_database()
    for item in items:
        if item['all_day'] == 1:
            item['all_day'] = True
        else:
            item['all_day'] = False
    return jsonify(items)

@app.route('/api/items/<int:id>', methods=['GET'])
def get_item(id):
    item = database.get_item_from_database(id)
    if item:
        return jsonify(item)
    return jsonify({'message': 'Item not found'}), 404

@app.route('/api/admin/add', methods=['POST'])
@jwt_required()
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
    location=data.get('location')
    event = Create_Event(name,start_date, end_date, type, color, description, picture, start_time, end_time, all_day,location)
    if database.add_item_to_database(event):
        return jsonify({'message': 'Item added'}), 201
    return jsonify({'message': 'Item not added'}), 400

@app.route('/api/admin/update/<int:id>', methods=['PUT'])
@jwt_required()
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
    location=data.get('location')
    event=Create_Event(name,start_date, end_date, type, color, description, picture, start_time, end_time, all_day,location)
    if database.update_item_in_database(id, event):
        return jsonify({'message': 'Item updated'}), 200
    else:
        return jsonify({'message': 'Item not updated'}), 400


@app.route('/api/admin/delete/<int:id>', methods=['DELETE'])
@jwt_required()
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
    
    if not customer_name or not customer_email or not feedback:
        return jsonify({'message': 'Missing data'}), 400

    if " " in customer_email:
        return jsonify({'message': 'Invalid Email'}), 400
    
    if not '@hpe.com' in customer_email:
        return jsonify({'message': 'You need you use your HPE email'}), 400
    
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
