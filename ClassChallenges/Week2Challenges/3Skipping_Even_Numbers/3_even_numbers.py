#-----------------------------------------------------------------------------
# Name:         Even_Number_skipper
# Purpose:     write a program that prints numbers from 1 to 10 but skips even numbers
# Author:      Justin
# Created:     20-March-2025
#-----------------------------------------------------------------------------


for number in range(1, 11): #loops numbers from 1 to 10
    if number % 2 == 0: #identifies if the number is even
        continue #skip the loop for even number
    print(number) #print number if its odd
