#!/usr/bin/python
# -*- coding: utf-8 -*-

from namedfunc import my_funny_routine

def test_my_funny():
	assert my_funny_routine('Cedric') == "Hello Cedric!"
