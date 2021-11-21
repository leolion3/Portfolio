import socket

addr = input('Please enter address: ')
prt = int(input('Please enter port: '))
s = socket.socket()
s.connect((addr,prt))
s.close()
print("Connection successful!")
