#! /usr/bin/python

# Purpose: Prints base64 encoded password	
# Usage: python password.py --password


import base64
import sys
from argparse import ArgumentParser

def argParser():
    parser = ArgumentParser(description="Prints base64 encoded password")

    parser.add_argument("-p", "--password", help="Password to encode")

    args = parser.parse_args()

    if (args.password is None):
        parser.print_help()
        sys.exit(1)

    return args

def main(args):
    args = argParser()
    encoded_password=base64.b64encode(args.password)
    print ("Encoded Password: " + str(encoded_password))

    return(0)

if __name__ == "__main__":
    main(sys.argv)
    sys.exit(0)
