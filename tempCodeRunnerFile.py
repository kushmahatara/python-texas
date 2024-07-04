# Exercise of Conditional Statement
# Task 1
# Write a python program to display students grade
# First ask user score using input method
# Check if user score above 90, print your grade is A
# Check if user score above 75, print your grade is B
# Check if user score above 65, print your grade is C
# Check if user score below 40, print your grade is Fail

# score = int(input("enter your score:"))

# if (score > 90):
#     print("A")
# elif (score > 75 ):
#     print("B")
# elif (score > 65):
#     print("C")
# elif (score > 40):
#     print("Fail")

#write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria:

# amt=0
# nu=int(input("Enter number of electric unit"))
# if nu<=100:
#     amt=0
#     if nu>100 and nu <=200:
#         amt=(nu-100)*5
#         if nu>200:
#             amt=500+(nu-200)*10
#             print("Amount to pay:",amt)

# Write a program to print multiplication table of given number(accept number from user)
# Q1. Write a program to print multiplication table of a given number(accept number from user)
# eg. if user input 3
# 3 x 1 = 3
# 3 x 2 = 6 and so on

# number = int(input("Enter Your Number U Want Table: "))
# for i in range (1, 11):
#    result = number * i
#    print(f"{number} * {i} = {result}")

# Q2. Accept 10 numbers from user and display average of it.

# numbers = []
# for i in range (10):
#    num = int(input(f"Enter Number {i+1} : "))
#    numbers.append(num)
# avg = sum(numbers)/ len(numbers)
# print(f"The Sum of 10 Number:{avg}")

# Q3. Write a program to display numbers which is divisible by only 11 from 100 to 300.

# print("The number divible by 11 from 100 - 300 are :")
# for num in range (100, 300):
#    if num % 11 == 0:
#       print(num)

# single , double and triple line code 
# sid = 'I just love all girls'
# print('\nMy name sid. I love all texas girl')
# print(sid)

#INDEX
# print(input('choose the number'))
Girl1 = {
   'name':'smriti',
   'number':'5'
}
Girl2 = {
   'name':'pallavi',
   'number':'1'
}


Girl3 = {
   'name':'gracey',
   'number':'5'
}

for i in range (5):
   user_choose=input('choose the number ')
   print(user_choose)
   if user_choose==Girl1['number']:
      print(Girl1['name'],'love u')
   elif user_choose==Girl2:
      print(Girl2['name'],'love u')
   elif user_choose==Girl3:
      print(Girl3['name'],'love u')
      
else:
   print('noone love u pajii')


