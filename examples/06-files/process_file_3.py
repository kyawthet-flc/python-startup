#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import pprint
import sys
import os.path
from optparse import OptionParser


def process_file(filename):

    parser = OptionParser("usage: %prog [options] filename")
    (options, args) = parser.parse_args()

    if len(args) < 1:
        print('Error: you must pass a filename')
        sys.exit(-1)

    filename = args[0]
    if not os.path.isfile(filename):
        print('Error: %s does not seem to be a file name' % filename)
        sys.exit(-2)

    with open(filename) as json_file:
        json_data = json.load(json_file)
        pprint.pprint(json_data)


if __name__ == '__main__':
    process_file('data.json')
