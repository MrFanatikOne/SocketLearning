import json
import socket
import DB


DB.create_table()
sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
print(DB.read_db())

# print(DB_new.read_db())
while True:
    conn, addr = sock.accept()
    print('connected:', addr)
    data = conn.recv(1024).decode()
    if data:
        json_data = json.loads(data)
        print(data)

        if json_data.get('fun') == 'reg':
            msg = DB.write_new_user(json_data)
            conn.send(msg)

        if json_data.get('fun') == 'log':
            msg = DB.login(json_data)
            conn.send(msg)

        if json_data.get('fun') == 'close':
            msg = b'Close connection'
            conn.send(msg)
            break
        conn.close()



