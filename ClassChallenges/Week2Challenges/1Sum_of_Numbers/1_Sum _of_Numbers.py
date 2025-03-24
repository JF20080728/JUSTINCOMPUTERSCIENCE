#-----------------------------------------------------------------------------
# Name:         Sum of Numbers
# Purpose:     Write a program that asks the user for a number and calculate the sum of all numbers from 1 to the given number using a for loop
# Author:      Justin
# Created:     18-March-2025
#-----------------------------------------------------------------------------


number = int(input("Enter a number: ")) #prompt the user to enter a number
total = 0 #start a variable to store the sum
for i in range (1, number+1): #loop from 1 to number
    total = total + i #add current number i to the sum
print("the sum of numbers adding between 1 and", number, "is", total) #prints the sum of the number