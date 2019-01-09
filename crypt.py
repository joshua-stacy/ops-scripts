#! /usr/bin/python

# Purpose: 
# Usage: python <program>.py --options

import os
import sys
from argparse import ArgumentParser
import getpass
import base64
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

def argParser():
	parser = ArgumentParser(description="Prints base64 encoded password")
	parser.add_argument("-a", "--action", help="Encrypt or Decrypt", default="decrypt", choices=["encrypt", "decrypt"], required=True)
	parser.add_argument("-f", "--file", help="File to Encrypt/Decrypt", required=True)
	parser.add_argument("-p", "--password", help="Optional Password", required=False)
	args = parser.parse_args()

	return args


def encryptfile(args, key, encode=True):
	input_file = open(args.file, 'r')
	textinput = input_file.read()
	input_file.close()
	key = SHA256.new(key).digest()  # use SHA-256 over our key to get a proper-sized AES key
	IV = Random.new().read(AES.block_size)  # generate IV
	encryptor = AES.new(key, AES.MODE_CBC, IV)
	padding = AES.block_size - len(textinput) % AES.block_size  # calculate needed padding
	textinput += chr(padding) * padding
	data = IV + encryptor.encrypt(textinput)  # store the IV at the beginning and encrypt
	encrypted_text = base64.b64encode(data).decode("latin-1") if encode else data
	output_file = open(args.file, 'w')
	output_file.write(encrypted_text)
	output_file.close()
	return (0)

def decryptfile(args, key, decode=True):
	input_file = open(args.file, 'r')
	encrypted_text = input_file.read()
	input_file.close()
	if decode:
		encrypted_text = base64.b64decode(encrypted_text.encode("latin-1"))
	key = SHA256.new(key).digest()  # use SHA-256 over our key to get a proper-sized AES key
	IV = encrypted_text[:AES.block_size]  # extract the IV from the beginning
	decryptor = AES.new(key, AES.MODE_CBC, IV)
	data = decryptor.decrypt(encrypted_text[AES.block_size:])  # decrypt
	padding = ord(data[-1])
	if data[-padding:] !=chr(padding) * padding:
		raise ValueError("Invalid padding...")
	output_file = open(args.file, 'w')
	output_file.write(data[:-padding])
	output_file.close()
	return (0)

def getpassword(args, verify):
	if args.password is not None:
		return(args.password)
	else:
		password = getpass.getpass(prompt="Password: ")
		if verify:
			verify_password = getpass.getpass(prompt="Verify Password: ")
			if password != verify_password:
				print("Passwords do not match.")
				exit(1)
		return (password)

def main(args):
	args = argParser()

	if args.action == "encrypt":
		password = getpassword(args, True)
		encryptfile(args, password)
		exit(0)
	elif args.action == "decrypt":
		password = getpassword(args, False)
		decryptfile(args, password)
	exit(0)

if __name__ == "__main__":
    main(sys.argv)

