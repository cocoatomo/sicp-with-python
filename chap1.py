#!/usr/local/bin/python
# -*- coding: utf-8 -*-

print('''
Exercise 1.5
============''')

def p():
    p()

def test(x, y):
    if x == 0:
        return 0
    else:
        return y

print(test(0, p))

print('''
1.1.7 Example: Square Roots by Newton's Method
==============================================''')

def average(x, y):
    return (x + y) / 2

def improve(guess, x):
    return average(guess, x / guess)

def square(x):
    return x * x

def good_enough(guess, x):
    return abs(square(guess) - x) < 0.001

def sqrt_iter(guess, x):
    if good_enough(guess, x):
        return guess
    else:
        return sqrt_iter(improve(guess, x), x)

def sqrt(x):
    return sqrt_iter(1.0, x)


def _test():
    print(sqrt(9))
    print(sqrt(100 + 37))
    print(sqrt(sqrt(2) + sqrt(3)))
    print(square(sqrt(1000)))

_test()


print('''
Exercise 1.7
============''')

print('''
good_enough(10**10, 10**10 + 1)
expect: True, actual: {0}'''.format(good_enough(10**10, 10**10 + 1)))

print('''
good_enough(0.00001, 0.0001)
expect: False, actual: {0}'''.format(good_enough(0.0001, 0.0009)))

print('re-define "good_enough" to show calculation process')

def good_enough(guess, x):
    print('guess: {0}'.format(guess))
    return abs(square(guess) - x) < 0.001

print('''
sqrt(10**10) (obviously is 10**5)
---------------------------------''')
print('actual: {0}'.format(sqrt(10**10)))

print('''
sqrt(0.0001) (obviously is 0.01)
----------------------------------''')
print('actual: {0}'.format(sqrt(0.0001)))

print('''
refining good_enough function...

def good_enough(guess, x):
    print('guess: {0}'.format(guess))
    return abs(square(guess) / x - 1) < 0.001''')

print('re-run')

def good_enough(guess, x):
    print('guess2: {0}'.format(guess))
    return abs((square(guess) / x) - 1) < 0.001

print('''
sqrt(10**10) (obviously is 10**5)
---------------------------------''')
print('actual: {0}'.format(sqrt(10**10)))

print('''
sqrt(0.0001) (obviously is 0.01)
----------------------------------''')
print('actual: {0}'.format(sqrt(0.0001)))
