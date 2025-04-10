#-----------------------------------------------------------------------------
# Name:        Create_a_grocery_list_and_add_items
# Purpose:     Create a list of groceries and then add new items to the list
# Author:      Justin
# Created:     27-March-2025
#-----------------------------------------------------------------------------

list= ['apples', 'bread', 'milk', 'egg'] #create the list with items
print("this is your current grocery list") #informing the user of the message
print(list) #print the current list
print("adding cheese and tomatoes to the current list") #telling the user that the list is changing and adding more items to the lists
list.append("cheese") #adding cheese to the list
list.append("tomatoes") #adding tomatoes to the list
print("this is your new and updated grocery list") #telling the user that the list has changed
print(list) #print the new and updated list