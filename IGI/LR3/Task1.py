import math

def my_arcsin(x, eps):
    sum = 0
    elem = x
    n=0
    while n<500 and abs(elem) > eps:
        elem =  (math.factorial(2 * n) / (2 ** (2 * n) * (math.factorial(n) ** 2))) * (x ** (2 * n + 1) / (2 * n + 1))
        sum += elem
        n+=1
    return sum, n

x=float(input())
eps=float(input())
my_res, n =my_arcsin(x,eps)
print(x,"|",n,"|",my_res,"|",math.asin(x),"|",eps)
