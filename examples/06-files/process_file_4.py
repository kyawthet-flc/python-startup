#!/usr/bin/python
import json
import pprint
import sys
import os.path
from optparse import OptionParser
import logging


LOG_FORMAT = '%(asctime)s:%(name)s:%(levelname)s: %(message)s'


def process_file(filename):

    parser = OptionParser("usage: %prog [options] filename")
    parser.add_option("-d", "--debug", dest="debug_level",
                      help="set log level to LEVEL", metavar="LEVEL")
    (options, args) = parser.parse_args()

    if len(args) < 1:
        print('Error: you must pass a filename')
        sys.exit(-1)

    filename = args[0]
    if not os.path.isfile(filename):
        print('Error: %s does not seem to be a file name' % filename)
        sys.exit(-2)

    if options.debug_level is not None:
        level = int(options.debug_level)
    else:
        level = logging.CRITICAL

    logging.basicConfig(level=level, format=LOG_FORMAT)
    logger = logging.getLogger("readjson")

    with open(filename) as json_file:
        logger.info('reading JSON data from %s', filename)
        json_data = json.load(json_file)
        logger.info('reading JSON data: done')

    for employee in json_data['employees']:
        logger.debug('printing employee: %s', employee['name'])
        pprint.pprint(employee)


if __name__ == '__main__':
    process_file('data.json')
