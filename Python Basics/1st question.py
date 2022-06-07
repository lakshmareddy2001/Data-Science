"""Calcultate the income tax to be paid by an employee taking his annual income HRA and other deductions as input. Maximum deductions must not be greater than 80000.
    Follow the conditions below
    below 300000 - 0% of tax
    below 600000 - 10% of tax
    below 1000000 - 15% of tax
    above 1000000 - 20% of tax
"""
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
