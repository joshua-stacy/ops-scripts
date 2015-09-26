#! /usr/bin/python

# Purpose: Deletes or replaces text in file and overwrites file, for when you don't want to mess with sed
# Usage: python replace_text.py -r <text_to_replace> -w <replacement_value>

import os
import sys
from argparse import ArgumentParser

def argParser():
    parser = ArgumentParser(description="")

    parser.add_argument("-f", "--file", help="File to Open")
    parser.add_argument("-o", "--old", help="Text to replace.")
    parser.add_argument("-n", "--new", help="Text to input in place.")

    args = parser.parse_args()

    if (args.file is None or args.old is None):
        parser.print_help()
        sys.exit(1)
    if args.new is None:
    	args.new = ""

    return (args)


def replaceText(args):
	textinput = open(args.file)
	lineread = textinput.readlines()
	output_lines = []
	
	for line in lineread:
		print line
		if line.find(args.old) > -1:
			new_string = line.replace(args.old, args.new)
			output_lines.append(new_string)
		else:
			output_lines.append(line)

	textinput.close()
	return (output_lines)

def writeFile (args, output):
	textoutput = open ( args.file, 'w' )
	for item in output:
		print item		
		textoutput.write(item)
		
	textoutput.close()
	return 0

def main (args):
	args = argParser()
	output = replaceText(args)
	print ("Writing File")
	writeFile(args, output)
	return 0

if __name__ == "__main__":
    main(sys.argv)
    sys.exit(0)
