import socket
from googletrans import Translator

translator = Translator()
server_lan = "en"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5555))
server.listen()
print("server start")

while True:
    client, address = server.accept()
    # print(connection, address)
    try:
        data = client.recv(1024).decode()
        source_lan_type = data[1:data.index("]")]
        source_lan = data[data.index("]")+1:]
        print(source_lan_type)
        print(source_lan)
        translation = translator.translate(source_lan,
                                           src=source_lan_type,
                                           dest=server_lan)
        print(translation.text)
    except ConnectionError as error:
        print('connection error')
        break
