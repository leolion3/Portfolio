import base64
import json
import hashlib
import logging
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
API_URL = 'http://localhost:5000/pixel/'
email_dict = {}

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
        return f"{API_URL}{pixel_hash}"

@app.route('/', methods=['GET'])
def render_form():
    return render_template('index.html')

@app.route('/generate_pixel', methods=['POST'])
def generate_pixel():
    data = request.json
    email = data.get('email')
    subject = data.get('subject')
    
    if not email or not subject:
        return jsonify(error="Email and subject are required."), 400

    tracking_pixel = generate_tracking_pixel(email, subject)
    return jsonify(tracking_pixel=tracking_pixel)

@app.route('/pixel/<pixel_hash>', methods=['GET'])
def track_pixel(pixel_hash):
    global email_dict
    if pixel_hash not in email_dict:
        return "", 403
    logging.info(f"Email opened: {json.dumps(email_dict[pixel_hash])}")
    return "", 200 

if __name__ == '__main__':
    logging.basicConfig(filename='app.log', level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s: %(message)s')
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
    console_handler.setFormatter(console_formatter)
    
    logging.getLogger('').addHandler(console_handler)
    app.run(host='0.0.0.0', port=5000)