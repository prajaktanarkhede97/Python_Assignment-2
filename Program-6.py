# Write a program which accept one number and display below pattern.
# Input : 5
# Output : * * * * *
#          * * * *
#          * * *
#          * *
#          *

def printpattern(x):
    
    for i in range(x):
        for j in range(i+1):
            print("*", end = "")
        print()
        
x = (int(input("Enter value of x")))
        
printpattern(x)
