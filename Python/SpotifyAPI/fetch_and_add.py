import requests
import json
from settings_config import read_settings, get_headers


BASE_URL = "https://api.spotify.com/v1/playlists/"


def fetch_playlist_songs(fetch_playlist_url : str) -> (int, [str]):
	global API_KEY
	data = requests.get(fetch_playlist_url, headers=get_headers())
	if data.status_code / 100 != 2:
		print(f'Error fetching songs! Response code: {data.status_code}')
		return (data.status_code, [])
	songs = []
	for x in json.loads(data.text)['items']:
		songs.append((x['track'])['uri'])
	return (data.status_code, songs)


def duplicate_playlist(other_playlist, new_playlist_url) -> bool:
	global API_KEY
	songs_string = ''
	for x in other_playlist[::-1]:
		songs_string += x + ','
	payload = songs_string[:-1]
	data = requests.post(new_playlist_url + payload + "&position=0", headers=get_headers())
	response = data.status_code / 100 == 2
	if not response:
		print(f'Error adding songs to playlist! Response code: {data.status_code}')
	return response


def copy_playlist():
	global BASE_URL
	old_playlist_id = input("Input old playlist id: ")
	fetch_playlist_url = BASE_URL + old_playlist_id + "/tracks"

	new_playlist_id = input("Input new playlist id: ")
	new_playlist_url = BASE_URL + new_playlist_id + "/tracks?uris="
	old_playlist_exec = fetch_playlist_songs(fetch_playlist_url) 
	duplicate_playlist(old_playlist_exec[1], new_playlist_url)


copy_playlist()