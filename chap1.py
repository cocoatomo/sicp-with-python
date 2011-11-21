#!/usr/local/bin/python
# -*- coding: utf-8 -*-

print('Exercise 1.5')

def p():
    p()

def test(x, y):
    if x == 0:
        return 0
    else:
        return y

print(test(0, p))

print("1.1.7 Example: Square Roots by Newton's Method")

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

if __name__ == '__main__':
    _test()
