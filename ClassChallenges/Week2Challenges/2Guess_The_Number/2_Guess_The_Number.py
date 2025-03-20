#-----------------------------------------------------------------------------
# Name:         Guess the Number
# Purpose:     Write a program that asks the user for a number and calculate the sum of all numbers from 1 to the given number using a for loop
# Author:      Justin.F
# Created:     19-March-2025
#-----------------------------------------------------------------------------


import random
random.randint(1,11)
while True :      #makes the code so it asks the user again
    number = int(input("Guess a number between 1 and 10: "))
    if number == random.randint(1,11):
        print("good guess")
        exit()
    else:
        print("sorry, you didn't guess a number correctly, please try again and better luck next time")
