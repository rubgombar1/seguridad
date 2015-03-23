import datetime
from src.RSA import execute_RSA

__author__ = 'usuario'


def rsa10KB():
    file = open('file10KB.txt', 'r')
    file = file.read()
    e,d = execute_RSA(file)
    return e, d

def rsa1MB():
    file = open('file1MB.txt', 'r')
    file = file.read()
    e, d = execute_RSA(file)
    return e, d

def rsa10MB():
    file = open('file10MB.txt', 'r')
    file = file.read()
    e, d = execute_RSA(file)
    return e, d

def rsa20MB():
    file = open('file20MB.txt', 'r')
    file = file.read()
    e, d = execute_RSA(file)
    return e, d

def test_rsa10KB():
    date = datetime.datetime.now()
    encrypt = date
    decrypt = date
    for i in range(5):
        print('Ejecucion de cifrado/descifrado RSA 10KB numero ' + str(i+1))
        e, d = rsa10KB()
        encrypt += e
        decrypt += d
        if i==4:
            print "Tiempo medio de cifrado: " +str((encrypt-date)/5)
            print "Tiempo medio de descifrado: " +str((decrypt-date)/5)
        print('\n')

def test_rsa1MB():
    date = datetime.datetime.now()
    encrypt = date
    decrypt = date
    for i in range(5):
        print('Ejecucion de cifrado/descifrado RSA 1MB numero ' + str(i+1))
        e, d = rsa1MB()
        encrypt += e
        decrypt += d
        if i==4:
            print "Tiempo medio de cifrado: " +str((encrypt-date)/5)
            print "Tiempo medio de descifrado: " +str((decrypt-date)/5)
        print('\n')

def test_rsa10MB():
    date = datetime.datetime.now()
    encrypt = date
    decrypt = date
    for i in range(5):
        print('Ejecucion de cifrado/descifrado RSA 10MB numero ' + str(i+1))
        e, d = rsa10MB()
        encrypt += e
        decrypt += d
        if i==4:
            print "Tiempo medio de cifrado: " +str((encrypt-date)/5)
            print "Tiempo medio de descifrado: " +str((decrypt-date)/5)
        print('\n')

def test_rsa20MB():
    date = datetime.datetime.now()
    encrypt = date
    decrypt = date
    for i in range(5):
        print('Ejecucion de cifrado/descifrado 3DES 20MB numero ' + str(i+1))
        e, d = rsa20MB()
        encrypt += e
        decrypt += d
        if i==4:
            print "Tiempo medio de cifrado: " +str((encrypt-date)/5)
            print "Tiempo medio de descifrado: " +str((decrypt-date)/5)
        print('\n')

test_rsa10KB()
test_rsa1MB()
test_rsa10MB()
test_rsa20MB()
