#!/usr/bin/python
# -*- coding: utf-8 -*-

company_info = {
	'name': 'My super company',
	'address': '45, beautiful avenue, blabla, France',
	'number of employees': 3,
	'employees': [
		"Pierre",
		"Cedric",
		"Manu"
	],
	'contact': {
		'email': 'contact@my-super-company.com',
		'phone': '+33 567874332'
	}
}
print "raw display"
print company_info

print

import pprint
pp = pprint.PrettyPrinter(indent=4)
print "pretty display"
pp.pprint(company_info)


# access field
print "access value from key"
print 'company name:', company_info['name']
print

# get keys and values
print "get keys and values"
print 'company keys:', company_info.keys()
print 'company values:', company_info.values()
print

# iter over key and values
print "iterate over key & values"
for key, value in company_info.items():
	print '\tkey:', key
	print '\tvalue:', value
print
