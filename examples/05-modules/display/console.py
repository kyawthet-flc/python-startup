#!/usr/bin/python

# import 'batteries included' modules
import datetime
import time

def print_to_console(msg):
    '''Print message to console'''

    print("%s > %s" % (datetime.datetime.now(), msg))

# Only executed if module directly called
# _not_ called on module import
if __name__ == '__main__':

    print_to_console("hey, it's me!")
    time.sleep(1)
    print_to_console("hey again! later :)")
