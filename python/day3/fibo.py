#!/usr/env/python

# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, a+b


def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

def add(x,y):
    return x+y
def add(*args):
    return sum(list(args))

def foo(x,y,z):
    print (x,y,z)
def foo(x,y=3,z="world"):
    print(x,y,z)


fib(5)
x= fib2(5)
print(x)
y=add(5,6)
print(y)
z=add(4,3,2,7)
print(z)

foo(5,3,"hi")
foo(x=5,y=3,z="hi")
foo(y=3,z="hi",x=5)

foo(13)
foo(7,5)