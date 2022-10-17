# Python Booleans

## Boolean Values

print(100>200)
print(100<200)
print(100==200)

x = 100
y = 200
if x>y:
    print('x is greater than y')
else:
    print('x is not greater than y')

## Evaluate Values and Variables

print(bool(24))
print(bool('Saran'))


r = 'Saran'
j = 200
print(bool(r))
print(bool(j))

## Most Values are True

# These all are True:

print(bool('Saran'))
print(bool(354))
print(bool(['Kawasaki','Pulsar','Apache']))

## Some Values are False

# These all are False:
 
print(bool(False))
print(bool([]))
print(bool(''))
print(bool(()))
print(bool({}))
print(bool(0))

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

## Functions can Return a Boolean

def myfunction():
    return True
print(myfunction())

def funct():
    return True

if funct():
    print('Yes')
else:
    print('No')
w = 500
print(isinstance(w,int))
