__author__ = 'usuario'
from Crypto.PublicKey import RSA
from Crypto import Random

KEY_LENGTH = 1024  # Key size (in bits)
random_gen = Random.new().read

keypair_snowden = RSA.generate(KEY_LENGTH, random_gen)
pubkey_snowden  = keypair_snowden.publickey()
message_to_snowden  = 'You are a patriot!'
encrypted_for_snowden   = pubkey_snowden.encrypt(message_to_snowden, 111)
decrypted_snowden   = keypair_snowden.decrypt(encrypted_for_snowden)
print(encrypted_for_snowden)
print(decrypted_snowden)