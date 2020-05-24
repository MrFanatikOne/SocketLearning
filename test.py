import socket
import json

reg = {
    'name': 'Danya',
    'password': 'JoJo',
    'fun': 'reg'
    }
log = {
    'name': 'Danya',
    'password': 'JoJo',
    'fun': 'log'
    }
close = {
    'name': 'Maxim',
    'password': 'Pass',
    'fun': 'close'
    }

data_json = json.dumps(log)  # data serialized

sock = socket.socket()
sock.connect(('localhost', 9090))

sock.send(data_json.encode())

data = sock.recv(1024)
sock.close()

print(data)