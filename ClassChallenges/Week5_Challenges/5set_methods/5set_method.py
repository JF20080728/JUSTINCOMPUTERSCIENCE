#-----------------------------------------------------------------------------
# Name:        Set_Methods
# Purpose:     Demonstrate various set methods
# Author:      Justin
# Created:     11-April-2025
#-----------------------------------------------------------------------------


#Create a set
data = {10, 20, 30, 40, 50}

#Copy the set using .copy()
data_copy = data.copy()
print("Copy:", data_copy) #print the copy

#Use .pop() to remove a random element
data.pop()  # Removes and returns a random element (sets are unordered)
print("After pop:", data) #print the set

#Use .clear() to empty the set
data.clear()
print("After clear:", data) #print the set
