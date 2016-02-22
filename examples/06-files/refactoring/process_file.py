#!/usr/bin/python
import traceback
import pprint
import sys
import os.path
from optparse import OptionParser
import logging
from decoders.json_decoder import JSONFileDecoder
from notifiers.gmail_notifier import GmailNotifier

LOG_FORMAT = '%(asctime)s:%(name)s:%(levelname)s: %(message)s'

SUPPORTED_FILE_DECODERS = {  # extension: decoder
                            "json": JSONFileDecoder
                        }

class FileProcessor(object):
    """
        FileProcessor takes a data file as input and processes it
    """

    def __init__(self, filename, notifiers=None, logger=None):
        self.logger = logger if logger is not None else logging.getLogger("fileprocess")
        self.notifiers = notifiers if notifiers is not None else []
        self.decoder = self.get_decoder_from_file(filename)

    def get_decoder_from_file(self, filename):

        file_ext = "json" # FIXME: decode extension
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
        data = self.decoder.get_data()
        for employee in data['employees']:
            self.logger.debug('printing employee: %s', )
            pprint.pprint(employee)
            for notifier in self.notifiers:
                notifier.notify(contact=employee['contact'], content=self._build_notif_msg(employee))

def process_file(filename):

    parser = OptionParser("usage: %prog [options] filename")
    parser.add_option("-d", "--debug", dest="debug_level",
                      help="set log level to LEVEL", metavar="LEVEL")
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
    logger = logging.getLogger("readjson")
    notifiers = []
    notifiers.append(GmailNotifier());

    try:
        processor = FileProcessor(filename=filename, notifiers=notifiers, logger=logger)
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
    process_file('data.json')
