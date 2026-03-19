"""
Taken from "Starting Out With Python" book from Gaddis

Write a program that asks the user for a number in the
    range of 1 through 7. The program should display the 
    corresponding day of the week, whter 1 = Monday, 2=Tuesday
    3=Wednesday, 4=thursday, 5=Friday, 6 = Saturday, 7 = Sunday
    The program should display an error message if the user enters
    a number that is outside the range of 1 through 7.


YOU MUST TURN IN A FLOW CHART TO RECEIVE FULL CREDIT - start with
    the flow chart, it will help you with your program
"""


number = int(input("Please enter a number 1-7: "))

if number == 1:
    day = "monday"
elif number == 2:
    day = "tuesday"
elif number == 3 : 
    day = "wednesday"
elif number == 4 :
    day = "thursday"
elif number == 5 : 
    day = "friday"
elif number == 6 : 
    day = "saturday"
elif number == 7 :
    day = "sunday"





