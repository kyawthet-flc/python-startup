#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import pprint
import sys


def process_file(filename):

    with open(filename) as json_file:
        json_data = json.load(json_file)
        pprint.pprint(json_data)


if __name__ == '__main__':
    process_file('data.json')
