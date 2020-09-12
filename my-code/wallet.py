from Crypto.PublicKey import RSA
import Crypto.Random
import binascii


class Wallet:
    def __init__(self):
        pass

    def generate_keys(self):
        rand_func = Crypto.Random.new().read
        print(rand_func)
        # private_key = RSA.generate(1024, rand_func)
        # public_key = private_key.publickey()
        # return (
        #     binascii.hexlify(private_key.exportKey(format='DER')).decode('ascii'),
        #     binascii.hexlify(public_key.exportKey(format='DER')).decode('ascii')
        # )
