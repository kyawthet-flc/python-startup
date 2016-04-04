#!/usr/bin/python
# -*- coding: utf-8 -*-

from processfile.decoders.base_decoder import BaseFileDecoder
import json

'''This module contains the JSONFileDecoder class
   which decodes JSON data'''


class JSONFileDecoder(BaseFileDecoder):

    def __init__(self, filename, logger=None):
        super(JSONFileDecoder, self).__init__(filename, logger)

    def get_employees(self):
        try:
            with open(self.filename) as json_file:
                self.logger.info('reading JSON data from %s', self.filename)
                json_data = json.load(json_file)
                self.logger.info('reading JSON data: done')
            return json_data['employees']
        except Exception as error:
            self.logger.critical('Error when reading JSON file: %s' % error)
            raise error
