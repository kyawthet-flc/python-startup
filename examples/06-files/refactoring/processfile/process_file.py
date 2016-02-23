#!/usr/bin/python
# -*- coding: utf-8 -*-

import traceback
import pprint
import sys
import os.path
from optparse import OptionParser
import logging
from decoders.json_decoder import JSONFileDecoder
from decoders.xml_decoder import XMLFileDecoder
from notifiers.gmail_notifier import GmailNotifier
from notifiers.sms_notifier import SMSNotifier

LOG_FORMAT = '%(asctime)s:%(name)s:%(levelname)s: %(message)s'

SUPPORTED_FILE_DECODERS = {  # extension: decoder
    ".json": JSONFileDecoder,
    ".xml": XMLFileDecoder
}


class FileProcessor(object):
    """
        FileProcessor takes a data file as input and processes it
    """

    def __init__(self, filename, notifiers=None):
        self.logger = logging.getLogger("fileprocess")
        self.notifiers = notifiers if notifiers is not None else []
        self.decoder = self._get_decoder_from_file(filename)

    def _get_decoder_from_file(self, filename):

        file_ext = os.path.splitext(filename)[1]
        for ext, decoder_class in SUPPORTED_FILE_DECODERS.items():
            if ext == file_ext:
                return decoder_class(filename=filename, logger=self.logger)

        raise Exception("Not decoder found for extension %s", file_ext)

    def _build_notif_msg(self, employee):

        content = "Hi %s!\n\n" % employee['name']
        content += "Your remaining days: %s\n\n" % (employee['holidays']['remaining'])
        content += "-- your smart employer ;)"
        return content

    def process(self):
        employees = self.decoder.get_employees()
        for employee in employees:
            print('processing employee: %s...' % employee['name'])
            for notifier in self.notifiers:
                notifier.notify(contact=employee['contact'],
                                content=self._build_notif_msg(employee))
            print('done.')


def process_file():

    parser = OptionParser("usage: %prog [options] filename")
    parser.add_option("-d", "--debug", dest="debug_level",
                      help="set log level to LEVEL", metavar="LEVEL")
    parser.add_option("-n", "--no-notification", dest="no_notif", action="store_true",
                      default=False,
                      help="disable notifications")
    (options, args) = parser.parse_args()

    if len(args) < 1:
        print('Error: you must pass a filename')
        sys.exit(-1)
    filename = args[0]

    if options.debug_level is not None:
        level = int(options.debug_level)
    else:
        level = logging.CRITICAL

    logging.basicConfig(level=level, format=LOG_FORMAT)
    notifiers = []
    if not options.no_notif:
        notifiers.append(GmailNotifier())
        notifiers.append(SMSNotifier())

    try:
        processor = FileProcessor(filename=filename, notifiers=notifiers)
        processor.process()
        sys.exit(0)
    except Exception as error:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        tb_lines = traceback.format_tb(exc_traceback)
        for line in tb_lines:
            print line
        print("Error: %s" % error)
        sys.exit(-1)

if __name__ == '__main__':
    process_file()
