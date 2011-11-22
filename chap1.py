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


print('''
Exercise 1.8''')


def improve(guess, x):
    return (x / guess**2 + 2 * guess) / 3


def qube(x):
    return x**3


def good_enough(guess, x):
    return abs(qube(guess) / x - 1) < 0.001


def qbrt_iter(guess, x):
    if good_enough(guess, x):
        return guess
    else:
        return qbrt_iter(improve(guess, x), x)


def qbrt(x):
    return qbrt_iter(1.0, x)


def _qbrt_test():
    print(qbrt(27))
    print(qbrt(1000))
    print(qbrt(2))
    print(qbrt(0.1))

_qbrt_test()


print('''
1.1.8  Procedures as Black-Box Abstractions
===========================================
''')


print('''
Internal definitions and block structure
----------------------------------------''')


def sqrt(x):
    def good_enough(guess, x):
        return abs(square(guess) - x) < 0.001

    def improve(guess, x):
        return average(guess, x / guess)

    def sqrt_iter(guess, x):
        if good_enough(guess, x):
            return guess
        else:
            return sqrt_iter(improve(guess, x), x)

    return sqrt_iter(1.0, x)

_test()


print('''
lexical scoping''')

def sqrt(x):
    def good_enough(guess):
        return abs(square(guess) - x) < 0.001

    def improve(guess):
        return average(guess, x / guess)

    def sqrt_iter(guess):
        if good_enough(guess):
            return guess
        else:
            return sqrt_iter(improve(guess))

    return sqrt_iter(1.0)

_test()


print('''
Exercise 1.10
=============''')


def A(x, y):
    if y == 0:
        return 0
    elif x == 0:
        return 2 * y
    elif y == 1:
        return 2
    else:
        return A(x - 1, A(x, y - 1))


print(A(1, 10))
print(A(2, 4))
print(A(3, 3))

