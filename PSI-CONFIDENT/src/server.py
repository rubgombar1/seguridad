import socket
from functions import recieved_request, check_integrity, check_replay

server_socket = socket.socket()
server_socket.bind(("localhost",  6032))
server_socket.listen(5)
while True:
    c, addr = server_socket.accept()
    request = c.recv(1024)
    message, mac, nonce, hash_name = recieved_request(request.decode())
    if check_replay(nonce):
        key = open('key-server.txt', 'r')
        key = key.read().encode()
        integrity = check_integrity(message, nonce, mac, key, hash_name)
        if integrity:
            print('El mensaje (' + message + ') ha llegado libre de ataque replay y se ha conservado su integridad')
            a = ('El mensaje ha llegado libre de ataque de replay e integro').encode()
            c.send(a)
        if not integrity:
            print('El mensaje (' + message + ') ha llegado libre de ataque replay pero no se ha conservado su integridad')
            a = ('El mensaje ha llegado libre de ataque de replay pero no ha llegado integro').encode()
            c.send(a)
    else:
        print('El mensaje (' + message + ') puede haber sufrido un ataque de replay')
        a = ('Es posible que el mensaje sea objeto de ataque de replay').encode()
        c.send(a)
c.close