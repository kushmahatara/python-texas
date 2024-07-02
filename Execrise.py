# Exercise of Conditional Statement
# Task 1
# Write a python program to display students grade
# First ask user score using input method
# Check if user score above 90, print your grade is A
# Check if user score above 75, print your grade is B
# Check if user score above 65, print your grade is C
# Check if user score below 40, print your grade is Fail

score = int(input("enter your score:"))

if (score > 90):
    print("A")
elif (score > 75 ):
    print("B")
elif (score > 65):
    print("C")
elif (score > 40):
    print("Fail")

#write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria:

amt=0
nu=int(input("Enter number of electric unit"))
if nu<=100:
    amt=0
    if nu>100 and nu <=200:
        amt=(nu-100)*5
        if nu>200:
            amt=500+(nu-200)*10
            print("Amount to pay:",amt)
            
