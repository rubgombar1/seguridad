import random
import string
import datetime
import sys
from Crypto.Hash import MD5

__author__ = 'usuario'

from Crypto.Cipher import Blowfish


def pad_string(str):
    INPUT_SIZE = 8
    new_str = str
    pad_chars = INPUT_SIZE - (len(str) % INPUT_SIZE)

    if pad_chars != 0:
        for x in range(pad_chars):
            new_str += " "

    return new_str

def key_generator(size=7, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def execute_blowfish(plaintext):
    crypt_obj = Blowfish.new(key_generator(16), Blowfish.MODE_ECB)
    hash_plaintex = MD5.new(plaintext).digest()
    date1 =  datetime.datetime.now()
    ciphertext = crypt_obj.encrypt(pad_string(plaintext))
    date2 =  datetime.datetime.now()
    print 'Tiempo de cifrado'+ str(date2-date1)
    print sys.getsizeof(ciphertext)
    date3 =  datetime.datetime.now()
    decrypt_text = crypt_obj.decrypt(ciphertext)
    date4 =  datetime.datetime.now()
    if hash_plaintex != MD5.new(decrypt_text.strip()).digest():
        print 'El mensaje no se ha descifrado'
    else:
        print sys.getsizeof(decrypt_text.strip())
        print 'Tiempo de descifrado'+ str(date4-date3)
        return date2-date1, date4-date3
