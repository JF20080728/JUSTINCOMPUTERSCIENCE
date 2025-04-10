#-----------------------------------------------------------------------------
# Name:        Swap_values
# Purpose:     Allows swapping values easily using tuples
# Author:      Justin
# Created:     8-April-2025
#-----------------------------------------------------------------------------

number = int(input("enter a number ")) #take the first number as an input and transform it to an integer
number2 = int(input("enter another number ")) #take the second number from the input and make it into an integer
list1 = [number, number2] #store the numbers in a list
print(list1) #print the unchanged list
print("swapping the numbers") #telling the user that the numbers are switched
print(list1[1], list1[0]) # print the swapped list
