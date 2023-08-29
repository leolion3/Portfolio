from flask import Flask, render_template, request, Response
from icalendar import Calendar, Event
from datetime import datetime
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        event_data = {
            'summary': request.form['summary'],
            'location': request.form['location'],
            'description': request.form['description'],
            'start_datetime': request.form['start_datetime'],
            'end_datetime': request.form['end_datetime'],
            'is_meeting': 'Yes' if 'is_meeting' in request.form else 'No',
            'meeting_url': request.form['meeting_url']
        }

        image = request.files['image']
        if image:
            image_path = f"uploads/{image.filename}"
            image.save(image_path)
            event_data['image'] = image_path

        ical_data = generate_ical(event_data)
        filename = f"{event_data['summary']}.ics"
        filename = re.sub(r'[\/:*?"<>|]', '_', filename)
        response = Response(ical_data, mimetype='text/calendar')
        response.headers['Content-Disposition'] = f'attachment; filename="{filename}"'
        return response

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
