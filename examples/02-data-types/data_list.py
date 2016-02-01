#!/usr/bin/python

print "---------------------"
print "List basic operations"
print

# Append item to list
user_list = ["Pierre"]
user_list.append("Cedric")
print user_list

# Add lists
others = ["Manu", 12, 3.14]
user_list += others
print user_list

# Access item by index
print user_list[1]

# Pop an item
poped = user_list.pop()
print poped
print user_list

print "-------------------"
print "List comprehensions" 
print

numbers = [2, 5, 7, 34, 1]

# Build a list from another one
lower_then = [number for number in numbers if number < 7]

print lower_then
