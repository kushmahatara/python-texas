# for loop with else example
'''
fruits = ["apple", "banana", "grapes"]
for index in range(len(fruits)):
    print(fruits[index])
else:
    print(len(fruits))

#while loop example
count = 0
while (count < 3):
    # count = count + 1 
    print ("Helo Programming")
'''
#nested for loop example
# adj = ["red", "big", "tasty"]
# fruits = ["apple", "grapes", "cherry"]

# for x in adj:
#     for y in fruits:
#         print(x,'\t',y, '\n')

# for i in range (1, 5):
#     for j in range (i):
#         print (i, end='')
#     print()

i = 1 
while i < 10:
    j = i
    while j < 10:
        print(f"{j}", end=" ")
        j = j + 1
    print (" ")
    i = i + 1
print("Complete")