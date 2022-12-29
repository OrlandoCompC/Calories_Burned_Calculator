"""
Assignment No.: 1
Course: PROG12974
Submission date: Sep 29 2022
Developed by: Orlando Companioni
Date created: sep 26 2022

This program calculates the amount of calories burned after the
user inputs details about the exercise and themselves
"""


#input
#get inputs from the user about their exercise and personal information
gender=input("Enter your gender(M=Male,F=Female): ")
user_age=int(input("Enter your age:  "))
weight=int(input("Enter your weight(lbs): "))
heart_rate=int(input("Enter your heart(BPM): "))
exerciseDuration=int(input("Enter the duration of the exercise(in mins): "))

#process
#check against my conditions and then process the math

male="M"
if gender==male:
    total_cal=((user_age*0.2017)-(weight*0.09036)+(heart_rate*0.6309) -\
55.0969)*exerciseDuration/4.184
else:
    total_cal = ((user_age*0.074)-(weight*0.05741)+(heart_rate*0.4472) -\
20.4022)*exerciseDuration/4.184

#output
#depending on the condition output the math
print(f"Enter your gender (M=Male,F=Female):\n{gender}")
print(f"Enter your age:\n{user_age}")
print(f"Enter your weight (lbs):\n{weight}")
print(f"Enter your heart rate (BPM):\n{heart_rate}")
print(f"Enter the duration of exercise (in mins):\n{exerciseDuration}")
print(f"You burned {total_cal:.2f} calories.")
print(f"Calories Burned calculator by:Orlando Companioni, 99145470849")




