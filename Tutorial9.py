# Python Data Types

## Built-in Data Types

'''
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
'''

## Getting the Data Type

x = 'SARAN'
print(type(x))  

## Setting the Data Type

a = "Hello World"	
b = 20	
c = 20.5		
d = 1j	
e = ["apple", "banana", "cherry"]		
f = ("apple", "banana", "cherry")		
g = range(6)		
h = {"name" : "John", "age" : 36}	
i = {"apple", "banana", "cherry"}	
j = frozenset({"apple", "banana", "cherry"})		
k = True		
l = b"Hello"		
m = bytearray(5)		
n = memoryview(bytes(5))	
o = None
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(type(j))
print(type(k))
print(type(l))
print(type(m))
print(type(n))
print(type(o))

## Setting the Specific Data Type

a = str("Hello World")	
b = int(20)
c = float(20.5)	
d = complex(1j)	
e = list(["apple", "banana", "cherry"])		
f = tuple(("apple", "banana", "cherry"))
g = range(6)		
h = dict({"name" : "John", "age" : 36})
i = set({"apple", "banana", "cherry"})	
j = frozenset({"apple", "banana", "cherry"})		
k = bool(True)	
l = bytes(5)
m = bytearray(5)		
n = memoryview(bytes(5))	
o = None
print(a)
print(type(a))  
print(b)
print(type(b))
print(c)
print(type(c))
print(d)
print(type(d))
print(e)
print(type(e))
print(f)
print(type(f))
print(g)
print(type(g))
print(h)
print(type(h))
print(i)
print(type(i))
print(j)
print(type(j))
print(k)
print(type(k))
print(l)
print(type(l))
print(m)
print(type(m))
print(n)
print(type(n))
print(o)
