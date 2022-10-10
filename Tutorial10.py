# Python Numbers

'''3 Numeric Types'''
from tkinter import Y


int
float
complex

f = 12
j = 6.0
k = 1j
print(type(f))
print(type(j))
print(type(k))

## int

r = 67
h = -67
m = 676767676767676676767676
print(type(r))
print(type(h))
print(type(m))

## float

t = 12.20
l = -120.2
e = 10e10                                 # e indicates power
print(type(t))
print(type(l))
print(type(e))

## Complex

w = -9.9999j                                  # Complex are written only using j
y = 23j
n = 23.45j
print(type(w))
print(type(y))
print(type(n))

## Type Conversion

x = 12    # int
y = 2.88  # float
z = 12j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

## Random Number

import random
print(random.randrange(1,100))
