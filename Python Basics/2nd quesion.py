""" Write a python program to create a data base having 10 employee data each employee information should have 
            Student Roll No
            Name of the Student
            Marks in SSC
            Marks in Intermediate
            CGPA util the current Semester
            Most preffered programing Language
            Carrier Option
 """

students = {501:["Lakshma Reddy",9.5,962,8.85,"Python","IT Job"],
            502:["Sujith Kumar Reddy",9.7,962,8.85,"JAVA","IT Job"],
            503:["Maha Lakshmi",9.3,962,8.85,"Python","Masters"],
            504:["Dheeraj",9.9,962,8.85,"Python","IT Job"],
            505:["Bhargav",9.8,962,8.85,"C++","IT Job"],
            506:["Akhil",9.7,962,8.85,"Python","Masters"],
            507:["Midhun",9.9,962,8.85,"Python","IT Job"],
            508:["Ajay",9.6,962,8.85,"C#","IT Job"],
            509:["Karthik",10,962,8.85,"Python","Masters"],
            510:["Amith",8.8,962,8.85,"Java","Masters"],
            }
for i in students:
            print("The details of the Student " + i + " are " + students[i])
