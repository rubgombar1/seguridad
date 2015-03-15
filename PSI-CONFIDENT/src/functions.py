import base64
import hashlib
import hmac
import random
import string
from datetime import datetime, timedelta
from Crypto.Cipher import AES
import sys
from test_DH import DiffieHellman


def key_generator(size=7, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def encrypt_message():
    key = key_generator()
    iv = random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    msg = iv + cipher.encrypt(b'Attack at dawn')
    print(msg)


def get_function(hash_name):
    hash_name = hash_name.upper()
    if hash_name == 'SHA256':
        func_hash = hashlib.sha256
        return func_hash
    elif hash_name == 'SHA384':
        func_hash = hashlib.sha384
        return func_hash
    elif hash_name == 'SHA512':
        func_hash = hashlib.sha512
        return func_hash
    else:
        print('La funcion introducida no es correcta, prueba de nuevo')
        sys.exit(0)


def calculate_mac(message, key, hash_name):
    hash_function = get_function(hash_name)
    func = hmac.new(key, message, hash_function)
    hash_result = func.hexdigest()
    return hash_result


def recieved_request(request):
    response = request.split('|')
    message = response[0]
    mac = response[1]
    nonce = response[2]
    hash_name = response[3]
    return message, mac, nonce, hash_name


def check_integrity(message, nonce, mac, key, hash_name):
    res = False
    message_nonce = (message+nonce).encode()
    hash_result = calculate_mac(message_nonce, key, hash_name)
    if mac == hash_result:
        res = True
    else:
        log = open('log.txt', 'a')
        log.write(message + '\n')
    return res


def clean_db_nonces():
    res = ''
    db_nonces_r = open('db_nonces.txt', 'r')
    nonces = db_nonces_r.read()
    db_nonces_r.close()
    nonces_aux = nonces.split('\n')
    nonces = nonces_aux[1 : len(nonces_aux)]
    db_nonces_w = open('db_nonces.txt', 'w')
    for nonce in nonces:
        nonce_aux = nonce.split('/')
        date = nonce_aux[0]
        today_date = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        today = datetime.strptime(today_date, '%Y-%m-%d %H:%M:%S')
        date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        if today - date < timedelta(minutes=1):
            res += '\n' + nonce
    db_nonces_w.write(res)

def check_replay(nonce):
    res = False
    aux = nonce.split('/')
    date, uid = aux[0], aux[1]
    today_date = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    today = datetime.strptime(today_date, '%Y-%m-%d %H:%M:%S')
    date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    if today - date < timedelta(minutes=1):
        db_nonces_r = open('db_nonces.txt', 'r')
        nonces = db_nonces_r.read()
        db_nonces_r.close()
        nonces_aux = nonces.split('\n')
        if not nonces_aux.__contains__(nonce):
            nonces += '\n' + nonce
            db_nonces_w = open('db_nonces.txt', 'w')
            db_nonces_w.write(nonces)
            db_nonces_w.close()
            res = True
    clean_db_nonces()
    return res

def create_diffieHellman():
    DH = DiffieHellman()
    return DH

def encode_AES(message, secret):
    BLOCK_SIZE = 32
    PADDING = 'skd'
    pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
    EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
    cipher = AES.new(secret)
    while message.__len__()%16!=0:
        message += ' '
    return EncodeAES(cipher, message)