a = [1, 2, 3]
b = [4, 5, 6]

composers = ["Beethoven", "Ravel", "Brahms", "Debussy", "Mahler", "Bruckner", "Mozart", "Bach", "Stravinsky"]

cars = [
    {"brand": "BMW", "trim": "328i", "color": "gray", "price": 38900},
     {"brand": "Mercedes", "trim": "350E", "color": "white", "price": 89000},
      {"brand": "Porsche", "trim": "911", "color": "orange", "price": 95000},
       {"brand": "Kia", "trim": "Sorento", "color": "blue", "price": 30900},
        {"brand": "Toyota", "trim": "Sienna", "color": "gray", "price": 51200},
]

#-----------------------------------------------------------------------------
# 1) Find length of composers list
l = len(composers)
print(l)

#------------------------------
# 2) Concatenate list a and list b
c = a + b
print(c)

#------------------------------
# 3) Instantiate a list of 3 piano brands 2 different ways(doesn't have to be pianos!)
my_faves = list(("Steinway","Bösendorfer", "Bechstein"))
my_faves1 =["Steinway","Bösendorfer", "Bechstein"]
print(my_faves)
print(my_faves1)

#------------------------------
# 4) Add an item to the list you just instantiated
my_faves.append("Baldwin")
print(my_faves)

#------------------------------
# 5)
# a) Return a list with Ravel & Brahms
s = composers[1:3]
print(s)

# b) Return a list with Beethoven, Ravel, Brahms, Debussy, & Mahler
s1 = composers[:5]
# c) Return a list with Mozart, Bach, & Stravinsky
s2 = composers[6:]
# d) Return a list with Ravel and Debussy
s3 = composers[1:4:2]
# e) Reverse the list
s4 = composers[::-1]
# f) Return a list Mozart & Bach


print(s)
print(s1)
print(s2)
print(s3)
# print(s5)
#------------------------------
# 6) 
# a) Make a list out of the words in the sentence "I love working in python!"
# b) Make a list out of the letters in the phrase "L-O-L"

my_str = "I love working in python!"
str_list = my_str.split()
my_str1 = "L-O-L"
str_list1 = my_str1.split("-")
print(str_list)
print(str_list1)
#------------------------------
# 7)
# Traverse the composer list and print them to the screen
def list_composers(l):
    for item in l:
        print(item)
list_composers(composers)

#------------------------------
# 8)
# Traverse the car list and print the dictionaries to the screen
def show_objs(objArr):
    for obj in objArr:
        print(obj)
show_objs(cars)

#------------------------------
# 9)
# Return the sum of the list 'b' (reduce)
total = sum(b)
print(total)

#------------------------------
# 10)
# Return a list of the composers, but lower case (map)
def to_lower_case(comps):
    result = []
    for comp in comps:
        result.append(comp.lower())
    return result
print(to_lower_case(composers))

#------------------------------
# 11)
# Return a list of the composers that being with the letter 'b'
def composers_with_b(comps):
    result = []
    for comp in comps:
        if comp[0] == "B":
            result.append(comp)
    return result
print(composers_with_b(composers))


