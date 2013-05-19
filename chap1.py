#!/usr/local/bin/python3
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
    for n in range(10):
        assert f(n) == 2 * n

test_f()


def test_g():
    for n in range(10):
        assert g(n) == (2**n if n > 0 else 0)

test_g()


def test_h():
    def hh(n):
        if n == 0:
            return 0

        result = 1
        for i in range(n):
            result = 2**result
        return result

    for n in range(5):
        assert h(n) == hh(n)

test_h()

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

test_fib()


print('''
Example: Counting change
========================''')


def first_denomination(kinds_of_coins):
    if kinds_of_coins == 1:
        return 1
    elif kinds_of_coins == 2:
        return 5
    elif kinds_of_coins == 3:
        return 10
    elif kinds_of_coins == 4:
        return 25
    elif kinds_of_coins == 5:
        return 50


def cc(amount, kinds_of_coins):
    if amount == 0:
        return 1
    elif amount < 0 or kinds_of_coins == 0:
        return 0
    else:
        return cc(amount, kinds_of_coins - 1) + \
            cc(amount - first_denomination(kinds_of_coins), kinds_of_coins)


def count_change(amount):
    return cc(amount, 5)


def test_cc():
    assert count_change(100) == 292

test_cc()

print('''
Exercise 1.11
=============''')


def f(n):
    """recursive version"""
    if n < 3:
        return n
    else:
        return f(n - 1) + 2 * f(n - 2) + 3 * f(n - 3)


def test_f():
    assert f(0) == 0
    assert f(1) == 1
    assert f(2) == 2
    assert f(3) == 4
    assert f(4) == 11
    assert f(5) == 25
    assert f(6) == 59
    assert f(7) == 142
    assert f(8) == 335
    assert f(9) == 796

test_f()


def f(n):
    """iterative version"""
    return f_iter(2, 1, 0, n)


def f_iter(a, b, c, count):
    if count == 0:
        return c
    elif count == 1:
        return b
    elif count == 2:
        return a
    else:
        return f_iter(a + 2 * b + 3 * c, a, b, count - 1)


def test_f2():
    test_f()


print('''
Exercise 1.12
=============''')


def pascal_triangle(m, n):
    if n == 0:
        return 1
    elif n == m:
        return 1
    else:
        return pascal_triangle(m - 1, n) + pascal_triangle(m - 1, n - 1)


for m in range(5):
    print(' '.join(str(pascal_triangle(m, n)) for n in range(m + 1)))


print('''
Exercise 1.13
=============''')


print('proof: obvious.')

print('''
1.2.3  Orders of Growth
=======================''')

print('''
Exercise 1.14
=============''')

pass

print('''
Exercise 1.15
=============''')

pass

print('''
1.2.4  Exponentiation
=====================''')


def expt_iter(b, counter, product):
    if counter == 0:
        return product
    else:
        return expt_iter(b, counter - 1, b * product)


def expt(b, n):
    return expt_iter(b, n, 1)


def test_expt():
    for b in range(10):
        for n in range(10):
            assert expt(b, n) == b**n

test_expt()


def even(n):
    return (n % 2) == 0


