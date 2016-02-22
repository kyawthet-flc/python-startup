
import os.path

class BaseFileDecoder(object):
    '''Base class for file decoders. It is the interface to be implemented'''

    def __init__(self, filename, logger=None):
        if not os.path.isfile(filename):
           raise Exception('%s does not seem to be a file name' % filename)
        self.filename = filename
        self.logger = logger if logger is not None else logging.getLogger("filedecoder")

    def get_data(self):
        raise Exception('get_data must be implented in your class!')
