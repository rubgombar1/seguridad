import sys
from src.tresdes import execute_3des
import datetime

__author__ = 'usuario'

def generate_files():
    stri = ''
    while sys.getsizeof(stri) < 1024*1024*20:
        stri += 'd'
    file = open('file20MB.txt', 'w')
    file.write(stri)
    print sys.getsizeof(stri)

def tresdes10KB():
    file = open('file10KB.txt', 'r')
    file = file.read()
    e,d = execute_3des(file)
    return e, d

def tresdes1MB():
    file = open('file1MB.txt', 'r')
    file = file.read()
    e, d = execute_3des(file)
    return e, d

def tresdes10MB():
    file = open('file10MB.txt', 'r')
    file = file.read()
    e, d = execute_3des(file)
    return e, d

def tresdes20MB():
    file = open('file20MB.txt', 'r')
    file = file.read()
    e, d = execute_3des(file)
    return e, d

def test_tresdes10KB():
    date = datetime.datetime.now()
    encrypt = date
    decrypt = date
    for i in range(5):
        print('Ejecucion de cifrado/descifrado 3DES 10KB numero ' + str(i+1))
        e, d = tresdes10KB()
        encrypt += e
        decrypt += d
        if i==4:
            print "Tiempo medio de cifrado: " +str((encrypt-date)/5)
            print "Tiempo medio de descifrado: " +str((decrypt-date)/5)
        print('\n')

def test_tresdes1MB():
    date = datetime.datetime.now()
    encrypt = date
    decrypt = date
    for i in range(5):
        print('Ejecucion de cifrado/descifrado 3DES 1MB numero ' + str(i+1))
        e, d = tresdes1MB()
        encrypt += e
        decrypt += d
        if i==4:
            print "Tiempo medio de cifrado: " +str((encrypt-date)/5)
            print "Tiempo medio de descifrado: " +str((decrypt-date)/5)
        print('\n')

def test_tresdes10MB():
    date = datetime.datetime.now()
    encrypt = date
    decrypt = date
    for i in range(5):
        print('Ejecucion de cifrado/descifrado 3DES 10MB numero ' + str(i+1))
        e, d = tresdes10MB()
        encrypt += e
        decrypt += d
        if i==4:
            print "Tiempo medio de cifrado: " +str((encrypt-date)/5)
            print "Tiempo medio de descifrado: " +str((decrypt-date)/5)
        print('\n')

def test_tresdes20MB():
    date = datetime.datetime.now()
    encrypt = date
    decrypt = date
    for i in range(5):
        print('Ejecucion de cifrado/descifrado 3DES 20MB numero ' + str(i+1))
        e, d = tresdes20MB()
        encrypt += e
        decrypt += d
        if i==4:
            print "Tiempo medio de cifrado: " +str((encrypt-date)/5)
            print "Tiempo medio de descifrado: " +str((decrypt-date)/5)
        print('\n')

test_tresdes10KB()
test_tresdes1MB()
test_tresdes10MB()
test_tresdes20MB()