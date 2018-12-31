#! /usr/bin/python

# Purpose: 
# Usage: python <program>.py --options

import os
import sys
from argparse import ArgumentParser
import yaml
import json

def argParser():
    parser = ArgumentParser(description="Converts YAML file to JSON or vice versa")

    parser.add_argument("-f", "--file", help="File to convert", required=True)

    args = parser.parse_args()

    return args

def yml_to_json(args):
	with open(args.file, 'r') as stream:
		try:
			datamap = yaml.safe_load(stream)
			with open(args.file.replace("yml", "json"), 'w') as output_file:
				json.dump(datamap, output_file)
		except yaml.YAMLError as exc:
			print(exc)
	output_file.close()
	return (0)

def json_to_yml(args):
	with open(args.file, 'r') as stream:
		try:
			datamap = json.load(stream)
			with open(args.file.replace("json", "yml"), 'w') as output_file:
				yaml.dump(datamap, output_file)
		except yaml.YAMLError as exc:
			print(exc)
	output_file.close()
	return (0)	

def main(args):
    args = argParser()
    if args.file.find("yml") > -1:
    	yml_to_json(args)
    elif args.file.find("json") > -1:
    	json_to_yml(args)
    else:
    	print ("File " + args.file + " incorrect format")
    	print Usage

    return(0)

if __name__ == "__main__":
    main(sys.argv)