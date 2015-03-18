import datetime
from src.blowfish import execute_blowfish

__author__ = 'usuario'


def blowFish10KB():
    file = open('file10KB.txt', 'r')
    file = file.read()
    e,d = execute_blowfish(file)
    return e, d

def blowFish1MB():
    file = open('file1MB.txt', 'r')
    file = file.read()
    e, d = execute_blowfish(file)
    return e, d

def blowFish10MB():
    file = open('file10MB.txt', 'r')
    file = file.read()
    e, d = execute_blowfish(file)
    return e, d

def blowFish20MB():
    file = open('file20MB.txt', 'r')
    file = file.read()
    e, d = execute_blowfish(file)
    return e, d

def test_blowFish10KB():
    date = datetime.datetime.now()
    encrypt = date
    decrypt = date
    for i in range(5):
        print('Ejecucion de cifrado/descifrado BlowFish 10KB numero ' + str(i+1))
        e, d = blowFish10KB()
        encrypt += e
        decrypt += d
        if i==4:
            print "Tiempo medio de cifrado: " +str((encrypt-date)/5)
            print "Tiempo medio de descifrado: " +str((decrypt-date)/5)
        print('\n')

def test_blowFish1MB():
    date = datetime.datetime.now()
    encrypt = date
    decrypt = date
    for i in range(5):
        print('Ejecucion de cifrado/descifrado BlowFish 1MB numero ' + str(i+1))
        e, d = blowFish1MB()
        encrypt += e
        decrypt += d
        if i==4:
            print "Tiempo medio de cifrado: " +str((encrypt-date)/5)
            print "Tiempo medio de descifrado: " +str((decrypt-date)/5)
        print('\n')

def test_blowFish10MB():
    date = datetime.datetime.now()
    encrypt = date
    decrypt = date
    for i in range(5):
        print('Ejecucion de cifrado/descifrado BlowFish 10MB numero ' + str(i+1))
        e, d = blowFish10MB()
        encrypt += e
        decrypt += d
        if i==4:
            print "Tiempo medio de cifrado: " +str((encrypt-date)/5)
            print "Tiempo medio de descifrado: " +str((decrypt-date)/5)
        print('\n')

def test_blowFish20MB():
    date = datetime.datetime.now()
    encrypt = date
    decrypt = date
    for i in range(5):
        print('Ejecucion de cifrado/descifrado BlowFish 20MB numero ' + str(i+1))
        e, d = blowFish20MB()
        encrypt += e
        decrypt += d
        if i==4:
            print "Tiempo medio de cifrado: " +str((encrypt-date)/5)
            print "Tiempo medio de descifrado: " +str((decrypt-date)/5)
        print('\n')

test_blowFish10KB()
test_blowFish1MB()
test_blowFish10MB()
test_blowFish20MB()