#-----------------------------------------------------------------------------
# Name:        Tuple_Operation_and_Count
# Purpose:     Create a tuple with repeated values
# Author:      Justin
# Created:     8-April-2025
#-----------------------------------------------------------------------------

Fruits =("apple", "banana", "apple", "cherry", "banana", "apple") #create a tuple containing a list of fruits
print(Fruits) #print the list of fruits
print("this is your current list of fruits") # telling the user the fruits
print("please enter a fruit from the list") # ask the user to enter a fruit name
user_ask = input("enter your fruit name: ") # ask the user to enter a fruit name
count = Fruits.count(user_ask) # count the number of times the fruit shows up in the tuple
print(count) # print the number of times the fruit shows in the tuple
