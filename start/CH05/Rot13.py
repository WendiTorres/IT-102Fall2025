#!/usr/bin/env python3
# Script that encrypts/decrypts text using ROT13
# By Wendi

#Create a simple Caesar Cipher encryption

import string 

plain_text = "Have a nice day!"

shift = 24


alphabet = string.ascii_lowercase
shifted = alphabet[shift:] + alphabet[:shift]

