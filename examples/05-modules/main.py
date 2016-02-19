#!/usr/bin/python

from display.console import print_to_console             # import print_console from your console module of your display package

username = raw_input('Enter your usernamee: ')   # raw_input is a built-in
print_to_console("Hey! %s talking!" % username)

