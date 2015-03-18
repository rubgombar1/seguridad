import random
import string
from Crypto.Cipher import DES3
from Crypto import Random
import datetime
from Crypto.Hash import MD5
import sys


def key_generator(size=7, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def execute_3des(plaintext):
    key = key_generator(16)
    iv = Random.get_random_bytes(8)
    des1 = DES3.new(key, DES3.MODE_CFB, iv)
    des2 = DES3.new(key, DES3.MODE_CFB, iv)
    date1 =  datetime.datetime.now()
    hash_plaintex = MD5.new(plaintext).digest()
    cipher_text = des1.encrypt(plaintext)
    date2 = datetime.datetime.now()
    print 'Tiempo de cifrado'+ str(date2-date1)
    date3 = datetime.datetime.now()
    decrypt_message = des2.decrypt(cipher_text)
    print sys.getsizeof(cipher_text)
    date4 = datetime.datetime.now()
    if hash_plaintex != MD5.new(decrypt_message).digest():
        print 'El mensaje no se ha descifrado'
    else:
        print 'Tiempo de descifrado'+ str(date4-date3)
        return date2-date1, date4-date3