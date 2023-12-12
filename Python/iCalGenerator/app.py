from flask import Flask, render_template, request, Response
from icalendar import Calendar, Event
from datetime import datetime
import re
from unidecode import unidecode
import json


app = Flask(__name__)


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        event_data = {
            'summary': request.form['summary'] if 'summary' in request.form else '',
            'location': request.form['location'] if 'location' in request.form else '',
            'description': request.form['description'] if 'description' in request.form else '',
            'start_datetime': request.form['start_datetime'] if 'start_datetime' in request.form else '',
            'end_datetime': request.form['end_datetime'] if 'end_datetime' in request.form else '',
            'is_meeting': 'Yes' if 'is_meeting' in request.form else 'No',
            'meeting_url': request.form['meeting_url'] if 'meeting_url' in request.form else ''
        }

        image = request.files['image'] if 'image' in request.files else None
        if image and allowed_file(image.filename):
            image_path = f"uploads/{image.filename}"
            image.save(image_path)
            event_data['image'] = image_path
        try:
            ical_data = generate_ical(event_data)
            filename = f"{unidecode(event_data['summary'])}.ics"
            filename = re.sub(r'[\/:*?"<>|]', '_', filename)
            response = Response(ical_data, mimetype='text/calendar; charset=utf-8')
            response.headers['Content-Disposition'] = f'attachment; filename="{filename}"'
            return response
        else:
            err = {'Error': 'Invalid request format!'}
            return json.dumps(err), 400, {'content-type': 'application/json'}

    return render_template('index.html')


def generate_ical(event_data):
    cal = Calendar()
    
    event = Event()
    event.add('summary', event_data['summary'])
    event.add('location', event_data['location'])
    event.add('description', event_data['description'])
    if event_data['start_datetime']:
        start_datetime = datetime.strptime(event_data['start_datetime'], '%Y-%m-%dT%H:%M')
        event.add('dtstart', start_datetime)
    if event_data['end_datetime']:
        end_datetime = datetime.strptime(event_data['end_datetime'], '%Y-%m-%dT%H:%M')
        event.add('dtend', end_datetime)
    
    if event_data.get('is_meeting'):
        event.add('url', event_data.get('meeting_url'))
    
    cal.add_component(event)
    
    return cal.to_ical()

if __name__ == '__main__':
    app.run()
