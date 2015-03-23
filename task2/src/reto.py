import random
import string
from src.aes import AESCipher


def key_generator(size=7, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
aes = AESCipher(key_generator(16))
file = open('1-1276102022HnzE.jpg', 'r')
imagen = open('asd.jpg', 'w')
res = file.read()
header = res[:109]
image = res[109:]
encrypt = aes.encrypt(image)

imagen.write(header+encrypt)


print image