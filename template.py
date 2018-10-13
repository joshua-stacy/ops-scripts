#! /usr/bin/python

# Purpose: 
# Usage: python <program>.py --options

import os
import sys
from argparse import ArgumentParser

def argParser():
    parser = ArgumentParser(description="Prints base64 encoded password")

    parser.add_argument("-p", "--password", help="Password to encode", required=True)

    args = parser.parse_args()

    return args

def main(args):
    args = argParser()

    return(0)

if __name__ == "__main__":
    main(sys.argv)
