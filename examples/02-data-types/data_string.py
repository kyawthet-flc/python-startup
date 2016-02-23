#!/usr/bin/python
# -*- coding: utf-8 -*-

first = "Pierre" # double quote

last = 'Roth' # single quote

cv = """
     Mon CV
     sur
     plusieurs lignes
     """

contact = '''
          pierreroth4@gmail.com
          @pierreroth64
          '''

print first + " " + last
print
print "Parcours:"
print "--"
print cv

print "Contact:\n--"     # tiens tiens... un commentaire dans le code
                         # qui explique un print avec caractere special 'line feed' (\n)
print contact
