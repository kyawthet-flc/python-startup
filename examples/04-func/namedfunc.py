#!/usr/bin/python


def my_funny_routine(name, greet='Hello'):
    '''This routine prints a greeting to the console'''
    output = "%s %s!" % (greet, name)
    print(output)
    return output

def main():

    # traditional (C-like)
    my_funny_routine('Cedric', 'Hello')

    # named args
    my_funny_routine(greet='Hi', name='Cedric')

    # ... identical to:
    my_funny_routine(name='Cedric', greet='Hi')

    # default value !
    my_funny_routine(name='Cedric')

    # Exercise:
    # change this routine to add an optional msg.
    # Hint: use the none value ;)
    #
    # calling my_funny_routine('Cedric') should now display: Hello Cedric, welcome to you!



if __name__ == '__main__':
    main()

