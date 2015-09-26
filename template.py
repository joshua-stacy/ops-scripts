#! /usr/bin/python

# Purpose: 
# Usage: python <program>.py --options

import os
import sys
from argparse import ArgumentParser

def argParser():
    parser = ArgumentParser(description="")

    parser.add_argument("-", "--", help="")

    args = parser.parse_args()

    if (args. is None):
        parser.print_help()
        sys.exit(1)

    return args

def main(args):
    args = argParser()

    return(0)

if __name__ == "__main__":
    main(sys.argv)
    sys.exit(0)
