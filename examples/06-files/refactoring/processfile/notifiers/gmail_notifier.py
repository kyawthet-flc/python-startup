#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import smtplib

'''This module contains the GmailNotifier class
   which enables to notify via a Gmail account'''

SMTP_LOGIN = "pierreroth64.python.startup@gmail.com"
SMTP_PWD = 'coucou6465'


class GmailNotifier(object):

    def __init__(self, login=SMTP_LOGIN, password=SMTP_PWD):
        self.login = login
        self.password = password
        self.conn = smtplib.SMTP('smtp.gmail.com', 587)
        self.logger = logging.getLogger("gmailnotifier")
        self.is_started = False

    def _get_email_from_contact(self, contact):
        return contact["email"]

    def notify(self, contact, content):

        if not self.is_started:
            self.conn.ehlo()
            self.conn.starttls()
            self.conn.login(self.login, self.password)
            self.is_started = True

        to = self._get_email_from_contact(contact)
        self.logger.debug('sending email to %s...', to)
        self.conn.sendmail(self.login, to, content)
        self.logger.debug('sent email to %s.', to)
