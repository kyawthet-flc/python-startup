#!/usr/bin/python
# -*- coding: utf-8 -*-

# Non pythonic way (C-like)
numbers = [2, 3, 7, 8, 90, 8, 8, 8]
odds = []

for number in numbers:
    if number % 2:
        odds.append(number)
print "odds (c-developer):", odds

# Pythonic way using list-comprehension
odds = [number for number in numbers if number % 2]
print "odds (pythonista!):", odds

# You can do it with list of dicts
AGE_LIMIT = 49
people = [
	{'name': 'Manu', 'age': 35},
	{'name': 'Cedric', 'age': 40},
	{'name': 'Diego', 'age': 56} ]

old_ones = []
for person in people:
    if person['age'] > AGE_LIMIT:
	old_ones.append(person['name'])
print "old ones (c-developer):", old_ones

# 1 line instead of 4!
old_ones = [person['name'] for person in people if person['age'] > AGE_LIMIT]
print "old ones (pythonista!):", old_ones
