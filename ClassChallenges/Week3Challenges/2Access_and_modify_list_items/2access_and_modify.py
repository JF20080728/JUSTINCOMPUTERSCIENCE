#-----------------------------------------------------------------------------
# Name:        Modifying List_items
# Purpose:     Modify a grocery list by changing an existing item.
# Author:      Justin
# Created:     1-April-2025
#-----------------------------------------------------------------------------

print("This is your first grocery list") #start the code by telling the user the first grocery list
grocerylist = ['apples', 'bananas', 'carrots', 'milk', 'bread'] #create a variable for a grocery list
print(grocerylist) #print the unedited list


print("This is your new updated grocery list ") #tell the user the grocery list has changed
grocerylist.insert(2,"grapes")  #insert grapes from the grocery list
grocerylist.remove("bananas") #remove banana from the grocery list
print(grocerylist) #print the changed list


print("This is your last updated grocery list ") #inform the user that its the last updated list
grocerylist.insert( 3, "chips") #add chips as an item to the 3rd list
grocerylist.remove("carrots") #remove carrots from the current list
print(grocerylist) #print the final updated grocery list
