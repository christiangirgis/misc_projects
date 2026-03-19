"""
Taken from "Starting Out With Python" book from Gaddis

Write a program that asks the user to enter a person's age. 
The program output should display a message indicating
whether the person is an infant, a child, or an adult.

These are the guidelines:
    If the person is 1 yr old or less, he or she is an infant
    If the person is older than 1 yr, but younger than 13 yr, 
        he or she is a child
    If the person is at least 13 yrs old, but less than 20 yrs
        old, he or she is a teenager
    If the person is at least 20 yrs old, he or she is an adult

YOU MUST TURN IN A FLOW CHART TO RECEIVE FULL CREDIT - start with
    the flow chart, it will help you with your program
"""
age= int(input("please enter an age") )

if age <= 1:
    print("infant")
elif age >= 1 and age <= 13:
    print("child")
elif age >= 13 and age < 20:
    print("teenager")
elif age >= 20:
    print("adult")




