# Task 1
def fact(n):
    ans = 1
    while(n>0):
        if n == 1:
            print(n,end=" ")
        else:
            print(n,'X',end= " ")
        ans = ans * n
        n = n - 1
    
    return ans

num = 6
print(":",fact(num))

# Task 2
from math import *

def mathop(n):
    print("Sqaure Root:",sqrt(n))
    print("Logarithm is ",log(n,e))
    n = radians(n)
    print("Sine of number in radians is ",sin(n))

    return n

usr_inp = input("Please Enter a number:")
usr_inp = int(usr_inp)

mathop(usr_inp)