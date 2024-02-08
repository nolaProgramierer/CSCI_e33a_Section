
cars = [
    {"brand": "BMW", "trim": "328i", "color": "gray", "price": 38900},
     {"brand": "Mercedes", "trim": "350E", "color": "white", "price": 89000},
      {"brand": "Porsche", "trim": "911", "color": "orange", "price": 95000},
       {"brand": "Kia", "trim": "Sorento", "color": "blue", "price": 30900},
        {"brand": "Toyota", "trim": "Sienna", "color": "gray", "price": 51200},
]

#Find orange car
def find_orange(obj_list):
    for obj in obj_list:
        if obj["color"] == "orange":
            print(obj)

find_orange(cars)

# Find cars that are less than $40000


# All cars capitalized whose price is under 40000


# Find most expensive car


#------------------------------------------------------

pianos = {"Steinway": 85000, "Bechstein": 95000, "Steingräber": 105000, "Rönisch": 65000, "Blüthner": 92000}
my_pianos = []

# 1 Returns a list of dictionary keys
piano_list =[]


# 2 Return a list of dictionary keys
# Return a list of all piano brands
piano_list1 = []

# 3 Iterate through all the values
# Return a list of all piano prices
piano_list2 = []


#4 Iterate through all the values
# Return a list of all piano prices (most common method)
piano_list3 = []

# 5 Print key-value pairs as tuples

# 6 Return all key, value pairs without using items()

#7 Unpacking dictionary keys into a list

#8 Unpacking dictionary values into a list

#9 Unpacking dictionary items into a list

#10 Find list of pianos above 85000

#11 Find list of pianos above 85000

#12 Render the above function using list comprehension

#13 Find the brand name of the most expensive piano

#14 Find piano brand without an umlaut
# umlauts = "[ü]"
import re
no_umlaut_pianos = []
for brand, price in pianos.items():
    if not re.search("[üäö]", brand):
        no_umlaut_pianos.append(brand)
print(no_umlaut_pianos)

#15 Using a List comprehension


    
