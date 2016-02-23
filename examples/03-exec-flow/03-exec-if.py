#!/usr/bin/python
# -*- coding: utf-8 -*-

AGE_LIMIT = 70
age = 74
is_a_boy = True
is_young = (age <= AGE_LIMIT)

if is_a_boy and not is_young:
    print 'Your are an "old" man... (%d which above the %d limit)' % (age, AGE_LIMIT)
else:
    print 'You are not an old man'
