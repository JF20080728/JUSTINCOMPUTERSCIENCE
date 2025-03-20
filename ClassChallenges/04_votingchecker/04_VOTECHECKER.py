#-----------------------------------------------------------------------------
# Name:      Voting Eligibility Checker
# Purpose:     To provide information that checks if a person is eligible to vote based on their age.
# Author:      Justin.F
# Created:     4-March-2025
#-----------------------------------------------------------------------------



AGE = int(input("Enter your age "))
if AGE < 18:
    print("you are unable to vote you are too young")
if AGE >= 18:
    print("You are eligible to vote")