#!/usr/bin/python


def my_varargs_routine(*args, **kwargs):
    '''This routine prints out passed args to the console'''

    for arg in args:
        print(arg)

    for key, value in kwargs.items():
        print ('key: %s, value: %s' % (key, value))

    print '-----------------'

def main():

    my_varargs_routine(1, 2)

    my_varargs_routine(1, 2, name='Cedric', greet='Hello')


if __name__ == '__main__':
    main()
