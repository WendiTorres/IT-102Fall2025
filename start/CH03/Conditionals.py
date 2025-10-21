#!/usr/bin/env python3
# example workign with conditionals
#By Wendi


#First must gather if the day id good or bad Requires user input

question = input("Is today a good day? Please answer with Y or N: ").upper()

#Analyze value and print of yes it is

if question == 'Y':
    print("Yes today is a good day")
elif question == 'N':
    print("Its okay, Tommorrow is another day ")
elif question == 'idk':
    print("That's okay")
else:
    print("Please enter a valid input of Y or N for yes or no")
        

