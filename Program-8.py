# Write a program which accept one number and display below pattern.
#Input : 5
#Output : 1
#         1 2
#         1 2 3
#         1 2 3 4
#         1 2 3 4 5

def printpattern(x):
    for i in range (x):
        for j in range (i+1):
            print(j+1 , end =" ")
        print()
x =(int(input("Enter value of x")))
printpattern(x)
