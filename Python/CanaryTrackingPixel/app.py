import base64
import json
import hashlib
import logging
import sqlite3
from flask import Flask, jsonify, request, render_template
from datetime import datetime
import threading


app = Flask(__name__)
API_URL = 'http://localhost:5000/pixel/'
transparent_pixel_gif = (
    "R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"
)
email_dict = {}
pixel_times_dict = {}

db_connections = threading.local()
db_connections.connection = None  # Initialize thread-local connection

def get_db_connection():
    if not hasattr(db_connections, 'connection') or db_connections.connection is None:
        db_connections.connection = sqlite3.connect('database.db')
    return db_connections.connection

def get_db_cursor():
    connection = get_db_connection()
    return connection.cursor()

def load_data_from_db():
    global email_dict, pixel_times_dict
    db_cursor = get_db_cursor()
    db_cursor.execute('SELECT pixel_hash, recipient, subject FROM email_data')
    rows = db_cursor.fetchall()
    for row in rows:
        pixel_hash, recipient, subject = row
        email_dict[pixel_hash] = {
            'Recipient': recipient,
            'Subject': subject
        }

    db_cursor.execute('SELECT pixel_hash, times FROM pixel_times')
    rows = db_cursor.fetchall()
    for row in rows:
        pixel_hash, times_str = row
        pixel_times_dict[pixel_hash] = times_str.split(',')

load_data_from_db()

def persist_data_to_db():
    global email_dict, pixel_times_dict
    db_cursor = get_db_cursor()

    for pixel_hash, data in email_dict.items():
        db_cursor.execute('INSERT OR REPLACE INTO email_data (pixel_hash, recipient, subject) VALUES (?, ?, ?)',
                          (pixel_hash, data['Recipient'], data['Subject']))
    get_db_connection().commit()

    for pixel_hash, times in pixel_times_dict.items():
        db_cursor.execute('INSERT OR REPLACE INTO pixel_times (pixel_hash, times) VALUES (?, ?)',
                          (pixel_hash, ','.join(times)))
    get_db_connection().commit()


def generate_tracking_pixel(email, subject):
    global email_dict
    pixel_data = f"open:{email}:{subject}"
    pixel_hash = hashlib.sha256(pixel_data.encode()).hexdigest()

    if pixel_hash in email_dict:
        return f"{API_URL}{pixel_hash}"
    else:
        email_dict[pixel_hash] = {
            'Recipient': email,
            'Subject': subject
        }
        persist_data_to_db()
        return f"{API_URL}{pixel_hash}"


@app.route('/', methods=['GET'])
def render_form():
    return render_template('index.html')


@app.route('/add', methods=['POST'])
def add():
    data = request.json
    email = data.get('email')
    subject = data.get('subject')
    pixel_hash = data.get('url').replace(API_URL, '')
    
    if not email or not subject or not pixel_hash:
        return jsonify(error="Email, subject and url are required."), 400

    if pixel_hash not in email_dict:
        email_dict[pixel_hash] = {
            'Recipient': email,
            'Subject': subject
        }

    return jsonify(success=True)


@app.route('/generate_pixel', methods=['POST'])
def generate_pixel():
    data = request.json
    email = data.get('email')
    subject = data.get('subject')
    
    if not email or not subject:
        return jsonify(error="Email and subject are required."), 400

    tracking_pixel = generate_tracking_pixel(email, subject)
    return jsonify(tracking_pixel=tracking_pixel)


@app.route('/check', methods=['GET'])
def check_pixel_times():
    global pixel_times_dict, API_URL, email_dict
    pixel_hash = request.args.get('pixel_hash')
    if pixel_hash is not None:
        pixel_hash = pixel_hash.replace(API_URL, '')
    times = pixel_times_dict.get(pixel_hash, [])
    pixel_info = email_dict.get(pixel_hash)

    if not times or not pixel_info:
        return jsonify([])

    return jsonify([{
        'Recipient': pixel_info['Recipient'],
        'Subject': pixel_info['Subject'],
        'PixelHash': pixel_hash,
        'Times': times
    }])


# Modify the track_pixel function to record the access time
@app.route('/pixel/<pixel_hash>', methods=['GET'])
def track_pixel(pixel_hash):
    global email_dict, transparent_pixel_gif, pixel_times_dict
    if pixel_hash not in email_dict:
        return "", 403

    logging.info(f"Email opened: {json.dumps(email_dict[pixel_hash])}")

    # Record the access time
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if pixel_hash in pixel_times_dict:
        pixel_times_dict[pixel_hash].append(current_time)
    else:
        pixel_times_dict[pixel_hash] = [current_time]
    persist_data_to_db()

    # Return a transparent pixel GIF (1x1)
    response = app.response_class(
        response=base64.b64decode(transparent_pixel_gif),
        content_type='image/gif',
        status=200
    )
    return response


if __name__ == '__main__':
    logging.basicConfig(filename='app.log', level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s: %(message)s')
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
    console_handler.setFormatter(console_formatter)
    
    logging.getLogger('').addHandler(console_handler)
    app.run(host='0.0.0.0', port=5000)
