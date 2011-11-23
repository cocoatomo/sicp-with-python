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


def test_sqrt():
    assert abs(sqrt(9) - 3.00009155413138) < 0.001
    assert abs(sqrt(100 + 37) - 11.704699917758145) < 0.001
    assert abs(sqrt(sqrt(2) + sqrt(3)) - 1.7739279023207892) < 0.001
    assert abs(square(sqrt(1000)) - 1000.000369924366) < 0.001

test_sqrt()


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


def test_qbrt():
    assert abs(qbrt(27) / 3 - 1) < 0.001
    assert abs(qbrt(1000) / 10 - 1) < 0.001
    assert abs(qbrt(2) / 1.2599210498948731647672106072782283506 - 1) < 0.001
    assert abs(qbrt(0.1) / 0.4641588833612778892410076350919446576 - 1) < 0.001

test_qbrt()


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

test_sqrt()


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

test_sqrt()


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


print('''
def f(n):
    return A(0, n)

def g(n):
    return A(1, n)

def h(n):
    return A(2, n)''')


def f(n):
    return A(0, n)


def g(n):
    return A(1, n)


def h(n):
    return A(2, n)


print('''
f(n) = 2 * n
g(n) = 2**n if n > 0 else 0
h(n) = 2**2**...**2 (<- n 2's) if n > 0 else 0
''')


def test_f():
    for n in xrange(10):
        assert f(n) == 2 * n


def test_g():
    for n in xrange(10):
        assert g(n) == (2**n if n > 0 else 0)


def test_h():
    def hh(n):
        if n == 0:
            return 0

        result = 1
        for i in xrange(n):
            result = 2**result
        return result

    for n in xrange(5):
        assert h(n) == hh(n)


print('''
1.2.2  Tree Recursion
=====================''')


def fib_iter(a, b, count):
    if count == 0:
        return b
    else:
        return fib_iter(a + b, a, count - 1)


def fib(n):
    return fib_iter(1, 0, n)


def test_fib():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5
    assert fib(6) == 8
    assert fib(7) == 13
    assert fib(8) == 21
    assert fib(9) == 34
