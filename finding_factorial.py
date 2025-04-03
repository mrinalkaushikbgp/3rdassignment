#Program to factorial for a number given by the user
from math import factorial

x = int(input('Enter a number: '))
def fact(x):
    if x<2:
        return 1
    else:
        return x * factorial(x-1)
res = factorial(x)
print('Factorial of',x,'is:', res)

