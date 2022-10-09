# Python - Global Variables

## Global Variables

a='Python'

def myfunct():
    print('My Favorite Prgramming language' + a)

def myfunct1():
    a = 'is a Awesome Programming Language'
    print('Python' +a)

print(a+ 'is a Best Proramming Language')
myfunct1()
myfunct()

## The global Keyword

def funct():
    global a
    a='Python'

print(a +'Freelancer')
