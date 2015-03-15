import random
import string
from Crypto.Cipher import DES3
from Crypto import Random


def key_generator(size=7, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

key = key_generator(16)
iv = Random.get_random_bytes(8)
des1 = DES3.new(key, DES3.MODE_CFB, iv)
des2 = DES3.new(key, DES3.MODE_CFB, iv)
text = 'viky mongui'
print text
cipher_text = des1.encrypt(text)
print des2.decrypt(cipher_text)
