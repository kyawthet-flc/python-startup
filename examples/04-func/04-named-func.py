#!/usr/bin/python

def my_funny_routine(name, greet='Hello'):
    '''This routine prints a greeting to the console'''

    print("%s %s!" % (greet, name))


# traditional (C-like)
my_funny_routine('Cedric', 'Hello')

# named args
my_funny_routine(greet='Hi', name='Cedric')

# ... identical to:
my_funny_routine(name='Cedric', greet='Hi')

# default value !
my_funny_routine(name='Cedric')

# Exercise:
# change this routine to add an optional msg
# 
# calling my_funny_routine('Cedric') should now display: Hello Cedric, welcome to you!