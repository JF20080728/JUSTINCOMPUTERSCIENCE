#-----------------------------------------------------------------------------
# Name:         Student Grading System
# Purpose:     To provide information that asks for a student's score and then provides a grade based on the score.
# Author:      Justin Fung
# Created:     4-March-2025
#-----------------------------------------------------------------------------

GRADES= int(input("what is your grading score "))
if GRADES >= 90 and GRADES <= 100:
    print("Your grade is a")
elif GRADES >= 80 and GRADES <= 89:
    print("Your grade is d")
elif GRADES >= 70 and GRADES <= 79:
    print("Your grade is c")
elif GRADES >= 60 and GRADES <= 69 :
    print("Your grade is d")
elif GRADES < 60:
    print("Your grade is f")
else:
    print("please add a number between 0-100")
