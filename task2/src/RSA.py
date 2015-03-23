from Crypto.Hash import MD5
import datetime
import sys

__author__ = 'usuario'
from Crypto.PublicKey import RSA
from Crypto import Random
def execute_RSA(plaintext):
    KEY_LENGTH = 1024  # Key size (in bits)
    random_gen = Random.new().read

    keypair_snowden = RSA.generate(KEY_LENGTH, random_gen)
    pubkey_snowden  = keypair_snowden.publickey()
    hash_plaintex = MD5.new(plaintext).digest()
    date1 =  datetime.datetime.now()
    encrypted_for_snowden   = pubkey_snowden.encrypt(plaintext, 111)
    date2 =  datetime.datetime.now()
    print sys.getsizeof(encrypted_for_snowden)
    date3 =  datetime.datetime.now()
    decrypted_snowden   = keypair_snowden.decrypt(encrypted_for_snowden)
    date4 =  datetime.datetime.now()
    if hash_plaintex != MD5.new(decrypted_snowden.strip()).digest():
        print 'El mensaje no se ha descifrado'
    else:
        print sys.getsizeof(decrypted_snowden.strip())
        print 'Tiempo de descifrado'+ str(date4-date3)
        return date2-date1, date4-date3