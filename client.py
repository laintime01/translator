# This is client part for translator
import socket

# AF_INET ->ipv4, SOCK_STREAM ->TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5555))
lang = input('plz input your language: ')
while True:
    try:
        msg = input("")
        if msg == 'q':
            client.close()
        else:
            client.send(f"[{lang}]{msg}".encode())
    except ConnectionError as e:
        print('connection error')
        break
