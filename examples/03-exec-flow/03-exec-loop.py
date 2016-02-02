#!/usr/bin/python

for i in range(10):
    print 'loop (count: %d)' % i

print

users = ['Manu', 'Cedric', 'Diego']

for user in users:
    msg = '%s is a marvelous Python developer' % user
    extra_msg = ''
    if user is 'Diego':
	extra_msg = ' (and loves cheese and wine)'
    print msg + extra_msg

print

users = {
	'Manu': 'Linux man',
	'Diego': 'Validation man',
	'Cedric': 'System man' }

for key, value in users.items():
    print "%s is a %s" % (key, value)

print

index = 0
while index < 5:
    print index
    index += 1
	
