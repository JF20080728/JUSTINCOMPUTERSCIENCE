#-----------------------------------------------------------------------------
# Name:       Temperature Advice
# Purpose:     To provide information  that asks the user for the current temperature and suggests whether they should wear a jacket, short-sleeves, or stay indoors.
# Author:      Justin.F
# Created:     4-March-2025
#-----------------------------------------------------------------------------


TEMP = int(input("enter your temperature in Celsius: "))

if TEMP  <10:
    print("it's cold outside. Wear a jacket!")
elif TEMP <=25 and TEMP >= 10:
    print("It's a nice day. Wear short-sleeves!")
elif TEMP >25 :
    print("It's hot outside. Stay cool!")