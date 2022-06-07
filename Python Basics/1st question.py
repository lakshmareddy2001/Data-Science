a = float(input("Enter the Anuual Salary of the Employee"))
b = float(input("Enter the Annaul HRA salary of the Employee"))
c = float(input("Enter the Deductions of the monthly salary"))
if(c>80000):
    c = 80000
a = a- b- c
if(a<300000):
    print(0)
elif(a<600000):
    print(a*0.1)
elif(a<1000000):
    print(a*0.15)
else:
    print(a*0.2)
