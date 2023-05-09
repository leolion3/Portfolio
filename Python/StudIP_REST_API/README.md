# StudIP REST API

Since StudIP comes with a REST API which is disabled by default, this REST API is used to perform various actions on StudIP using simple HTTP requests.

So far the only feature that has been implemented is an automated course sign up on a given time and date.

## Requirements

This app requires the libraries:

- Flask - for running the REST API
- requests - for performing HTTP Requests
- APScheduler - for task scheduling

To run the app simply execute `python3 ./flaskapp.py`