#!/usr/bin/python

AGE_LIMIT = 70
age = 23
is_a_boy = True
is_young = (age > AGE_LIMIT)

if is_a_boy and not is_young:
    print 'Your are an "old" man... (above %d years old)' % AGE_LIMIT
