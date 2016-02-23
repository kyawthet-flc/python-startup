#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest
import os.path
from decoders.json_decoder import JSONFileDecoder

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

def test_json_correct():
    '''Test the decoding when a correct file is given'''

    decoder = JSONFileDecoder(os.path.join(CURRENT_DIR, 'correct.json'))
    assert len(decoder.get_employees()) == 3


def test_json_bad_format():

    decoder = JSONFileDecoder(os.path.join(CURRENT_DIR, 'bad_format.json'))
    with pytest.raises(Exception):
        decoder.get_employees()

def test_json_not_found():

    with pytest.raises(Exception):
        JSONFileDecoder(os.path.join(CURRENT_DIR, 'not_found.json'))
