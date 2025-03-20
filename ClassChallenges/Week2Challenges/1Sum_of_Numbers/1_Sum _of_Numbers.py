#-----------------------------------------------------------------------------
# Name:         Sum of Numbers
# Purpose:     Write a program that asks the user for a number and calculate the sum of all numbers from 1 to the given number using a for loop
# Author:      Justin.F
# Created:     18-March-2025
#-----------------------------------------------------------------------------


number = int(input("Enter a number: "))
total = 0
for i in range (1, number+1):
    total = total + i
print("the sum of numbers adding between 1 and", number, "is", total)