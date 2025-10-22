#By Wendi


import cryptography.hazmat.primitives.ciphers

import os
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend 


plaintext = b"Have a nice day!"
key = os.urandom(32)

iv = os.urandom(16)

padder = padding.PKCS7(128).padder()
padded_data = padder.update(plaintext) + padder.finalize()




