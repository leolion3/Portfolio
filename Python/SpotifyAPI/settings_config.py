import json


cached_dict = None
API_KEY = None


def read_settings():
	global cached_dict
	if not cached_dict:
		FILENAME = 'config.json'
		with open(FILENAME, 'r') as f:
			cached_dict = json.loads(f.read())
	return cached_dict


def get_headers():
	global API_KEY
	HEADERS = {
		"Accept" : "application/json",
		"Content-Type" : "application/json",
		"Authorization": "Bearer " + API_KEY
#		'Content-Length': '0',
#		'scope' : 'playlist-modify-private'
	}


read_settings()
API_KEY = cached_dict['API_KEY']