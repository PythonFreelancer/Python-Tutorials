# Python - Format - Strings

## String Format

'''
age = 40
txt = 'My Father Age is '+36            !Wrong!
print(txt)
'''

from xxlimited import foo


age = 40 
txt = 'My Father Age is {}' 
print(txt.format(age))

food1 = 2
food2 = 1
food3 = 1
orders = 'I want {} Burgers , {} plate Chicken and {} plate Biriyani.'
print(orders.format(food1,food2,food3))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
