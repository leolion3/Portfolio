#!/usr/bin/env python3
from authenticate import StudIPAuthenticator
from getpass import getpass
from urllib.parse import unquote
import requests


def url_decode(data):
	decoded = {
		'&quot;': '"',
		'&amp;': '&',
		'\\/': '/',
		'&gt;': '>',
		'&lt;': '<',
		'\\n': '\n',
		'\\"': '"'
	}
	for key, val in decoded.items():
		data = data.replace(key, val)
	return data


def get_folders(data):
	links = data.split('"url":"')
	resp = []
	for link in links:
		link = link.split('"')[0]
		if '/course/files/index/' in link:
			resp.append(link)
	return resp


def get_files(data, file_types):
	links = data.split('"download_url":"')
	resp = []
	for link in links:
		link = link.split('"')[0]
		for ftype in file_types:
			if link.strip().lower().endswith(ftype):
				resp.append(link)
	return resp


def enumerate_subdir(session, url, files, file_types):
	splitter = 'data-folders="'
	html = session.get(url).text
	files.extend(get_files(url_decode(html), file_types))
	html = html.split(splitter)[1].split('"')[0]
	html = url_decode(html)
	return get_folders(html)


def enumerate_root(session, cid, files, file_types):
	URL = f'https://elearning.uni-bremen.de/dispatch.php/course/files?cid={cid}'
	return enumerate_subdir(session, URL, files, file_types)


def flatten_directory(session, url, files, file_types):
	subdirs = enumerate_subdir(session, url, files, file_types)
	flattened = [url]
	for directory in subdirs:
		flattened.extend(flatten_directory(session, directory, files, file_types))
	return flattened


def enumerate_from_root(session, file_types=['pdf']):
	files = []
	initial_folders = enumerate_root(session, cid, files, file_types)
	directories = []
	for folder in initial_folders:
		directories.extend(flatten_directory(session, folder, files, file_types))
	return files


def download_files(session, file_types=['pdf']):
	files = enumerate_from_root(session, file_types)
	header = '&force_download=1'
	for file in files:
		r = session.get(f'{file}{header}')
		try:
			filename = file.split('file_name=')[1].split('&')[0]
			with open(filename, "wb") as f:
				f.write(r.content)
			if r.status_code != 200:
				print(f'Error downloading file {filename}\n{r.text}')
			else:
				print(f'File {filename} downloaded.')
		except Exception as e:
			raise Exception('Error writing to file. Trace:', e)


if __name__ == '__main__':
	username = input('Username: ')
	password = getpass('Password: ')
	cid = input('Course ID (cid in URL): ')
	rest_api = StudIPAuthenticator()
	session = rest_api.authenticate(username, password)
	download_files(session)