
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
cheap_cars = [car for car in cars if car["price"] < 40000]
print(cheap_cars)

# All cars capitalized whose price is under 40000
cheap_car_brands = [car["brand"].upper() for car in cars if car["price"] < 40000]
print(cheap_car_brands)

#Find most expensive car brand
def find_expensive_car_brand(cars):
    temp_price = 0
    for obj in cars:
        if obj["price"] > temp_price:
            temp_price = obj["price"]
            best_obj = obj
    return best_obj["brand"]

print(find_expensive_car_brand(cars))

#------------------------------------------------------

pianos = {"Steinway": 85000, "Bechstein": 95000, "Steingräber": 105000, "Rönisch": 65000, "Blüthner": 92000}
my_pianos = []

# 1 Returns a list of dictionary keys
piano_list =[]
for piano in pianos:
    piano_list.append(piano)
print(f"Dictionary keys: {piano_list}")

# 2 Return a list of dictionary keys
# Return a list of all piano brands
piano_list1 = []
for piano in pianos.keys():
    piano_list1.append(piano)
print(f"Dictionary keys: {piano_list1}")

# 3 Iterate through all the values
# Return a list of all piano prices
piano_list2 = []
for piano in pianos.values():
    piano_list2.append(piano)
print(f"Dictionary values: {piano_list2}")

#4 Iterate through all the values
# Return a list of all piano prices (most common method)
piano_list3 = []
for piano in pianos:
    piano_list3.append(pianos[piano])
print(f"Dictionary values: {piano_list3}")

# 5 Print key-value pairs as tuples
piano_items = pianos.items()
print(piano_items)

# 6 Return all key, value pairs without using items()
for piano in pianos:
    print(piano, ":", pianos[piano])

#7 Unpacking dictionary keys into a list
keys = [*pianos]
print(f"Unpacked dictionary keys: {keys}")

#8 Unpacking dictionary values into a list
values = [*pianos.values()]
print(f"Unpacked dictionary values: {values}")

#9 Unpacking dictionary items into a list
items = [*pianos.items()]
print(f"Unpacked dictionary items: {items}")

# Here the piano brand names in curly brackets are replacement fields.
# Anything outside of the brackets are part of the outputted string

# Format method has 2 args, positional args and keyword args
# Positional arguments are inserted iinto the template in place of 
# numbered replacement fields
# Keyword arguments are inserted into the template string in place of keyword
# replacement fields with the same name.
# Here the value of the keyword args take the place of the replacements fields
values1 = '{Steinway}-{Bechstein}-{Steingräber}-{Rönisch}'.format(**pianos)
print(values1)


# Find list of pianos above 85000
expensive_piano_list = []
for piano in pianos:
    if pianos[piano] > 85000:
        expensive_piano_list.append(piano)
print(expensive_piano_list)

# Find list of pianos above 85000
exp_piano_list = []
for brand, price in pianos.items():
    if price > 85000:
        exp_piano_list.append(brand)
print(exp_piano_list)


# Can be used with any iterable
exp_piano_list = [key for key, val in pianos.items() if val > 85000]
print(f"Using list comprehension: {exp_piano_list}")

exp_piano_list = [piano for piano in pianos if pianos[piano] > 85000]
print(exp_piano_list)

# Find the brand name of the most expensive piano
most_valuable_piano = [key for key, value in pianos.items() if value == max(pianos.values())]
print(most_valuable_piano)

# Find piano brand without an umlaut
# umlauts = "[ü]"
import re
no_umlaut_pianos = []
for brand, price in pianos.items():
    if not re.search("[üäö]", brand):
        no_umlaut_pianos.append(brand)
print(no_umlaut_pianos)

# Using a List comprehension
no_umlaut_pianos = [brand for brand, val in pianos.items() if not re.search("[üäö]", brand)]
print(no_umlaut_pianos)

#Don't do this!
print([brand for brand, val in pianos.items() if not re.search("[üäö]", brand)])

    
