#-----------------------------------------------------------------------------
# Name:        Set_Operations
# Purpose:     Combine and compare sets using set operations.
# Author:      Justin
# Created:     11-April-2025
#-----------------------------------------------------------------------------

# Create two sets
set1 = {1, 2, 3, 4}  # First set containing integers
set2 = {3, 4, 5, 6}  # Second set containing integers
# Step 2: Perform set operations
# Union: Combines all unique elements from both sets
union_set = set1 | set2
# Intersection: Finds common elements between the two sets
intersection_set = set1 & set2
# Difference: Finds elements that are in set1 but not in set2
difference_set = set1 - set2
# Print the results of each operation
print("Union:", union_set)  # Output: Union: {1, 2, 3, 4, 5, 6}
print("Intersection:", intersection_set)  # Output: Intersection: {3, 4}
print("Difference:", difference_set)  # Output: Difference: {1, 2}
