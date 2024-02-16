import math

def variable(a, b):
    c = math.sqrt (a**2 + b**2)
    return c

a = int(input('Enter the value of a: '))
b = int(input('Enter the value of b: '))

c = variable(a,b)

print('The square root is', c)





