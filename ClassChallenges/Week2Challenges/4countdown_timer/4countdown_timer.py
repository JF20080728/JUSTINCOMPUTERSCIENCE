#-----------------------------------------------------------------------------
# Name:         Even_Number_skipper
# Purpose:     write a program that prints numbers from 1 to 10 but skips even numbers
# Author:      Justin
# Created:     20-March-2025
#-----------------------------------------------------------------------------



number= 10 #start countdown

while number > 0: #loop if number is greater than 0
    print(number) #display the countdown number
    number -= 1 #decrease number by 1 in the countdown

    user = input("enter to quit or press enter: ") #prompt the user for input
    if user == "stop": #if user enteres stop
        print("countdown discontinued") #lets user know code is stopped
        break #breaks the code and everything is stopped

if number == 0: # countdown completed
    print("countdown finished") #tells the user that the countdown is done