import math
from check_input import check_input
#Make calculations for arcsin by custom fun and math lib function and print result
def task1():

    #Calculate custom arcsin
    def my_arcsin(x, eps):
        sum = x
        elem = x
        n=0
        while  abs(elem) > eps and n < 500:
            n+=1
            elem =  (math.factorial(2 * n) / ((2 ** (2 * n) * (math.factorial(n) ** 2))) * (x ** (2 * n + 1) / (2 * n + 1)))
            print(elem)
            sum += elem
            
        return sum, n
    
    while True:
        print("Enter the value of x (-1 to 1): ")
        x = check_input(float, "NO VALUE")  # Prompt the user to enter the value of 'x'
        if -1 <= x <= 1:
            break
        else:
            print("The value of x must be in the range from -1 to 1 inclusive.")
    while True:
        print("Enter precision eps: ")
        eps = check_input(float, "NO VALUE")  # Prompt the user to enter the precision 'eps'
        if eps <=0:
            print("Input error. The accuracy must be greater than 0!")
        else:
            break
    
     
    my_res, n = my_arcsin(x,eps)
    print(x,"|",n,"|",my_res,"|",math.asin(x),"|",eps)
