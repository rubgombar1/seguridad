__author__ = 'usuario'
import base64
from Crypto.Cipher import AES
from Crypto import Random

class AESCipher:
    def __init__( self, key ):
        self.key = key

    def encrypt( self, raw ):
        BS = 16
        pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw ) )

    def decrypt( self, enc ):
        unpad = lambda s : s[:-ord(s[len(s)-1:])]
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc[16:] ))