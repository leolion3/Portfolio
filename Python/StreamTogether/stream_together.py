#!/usr/bin/env python3
import pyautogui
import keyboard
import socket
import sys
import threading
import uuid
from time import sleep


MAX_CLIENTS = 1
PORT = 9001

if len(sys.argv) < 3:
	print(f'Usage: {sys.argv[0]} [client/server] [server_ip]')
	exit()

IP_ADDRESS = sys.argv[2]

if len(sys.argv) > 3:
	try:
		PORT = int(sys.argv[3])
	except:
		# ignored
		pass

mode = sys.argv[1]

if 's' in mode:
	mode = 1
else:
	mode = 0


class client:

	def get_data(self):
		data = ''
		while not '\n' in data:
			data += self.s.recv(1).decode()
		return data.strip()

	def get_uuid(self, data):
		if ':' in data:
			return data.split(':')[1]
		return ''

	def get_key(self, data):
		if ':' in data:
			return data.split(':')[0]
		return data

	def exec_allowed(self, uuid):
		if uuid == self.previous_uuid or self.lock:
			return False
		self.previous_uuid = uuid
		self.lock = True
		return True

	def receiver_thread(self):
		while self.active:
			data = self.get_data()
			key = self.get_key(data)
			uuid = self.get_uuid(data)
			if not self.exec_allowed(uuid):
				continue

			keys = ['space', 'f', 'esc', 'ctrl+up', 'ctrl+down', 'ctrl+left', 'ctrl+right', 'shift+left', 'shift+right', 'alt+left', 'alt+right', 'left', 'right', 'up', 'down']
			if key in keys:
				if '+' in key:
					pyautogui.hotkey(key.split('+'))
				else:
					pyautogui.press(key)
			sleep(1)
			self.lock = False

	def on_key_press(self, event):
		if self.lock:
			return
		self.lock = True
		payload = bytes(f'{keyboard.read_event(suppress=True).name}:{str(uuid.uuid4())}\n', 'utf-8')
		self.s.send(payload)
		self.lock = False

	def keyboard_listener(self):
		keyboard.on_press_key('space', self.on_key_press)
		keyboard.read_event(suppress=True)
		keyboard.wait()

	def __init__(self, ip_addr, port):
		self.previous_uuid = ''
		self.lock = False
		self.s = socket.socket()
		self.s.connect((ip_addr, port))
		self.active = True
		t2 = threading.Thread(target=self.receiver_thread)
		t2.start()
		self.keyboard_listener()


class server:

	def propagate(self, data, addr, port):
		print(f'[::] <-- Received {data} from {addr}:{port}...')
		new_clients = []
		for client, address, port, name in self.clients:
			if addr == address:
				new_clients.append((client, address, port, name))
				continue
			try:
				client.send(bytes(f'{data}\n', 'utf-8'))
				new_clients.append((client, address, port, name))
				print(f'[::] --> Sent {data} to {name} {address}:{port}!')
			except:
				print(f'[::] -x-> Attempted to send {data} to {name} {address}:{port} but was unsuccessful!')
		self.clients = new_clients

	def __receive_data(self, client):
		data = ''
		while not '\n' in data:
			data += client.recv(1).decode()
		return data.strip()


	def client_handler(self, client, addr, port):
		while True:
			try:
				data = self.__receive_data(client)
				self.propagate(data, addr, port)
			except:
				print(f'[::] <-x- Failed to receive data from client {addr}:{port}. Terminating thread...')
				break

	def __setup_server(self, ip_addr, port, max_clients):
		s = socket.socket()
		s.bind((ip_addr, port))
		# +1 since we are the first client
		s.listen(max_clients + 1)
		print(f'[INFO] Started listener, awaiting {max_clients + 1} clients...')
		return s

	def __connect_server_client(self, s):
		srv_client, srv_addr = s.accept()
		threading.Thread(target=self.client_handler, args=(srv_client, srv_addr[0], srv_addr[1])).start()
		self.clients = [(srv_client, srv_addr[0], srv_addr[1], '[SERVER]')]
		print('[::] <-- Connected server client.')

	def __run_server(self, s):
		while True:
			client, addr = s.accept()
			print(f'[::] <-- Accepted a new connection from {addr[0]}:{addr[1]}')
			t = threading.Thread(target=self.client_handler, args=(client, addr[0], addr[1]))
			self.clients.append((client, addr[0], addr[1], '[REMOTE]'))
			t.start()

	def __init__(self, ip_addr, port, max_clients):
		s = self.__setup_server(ip_addr, port, max_clients)
		self.__connect_server_client(s)
		self.__run_server(s)


def server_thread():
	server(IP_ADDRESS, PORT, MAX_CLIENTS)


def client_thread():
	client(IP_ADDRESS, PORT)


if __name__ == '__main__':
	if mode == 1:
		srv_thread = threading.Thread(target=server_thread)
		c_thread = threading.Thread(target=client_thread)
		srv_thread.start()
		c_thread.start()
		srv_thread.join()
		c_thread.join()	
	else:
		client(IP_ADDRESS, PORT)