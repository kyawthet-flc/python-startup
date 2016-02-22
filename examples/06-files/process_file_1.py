#!/usr/bin/python
import json
import sys

def process_file(filename):

    with open(filename) as json_file:
        json_data = json.load(json_file)
        print(json_data)

if __name__ == '__main__':
    process_file('data.json')
    sys.exit(0);
