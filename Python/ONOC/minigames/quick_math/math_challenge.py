#!/usr/bin/env python3
import socket
import threading
import random


def log(msg):
	print(msg)


def send(s, addr, msg):
	s.send(bytes(f'{msg}\n', 'utf-8'))
	log(f'[<--] Sent {msg} to {addr[0]}:{addr[1]}')


def recv(s, addr):
	r = s.recv(4096).decode().strip()
	log(f'[-->] Client {addr[0]}:{addr[1]} sent data: \"{r}\"')
	return r


def plus_minus(s, addr):
	for i in range(2500):
		a, b = random.randint(1, 1000000), random.randint(1, 1000000)
		r = random.choice([0, 1])
		if r == 0:
			eq = f'{a}+{b}='
		else:
			eq = f'{a}-{b}='
		send(s, addr, eq)
		try:
			r = recv(s, addr)
		except:
			send(s, addr, 'Too slow!')
			return False
		if r != str(eval(eq[:-1])):
			send(s, addr, 'Try again!')
			return False
	return True


def div_mult(s, addr):
	for i in range(2500):
		a, b = random.randint(100000, 1000000), random.randint(1, 10000)
		r = random.choice([0, 1])
		if r == 0:
			eq = f'{a}/{b}='
		else:
			eq = f'{a}*{b}='
		send(s, addr, eq)
		try:
			r = recv(s, addr)
		except:
			send(s, addr, 'Too slow!')
			return False
		acc = int(round(eval(eq[:-1]), 0))
		if r != str(acc):
			send(s, addr, 'Try again!')
			return False
	return True



def client_handler(s, addr):
	log(f'[::] Client connected from {addr[0]}:{addr[1]}.')
	m = plus_minus(s, addr)
	if not m:
		s.close()
		return
	c = div_mult(s, addr)
	if not c:
		s.close()
		return
	send(s, addr, """flag{N0T_P0ST3D_0N_G17HUB}""")



def start_server():
	try:
		server = socket.socket()
		server.bind(('0.0.0.0', 80))
		server.listen()
		print('Server listening on [::]...')
		while True:
			# Exception handling for connection fails
			try:
				s, addr = server.accept()
				s.settimeout(0.5)
				s.send(b'Please respect the game and dont attempt attacking this server.\nALL TRAFFIC IS LOGGED ALONG WITH SOURCE IPs!\nNote: You can round answers!\n')
				t = threading.Thread(target=client_handler, args=(s,addr))
				t.start()
				t.join()
			except:
				#ignored
				continue
	finally:
		server.close()


if __name__ == '__main__':
	start_server()
