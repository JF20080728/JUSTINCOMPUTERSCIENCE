#-----------------------------------------------------------------------------
# Name:         Even_Number_skipper
# Purpose:     write a program that prints numbers from 1 to 10 but skips even numbers
# Author:      Justin.F
# Created:     20-March-2025
#-----------------------------------------------------------------------------


for i in range(1, 11):
    if i  % 2 == 0:
        print(i)
        continue