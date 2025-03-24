#-----------------------------------------------------------------------------
# Name:         Guess the Number
# Purpose:     Write a program that asks the user for a number and calculate the sum of all numbers from 1 to the given number using a for loop
# Author:      Justin
# Created:     19-March-2025
#-----------------------------------------------------------------------------


import random #import random to create random numbers

random.randint(1,11) #creates a number from 1 to 10

while True :      #makes the code so it asks the user again repeatedly
    number = int(input("Guess a number between 1 and 10: ")) #promp the user to enter a number
    if number == random.randint(1,11): #identifies if the number guess is correct
        print("good guess") #print a congrats message
        exit()
    else:
        print("sorry, you didn't guess a number correctly, please try again and better luck next time") #wrong guess so the code will continue to ask the user
