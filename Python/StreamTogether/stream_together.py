#!/usr/bin/env python3
from typing import List

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
    print(f'Usage: {sys.argv[0]} [[c]lient/[s]erver] [Server IP] <Port>')
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


class Client:
    """
    Saves client state and handles data exchanges.
    """

    def get_data(self) -> str:
        """
        Receives data from the socket until a newline is returned.
        :return: the received data string.
        """
        data = ''
        while '\n' not in data:
            data += self.s.recv(1).decode()
        return data.strip()

    @staticmethod
    def get_uuid(data: str) -> str:
        """
        Extracts the message UID from a received message.
        :param data: the received data string.
        :return: the message UID.
        """
        if ':' in data:
            return data.split(':')[1]
        return ''

    @staticmethod
    def get_key(data: str) -> str:
        """
        Gets the key that was propagated by the server.
        :param data: the received data string.
        :return: the pressed key.
        """
        if ':' in data:
            return data.split(':')[0]
        return data

    def exec_allowed(self, message_uuid: str) -> bool:
        """
        Checks whether the key should be pressed based on the uid.
        :param message_uuid: the message uid.
        :return: True if the key should be pressed, false otherwise.
        """
        if message_uuid == self.previous_uuid or self.lock:
            return False
        self.previous_uuid = message_uuid
        self.lock = True
        return True

    def recv_and_exec(self, keys: List[str]) -> None:
        """
        Receives a message from the server and executes the matching key combination.
        :param keys: available key combinations.
        :return:
        """
        data: str = self.get_data()
        key: str = self.get_key(data)
        message_uuid: str = self.get_uuid(data)
        if not self.exec_allowed(message_uuid):
            return

        if key in keys:
            if '+' in key:
                pyautogui.hotkey(key.split('+'))
            else:
                pyautogui.press(key)
        sleep(1)
        self.lock = False

    def receiver_thread(self) -> None:
        """
        Handles receiving data for the client.
        :return:
        """
        keys = ['space', 'f', 'esc', 'ctrl+up', 'ctrl+down', 'ctrl+left', 'ctrl+right', 'shift+left', 'shift+right',
                'alt+left', 'alt+right', 'left', 'right', 'up', 'down']
        while self.active:
            try:
                self.recv_and_exec(keys)
            except Exception as e:
                print(f'[Receiver Thread] Exception raised and caught, trace: {e}')

    def on_key_press(self, event):
        """
        Propagates pressed key to server for broadcast.
        :param event: keyboard event action listener.
        :return:
        """
        if self.lock:
            return
        self.lock = True
        # Broadcast
        payload = bytes(f'{keyboard.read_event(suppress=True).name}:{str(uuid.uuid4())}\n', 'utf-8')
        self.s.send(payload)
        self.lock = False

    def keyboard_listener(self) -> None:
        """
        Listens for key presses.
        :return:
        """
        keyboard.on_press_key('space', self.on_key_press)
        keyboard.read_event(suppress=True)
        keyboard.wait()

    def __init__(self, ip_addr, port):
        """
        Client init.
        :param ip_addr: server ip.
        :param port: server port to connect to.
        """
        self.previous_uuid = ''
        self.lock = False
        self.s = socket.socket()
        self.s.connect((ip_addr, port))
        self.active = True
        t2 = threading.Thread(target=self.receiver_thread)
        t2.start()
        self.keyboard_listener()


class Server:
    """
    Handles server operations for propagating key presses.
    """

    def propagate(self, data: str, addr: str, s_port: int) -> None:
        """
        Propagate pressed key to other clients.
        :param data: payload keypress from client.
        :param addr: IP address of client that sent the message.
        :param s_port: source client port.
        :return:
        """
        print(f'[::] <-- Received {data} from {addr}:{s_port}...')
        new_clients = []
        for client, address, port, name in self.clients:
            try:
                # Propagate message to other clients.
                # To not cause an endless keypress loop, never propagate to localhost.
                if addr != address:
                    client.send(bytes(f'{data}\n', 'utf-8'))
                    print(f'[::] --> Sent {data} to {name} {address}:{port}!')
                new_clients.append((client, address, port, name))
            except Exception as ignored:
                print(f'[::] -x-> Attempted to send {data} to {name} {address}:{port} but was unsuccessful!')
        self.clients.clear()
        [self.clients.append(c) for c in new_clients]

    @staticmethod
    def __receive_data(client: socket.socket) -> str:
        """
        Receives data from a client.
        :param client: the client to receive data from.
        :return: the received data string.
        """
        data = ''
        while not '\n' in data:
            data += client.recv(1).decode()
        return data.strip()

    def client_handler(self, client: socket.socket, addr: str, port: int) -> None:
        """
        Handles client connections.
        :param client: the client to handle.
        :param addr: the client's address.
        :param port: the client's port.
        :return:
        """
        while True:
            try:
                data: str = self.__receive_data(client)
                self.propagate(data, addr, port)
            except Exception as ignored:
                print(f'[::] <-x- Failed to receive data from client {addr}:{port}. Terminating thread...')
                break

    @staticmethod
    def __setup_server(ip_addr, port, max_clients) -> socket.socket:
        """
        Server setup.
        :param ip_addr: ip address to bind.
        :param port: port to bind.
        :param max_clients: max clients allowed.
        :return:
        """
        s = socket.socket()
        s.bind((ip_addr, port))
        # +1 since we are the first client
        s.listen(max_clients + 1)
        print(f'[INFO] Started listener, awaiting {max_clients + 1} clients...')
        return s

    def __connect_server_client(self, s: socket.socket) -> None:
        """
        Creates a client for the server and connects it.
        :param s: the server socket.
        :return:
        """
        srv_client, srv_addr = s.accept()
        threading.Thread(target=self.client_handler, args=(srv_client, srv_addr[0], srv_addr[1])).start()
        self.clients = [(srv_client, srv_addr[0], srv_addr[1], '[SERVER]')]
        print('[::] <-- Connected server client.')

    def __run_server(self, s: socket.socket):
        """
        Server loop, handles client threads.
        :param s: server socket.
        :return:
        """
        while True:
            try:
                client, addr = s.accept()
                print(f'[::] <-- Accepted a new connection from {addr[0]}:{addr[1]}')
                t = threading.Thread(target=self.client_handler, args=(client, addr[0], addr[1]))
                self.clients.append((client, addr[0], addr[1], '[REMOTE]'))
                t.start()
                t.join()
            except Exception as e:
                print('Error occurred while handling client. Trace:', e)

    def __init__(self, ip_addr, port, max_clients):
        """
        Server init.
        :param ip_addr: server bind address.
        :param port: server bind port.
        :param max_clients: max allowed clients.
        """
        s = self.__setup_server(ip_addr, port, max_clients)
        self.__connect_server_client(s)
        self.__run_server(s)


def server_thread():
    Server(IP_ADDRESS, PORT, MAX_CLIENTS)


def client_thread():
    Client(IP_ADDRESS, PORT)


if __name__ == '__main__':
    if mode == 1:
        srv_thread = threading.Thread(target=server_thread)
        c_thread = threading.Thread(target=client_thread)
        srv_thread.start()
        c_thread.start()
        srv_thread.join()
        c_thread.join()
    else:
        Client(IP_ADDRESS, PORT)
