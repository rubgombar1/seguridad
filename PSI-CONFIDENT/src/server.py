import socket
from functions import recieved_request, check_integrity, check_replay, create_diffieHellman, decode_AES

server_socket = socket.socket()
server_socket.bind(("localhost",  6032))
server_socket.listen(5)
while True:
    c, addr = server_socket.accept()
    client_public_key = int(c.recv(2048))
    DH = create_diffieHellman()
    c.send(str(DH.publicKey).encode())
    DH.generateKey(client_public_key)
    print DH.getKey()
    request = c.recv(1024)
    message_cipher, mac, nonce, hash_name, count = recieved_request(request.decode())
    message = decode_AES(message_cipher, DH.getKey()[:len(DH.getKey())/2], count)
    print message
    if check_replay(nonce):
        key = open('key-server.txt', 'r')
        key = key.read().encode()
        integrity = check_integrity(message, nonce, mac, key, hash_name)
        if integrity:
            print('El mensaje (' + message_cipher + ') ha llegado libre de ataque de replay, se ha podido descifrar e integro')
            a = ('El mensaje ha llegado libre de ataque de replay, se ha podido descifrar e integro').encode()
            c.send(a)
        if not integrity:
            print('El mensaje (' + message_cipher + ') ha llegado libre de ataque de replay pero no ha llegado integro o no se ha podido descifrar correctamente')
            a = ('El mensaje ha llegado libre de ataque de replay pero no ha llegado integro o no se ha podido descifrar correctamente').encode()
            c.send(a)
    else:
        print('El mensaje (' + message_cipher + ') puede haber sufrido un ataque de replay')
        a = ('Es posible que el mensaje sea objeto de ataque de replay').encode()
        c.send(a)
c.close