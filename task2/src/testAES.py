import random
import string
import datetime
from Crypto.Hash import MD5
import sys
from src.aes import AESCipher

__author__ = 'usuario'

def key_generator(size=7, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def aes10KB():
    file = open('file10KB.txt', 'r')
    file = file.read()
    aes = AESCipher(key_generator(16))
    hash_plaintex = MD5.new(file).digest()
    date1 =  datetime.datetime.now()
    message_encrypt = aes.encrypt(file)
    date2 =  datetime.datetime.now()
    print 'Tiempo de cifrado'+ str(date2-date1)
    print sys.getsizeof(message_encrypt)
    date3 =  datetime.datetime.now()
    message_decrypt = aes.decrypt(message_encrypt)
    date4 =  datetime.datetime.now()
    print sys.getsizeof(message_decrypt)
    if hash_plaintex != MD5.new(message_decrypt).digest():
        print 'El mensaje no se ha descifrado'
    else:
        print 'Tiempo de descifrado'+ str(date4-date3)
        return date2-date1, date4-date3

def aes1MB():
    file = open('file1MB.txt', 'r')
    file = file.read()
    aes = AESCipher(key_generator(16))
    hash_plaintex = MD5.new(file).digest()
    date1 =  datetime.datetime.now()
    message_encrypt = aes.encrypt(file)
    date2 =  datetime.datetime.now()
    print 'Tiempo de cifrado'+ str(date2-date1)
    print sys.getsizeof(message_encrypt)
    date3 =  datetime.datetime.now()
    message_decrypt = aes.decrypt(message_encrypt)
    date4 =  datetime.datetime.now()
    print sys.getsizeof(message_decrypt)
    if hash_plaintex != MD5.new(message_decrypt).digest():
        print 'El mensaje no se ha descifrado'
    else:
        print 'Tiempo de descifrado'+ str(date4-date3)
        return date2-date1, date4-date3

def aes10MB():
    file = open('file10MB.txt', 'r')
    file = file.read()
    aes = AESCipher(key_generator(16))
    hash_plaintex = MD5.new(file).digest()
    date1 =  datetime.datetime.now()
    message_encrypt = aes.encrypt(file)
    date2 =  datetime.datetime.now()
    print 'Tiempo de cifrado'+ str(date2-date1)
    print sys.getsizeof(message_encrypt)
    date3 =  datetime.datetime.now()
    message_decrypt = aes.decrypt(message_encrypt)
    date4 =  datetime.datetime.now()
    print sys.getsizeof(message_decrypt)
    if hash_plaintex != MD5.new(message_decrypt).digest():
        print 'El mensaje no se ha descifrado'
    else:
        print 'Tiempo de descifrado'+ str(date4-date3)
        return date2-date1, date4-date3

def aes20MB():
    file = open('file20MB.txt', 'r')
    file = file.read()
    aes = AESCipher(key_generator(16))
    hash_plaintex = MD5.new(file).digest()
    date1 =  datetime.datetime.now()
    message_encrypt = aes.encrypt(file)
    date2 =  datetime.datetime.now()
    print 'Tiempo de cifrado'+ str(date2-date1)
    print sys.getsizeof(message_encrypt)
    date3 =  datetime.datetime.now()
    message_decrypt = aes.decrypt(message_encrypt)
    date4 =  datetime.datetime.now()
    print sys.getsizeof(message_decrypt)
    if hash_plaintex != MD5.new(message_decrypt).digest():
        print 'El mensaje no se ha descifrado'
    else:
        print 'Tiempo de descifrado'+ str(date4-date3)
        return date2-date1, date4-date3

def test_aes10KB():
    date = datetime.datetime.now()
    encrypt = date
    decrypt = date
    for i in range(5):
        print('Ejecucion de cifrado/descifrado AES 10KB numero ' + str(i+1))
        e, d = aes10KB()
        encrypt += e
        decrypt += d
        if i==4:
            print "Tiempo medio de cifrado: " +str((encrypt-date)/5)
            print "Tiempo medio de descifrado: " +str((decrypt-date)/5)
        print('\n')

def test_aes1MB():
    date = datetime.datetime.now()
    encrypt = date
    decrypt = date
    for i in range(5):
        print('Ejecucion de cifrado/descifrado AES 1MB numero ' + str(i+1))
        e, d = aes1MB()
        encrypt += e
        decrypt += d
        if i==4:
            print "Tiempo medio de cifrado: " +str((encrypt-date)/5)
            print "Tiempo medio de descifrado: " +str((decrypt-date)/5)
        print('\n')


def test_aes10MB():
    date = datetime.datetime.now()
    encrypt = date
    decrypt = date
    for i in range(5):
        print('Ejecucion de cifrado/descifrado AES 10MB numero ' + str(i+1))
        e, d = aes10MB()
        encrypt += e
        decrypt += d
        if i==4:
            print "Tiempo medio de cifrado: " +str((encrypt-date)/5)
            print "Tiempo medio de descifrado: " +str((decrypt-date)/5)
        print('\n')

def test_aes20MB():
    date = datetime.datetime.now()
    encrypt = date
    decrypt = date
    for i in range(5):
        print('Ejecucion de cifrado/descifrado AES 20MB numero ' + str(i+1))
        e, d = aes20MB()
        encrypt += e
        decrypt += d
        if i==4:
            print "Tiempo medio de cifrado: " +str((encrypt-date)/5)
            print "Tiempo medio de descifrado: " +str((decrypt-date)/5)
        print('\n')

test_aes10KB()
test_aes1MB()
test_aes10MB()
test_aes20MB()