#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging


'''This module contains the SMSNotifier class which enables to notify via Short Message Service'''


class SMSNotifier(object):

    def __init__(self):
        self.logger = logging.getLogger("smsnotifier")

    def _get_phone_from_contact(self, contact):
        return contact["phone"]

    def notify(self, contact, content):

        to = self._get_phone_from_contact(contact)
        self.logger.debug('sending SMS to %s...', to)
        #FIXME: Actually send the SMS here!
        self.logger.debug('sent SMS to %s.', to)
