# Write a program which accept one number from user and return its factorial.

def Factorial(n):
    i=1
    while n > 0:
        i = i * n
        n = n - 1
    return i
    
n = (int(input("Enter value of n")))
Factorial(n)
