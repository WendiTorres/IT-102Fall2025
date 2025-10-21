#!/usr/bin/env python3
# example workign with Loops
#By Wendi

#First must gather if the day id good or bad Requires user input

question = input("Is today a good day? Please answer with Y or N: ").upper()

#Analyze value and print of yes it is (Yes today is a good day)

if question == 'Y':
    #Create a loop of 10 times saying Yes today is a good day (yes it is)
    number = 1
    while number < 11:
        print("Yes today is a good day")
        number += 1
elif question == 'N':
    print("Its okay, Tommorrow is another day ")
elif question == 'idk':
    print("That's okay")
else:
    print("Please enter a valid input of Y or N for yes or no")