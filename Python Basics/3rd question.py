""" Display first ten tables. Print a table in single line and move to next line"""
for i in range(1,11):
    for j in range(1,10):
        print(i*j,end = ",")
    print(i*(j+1))
    
