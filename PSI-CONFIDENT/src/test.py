from Crypto import Random
from Crypto.Cipher import AES
import base64
import os


BLOCK_SIZE = 32
PADDING = 'skd'#Random.new().read(BLOCK_SIZE)
print PADDING.__len__()

# one-liner to sufficiently pad the text to be encrypted
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING

# one-liners to encrypt/encode and decrypt/decode a string
# encrypt with AES, encode with base64
EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)

# generate a random secret key
secret = os.urandom(BLOCK_SIZE)
print base64.b64encode(secret)
# create a cipher object using the random secret
cipher = AES.new(secret)
message = raw_input('Mete mensaje ome: ')
res = message
i = 0
while message.__len__()%16!=0:
    i += 1
    message += ' '

# encode a string
encoded = EncodeAES(cipher, message)
print 'Encrypted string:', encoded

# decode the encoded string
decoded = DecodeAES(cipher, encoded)
print 'Decrypted string:', decoded[:len(decoded)-i]

