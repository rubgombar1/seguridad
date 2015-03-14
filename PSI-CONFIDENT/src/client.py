import socket
import uuid
from functions import calculate_mac
from datetime import datetime

s = socket.socket()
port = 6032
s.connect(("localhost", port))
message = raw_input('Introduzca su mensaje: ')
hash_name = raw_input('Introduzca la funcion resumen a utilizar(SHA256, SHA384 o SHA512): ')
message = message.encode()
date = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
uid = uuid.uuid1()
key = open('key-client.txt', 'r')
key = key.read().encode()
nonce = (str(date) + '/' + str(uid)).encode()
mac_of_message = calculate_mac(message+nonce, key, hash_name)
print(str(message.decode()) + '|' + str(mac_of_message) + '|' + nonce.decode())
request = str(message.decode()) + '|' + str(mac_of_message) + '|' + nonce.decode() + '|' + hash_name
s.send(request.encode())
res = s.recv(1024)
print(res.decode())
s.close