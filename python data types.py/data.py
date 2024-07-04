# index
# myString = "PythonProgramming"
# print(myString)
# print(myString[0])
# print(myString[0:5])
# print(myString[::-1])

# concatenation
# myString = "Hello" + "World"
# print(myString)

# repetition
# myString = "hello \n " * 4
# print(myString)

# Updating character
myString = "Hello, I'am AI"
print("Initial myString: ")
print(myString)

# deleting character
del myString
print("\nDeleting entire String : ")


# list1 = list(myString)
# list1[2] = 'p'
# myString2 = "". join(list1)
# print("\nUpdating character in 2 nd index: ")
# print(myString2)


# String formating
age = 23
text = f"my age is {age}"
print(text)

# default order string
my_String = "{} {} {}".format("Python", "Java", "C++") 
print( "Default order: ")
print(my_String)

# tuple
Name = ("Manish", "suraj", "bebek")
print(Name)

# unpacking tuple
Name = ("Manish", "suraj", "bebek")
(Handsome, genius, talent) = Name
print(Handsome)
print(genius)
print(talent)

# UNPACKING TUPLE WITH*
Name = ("Manish", "suraj", "bebek", "kush")
(Handsome, genius, *talent) = Name
print(Handsome)
print(genius)
print(talent)

# dictionary
Nosier = {
    "Manish" : "most talk person",
    "Suraj"  : "few noise creater",
    "Bibek"  : "Lazy",
    "Kanchan" : "most breakup person"
    }

print(Nosier)

# add dictionary
Nosier = {
    "Manish" : "most talk person",
    "Suraj"  : "few noise creater",
    "Bibek"  : "Lazy",
    "Kanchan" : "most breakup person"
    }

Nosier["Kush"] = "Good Boy"
print(Nosier)

# update dictionary
Nosier = {
    "Manish" : "most talk person",
    "Suraj"  : "few noise creater",
    "Bibek"  : "Lazy",
    "Kanchan" : "most breakup person"
    }
Nosier.update({"mielage":8})
print(Nosier)

# Remove dictionary
Nosier = {
    "Manish" : "most talk person",
    "Suraj"  : "few noise creater",
    "Bibek"  : "Lazy",
    "Kanchan" : "most breakup person"
    }
Nosier.pop("Bibek")
print(Nosier)

# popitem dictionary
# Nosier = {
#     "Manish" : "most talk person",
#     "Suraj"  : "few noise creater",
#     "Bibek"  : "Lazy",
#     "Kanchan" : "most breakup person"
#     }
# Nosier.popitem()
# print(Nosier)

# for loop 
# Song = {
#     "maiti ghar" : "Nepali Song",
#     "Venonm" : "Eminem",
#     "Rap God" : "Drake"
# }
# for x in Song:
#     print(x)
    
# for x in Song.values():
#     print(x,x)
    
# for x, y in Song.items():
#     print(x,y)

# for Nested 
# politics = {
#     "MLA":{
#         "name" : "Kp oli",
#         "age" : "60"
#     },
#     "Army" :{
#         "name" : "prachanda",
#         "age"  : "60"
#     },
#     "kanrace" :{
#         "name" : "rabi lamachane",
#         "age" : "50"
#     }
# }
# print(politics["MLA"],["name"])

#  dictionary items 
# Nepali ={
#     "name" : "Kush",
#     "age" :"20",
#     "Hobby" : "Singer",
#     "song" : ["HERO","OneLove","RapGod"]
# }
# print(Nepali)
# print(Nepali["song"][1])

# zip function?
list1 = [1,2,3]
list2 = ['a','b','c']
zipped = zip(list1, list2)
print(list(zipped))

# reversed function
my_list = [1,2,3,4,5,6]
reversed_list = list(reversed(list(my_list)))
print(reversed_list)

# with arguments
def combine(fname, lname):
    print(fname +" "+lname)

# calling the function
combine("manish", "shankar")

#with parameters
def combineNames (fname="manish", lname="shankar"):
    print(fname + "" + laname)

# calling the function
combineNames()



