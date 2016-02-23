#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import os.path

'''This module contains the BaseFileDecoder class, the parent class of all the file decoders'''


class BaseFileDecoder(object):
    '''Base class for file decoders. It is the interface to be implemented'''

    def __init__(self, filename, logger=None):
        if not os.path.isfile(filename):
            raise Exception('%s does not seem to be a file name' % filename)
        self.filename = filename
        self.logger = logger if logger is not None else logging.getLogger("filedecoder")

    def get_employees(self):
        raise Exception('get_employees must be implented in your class!')
