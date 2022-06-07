"""
    Write a Python Script to find a prime number or not, even or odd, divisible by 5 or not, and also find the sum of first n natural numbers till n.
"""

def Prime(n):
    flag = True
    for i in range(2,n//2):
        if(n%i == 0):
            flag = False
            break
    if(flag):
        print("Yes, It is a prime Number")
    else:
        print("No, It is not a Prime Number")
def EvenOrOdd(n):
    if(n%2 == 0):
        print("Yes, It is Even")
    else:
        print("No, It is not Even")
def Divisible5(n):
    if(n%5 == 0):
        print("Yes, It is Divisible by 5")
    else:
        print("No, It is not Divisible by 5")
    
a = int(input("Enter a number"))
Prime(a)
EvenOrOdd(a)
Divisible5(a)
print(n*(n+1)//2)
