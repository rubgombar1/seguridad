import socket
import uuid
from functions import calculate_mac, create_diffieHellman, encode_AES, decode_AES
from datetime import datetime

DH = create_diffieHellman()
print 'tarda'
s = socket.socket()
port = 6032
s.connect(("localhost", port))
s.send(str(DH.publicKey).encode())
server_public_key = int(s.recv(2048))
DH.generateKey(server_public_key)
print len(DH.getKey()[:len(DH.getKey())/2])
message = raw_input('Introduzca su mensaje: ')
hash_name = raw_input('Introduzca la funcion resumen a utilizar(SHA256, SHA384 o SHA512): ')
message_cipher, count = encode_AES(message, DH.getKey()[:len(DH.getKey())/2])
#mes = decode_AES(message_cipher, DH.getKey()[:len(DH.getKey())/2], count)
message_cipher = message_cipher.encode()
date = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
uid = uuid.uuid1()
key = open('key-client.txt', 'r')
key = key.read().encode()
nonce = (str(date) + '/' + str(uid)).encode()
mac_of_message = calculate_mac(message+nonce, key, hash_name)
print(str(message_cipher.decode()) + '|' + str(mac_of_message) + '|' + nonce.decode())
request = str(message_cipher.decode()) + '|' + str(mac_of_message) + '|' + nonce.decode() + '|' + hash_name + '|' + str(count)
s.send(request.encode())
res = s.recv(1024)
print(res.decode())
s.close