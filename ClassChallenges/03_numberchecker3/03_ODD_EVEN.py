#-----------------------------------------------------------------------------
# Name:       Even or Odd Number Checker
# Purpose:     To provide information  that asks the user for a number and then tells them if the number is even or odd.
# Author:      Justin
# Created:     4-March-2025
#-----------------------------------------------------------------------------



number= int(input("Think of a number and enter it "))

if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
