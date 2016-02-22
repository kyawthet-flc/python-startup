from base_decoder import BaseFileDecoder
import json

class JSONFileDecoder(BaseFileDecoder):

    def __init__(self, filename, logger=None):
        super(JSONFileDecoder, self).__init__(filename, logger)

    def get_data(self):
        with open(self.filename) as json_file:
            self.logger.info('reading JSON data from %s', self.filename)
            json_data = json.load(json_file)
            self.logger.info('reading JSON data: done')
        return json_data
