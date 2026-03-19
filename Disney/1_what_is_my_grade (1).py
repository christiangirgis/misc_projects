"""
Write a program that displays the letter grade for a 
    particular numerical grade. For example, if the user says
    that their grade is 85, the program output should say
    "You have a B!". The initial variable for grade has 
    been created for you below.

Use the following guidlines to create your gradebook: 
NOTE DIFFERENT FROM IN CLASS!!!
    A is any value greater than or equal to 87
    B is any value greater than or equal to 78, but below 87
    C is any value greater than or equal to 69, but below 78
    D is any value greater than or equal to 55, but below 69
    F is any value lower than (but not equal to) 55


"""

grade = int(input("What is your numerical grade? "))

if grade < 55 :
    print("F")
elif grade >= 55 and grade < 69 :
    print("d")
elif grade >= 69 and grade < 78 : 
    print("c")
elif grade >= 78 and grade < 87 :
    print("b")
elif grade >= 87 :
    print("a")

