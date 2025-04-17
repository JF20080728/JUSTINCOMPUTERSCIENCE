#-----------------------------------------------------------------------------
# Name:        Subsets_supersets
# Purpose:     Work with subsets and supersets.
# Author:      Justin
# Created:     11-April-2025
#-----------------------------------------------------------------------------

#Create two sets
set_a = {1, 2, 3, 4, 5}
set_b = {2, 3, 4}

#Check if set_b is a subset of set_a and print the result
is_subset = set_b.issubset(set_a)
print(is_subset)  # True

#Check if set_a is a superset of set_b and print the result
is_superset = set_a.issuperset(set_b)
print(is_superset)  # True