def fast_expt(b, n):
    if n == 0:
        return 1
    elif even(n):
        return square(fast_expt(b, n // 2))
    else:
        return b * fast_expt(b, n - 1)


def test_fast_expt():
    for b in range(10):
        for n in range(10):
            assert fast_expt(b, n) == b**n

test_fast_expt()

print('''
Exercise 1.16
=============''')


def expt_iter(b, exponent, product):
    """invariant: b**exponent * product
    """
    if exponent == 0:
        return product
    elif even(exponent):
        return expt_iter(square(b), exponent // 2, product)
    else:
        return expt_iter(square(b), (exponent - 1) // 2, b * product)


def test_expt2():
    test_expt()

test_expt2()

print('''
Exercise 1.17
=============''')


def halve(b):
    return b // 2


def double(n):
    return n + n


def fast_int_mul(a, b):
    if b < 0:
        return -fast_int_mul(a, -b)
    elif b == 0:
        return 0
    elif even(b):
        return double(fast_int_mul(a, halve(b)))
    else:
        return a + fast_int_mul(a, b - 1)


def test_fast_int_mul():
    for a in range(-5, 10):
        for b in range(-5, 10):
            assert fast_int_mul(a, b) == a * b

test_fast_int_mul()

print('''
Exercise 1.18
=============''')


def int_mul_iter(a, multiplier, summation):
    if multiplier == 0:
        return summation
    elif even(multiplier):
        return int_mul_iter(double(a), halve(multiplier), summation)
    else:
        return int_mul_iter(double(a), halve(multiplier - 1), a + summation)


def int_mul(a, b):
    return int_mul_iter(a, b, 0)


def test_int_mul():
    for a in range(10):
        for b in range(10):
            assert int_mul(a, b) == a * b

test_int_mul()

print('''
Exercise 1.19
=============''')


def fib(n):
    return fib_iter(1, 0, 0, 1, n)


def fib_iter(a, b, p, q, count):
    """fibonacci series.

    fib(0) = 0, fib(1) = 1, fib(2) = 1,...

    fib(n) = b_n

    a_0 = 1, b_0 = 0

    (a_n) = T_{p q}^n (a_0)
    (b_n)             (b_0)

    T_{p q} = (p + q q)
              (q     p)

    T_{0 1} = (1 1)
              (1 0)
    """
    if count == 0:
        return b
    elif even(count):
        return fib_iter(a,
                        b,
                        square(p) + square(q),
                        2 * p * q + square(q),
                        count // 2)
    else:
        return fib_iter(b * q + a * q + a * p,
                        b * p + a * q,
                        p,
                        q,
                        count - 1)


def test_fib2():
    test_fib()

test_fib2()

print('''
1.2.5  Greatest Common Divisors
===============================''')

print('''
Exercise 1.20
=============''')

pass

print('''
1.2.6  Example: Testing for Primality
=====================================''')

print('''
Exercise 1.21
=============''')


def divides(a, b):
    return (b % a) == 0


def find_divisor(n, test_divisor):
    if square(test_divisor) > n:
        return n
    elif divides(test_divisor, n):
        return test_divisor
    else:
        return find_divisor(n, test_divisor + 1)


def smallest_divisor(n):
    return find_divisor(n, 2)


def prime(n):
    return n == smallest_divisor(n)


def test_prime():
    assert prime(2)
    assert prime(3)
    assert not prime(4)
    assert prime(5)
    assert not prime(6)
    assert prime(7)
    assert not prime(8)
    assert not prime(9)
    assert not prime(10)
    assert prime(11)

test_prime()


def expmod(base, exp, m):
    if exp == 0:
        return 1
    elif even(exp):
        return square(expmod(base, exp // 2, m)) % m
    else:
        return (base * expmod(base, exp - 1, m)) % m


def test_expmod():
    assert expmod(1, 1, 2) == 1
    assert expmod(1, 2, 2) == 1
    assert expmod(2, 2, 3) == 1
    assert expmod(2, 3, 4) == 0
    assert expmod(4, 2, 5) == 1
    assert expmod(2, 3, 6) == 2
    assert expmod(3, 2, 7) == 2


test_expmod()


def fermat_test(n):
    def try_it(a):
        return expmod(a, n, n) == a

    import random

    return try_it(1 + random.randrange(n - 1))


def fast_prime(n, times):
    if times == 0:
        return True
    elif fermat_test(n):
        return fast_prime(n, times - 1)
    else:
        return False


def test_fast_prime(times):
    assert fast_prime(2, times)
    assert fast_prime(3, times)
    assert not fast_prime(4, times)
    assert fast_prime(5, times)
    assert not fast_prime(6, times)
    assert fast_prime(7, times)
    assert not fast_prime(8, times)
    assert not fast_prime(9, times)
    assert not fast_prime(10, times)
    assert fast_prime(11, times)

test_fast_prime(10)
