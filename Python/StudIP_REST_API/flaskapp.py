#!/usr/bin/env python3
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, render_template, request
from authenticate import StudIPAuthenticator

HOST = '0.0.0.0'
PORT = 5050
app = Flask('StudIP REST API')

rest_api = StudIPAuthenticator()

# Create a new scheduler instance
scheduler = BackgroundScheduler()
scheduler.start()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieve the input data from the HTML form
        username = request.form['username']
        password = request.form['password']
        uid = request.form['uid']
        datetime_str = request.form['datetime']
        datetime_obj = datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M')

        # Schedule the job to run at the specified time
        scheduler.add_job(func=schedule_job, args=(username, password, uid), trigger='date', run_date=datetime_obj)

        # Render a success message
        message = datetime_obj.strftime('%Y-%m-%d %H:%M:%S')
        return render_template('index.html', message=message)
    
    # Render the initial HTML form
    return render_template('index.html')

def schedule_job(username, password, uid):
    session = rest_api.authenticate(username, password)
    return_code = rest_api.apply_for_course(session, uid)
    print(f'Job ran at {datetime.now()} with username {username}, and uid {uid} with status code {return_code}')


app.run(HOST, PORT)