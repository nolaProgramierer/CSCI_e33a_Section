
pianos = {"Steinway": 85000, "Bechstein": 95000, "Steingräber": 105000, "Rönisch": 65000, "Blüthner": 92000}
list1 = [1, 2, 3, 4]

#----------------------------------------------
# Write a method to increase an argument by 10
def add_ten(num):
    return num + 10
print(add_ten(10))

#-----------------------------------------------
# Write the same method as a lambda

#-----------------------------------------------
# Write the above lambda without passing in an argument to the function variable

#-----------------------------------------------
# Write a lambda which sums 3 arguments

#-----------------------------------------------
# Write a lambda which multiplies the argument by 10

#-----------------------------------------------------
# Use it inside another function
# Insert a lambda function inside another function, passing in
# an argument to the 'outer'function, then call the lambda passing
# in the argument to the lambda


#---------------------------------------------------
#Finding expensive pianos conventional loops
def expensive_piano(list):
    result = []
    for piano in list:
        if list[piano] > 100000:
            result.append(piano)      
    return result
print(expensive_piano(pianos))

# Write the above function using a lambda

#-----------------------------------------------------------------------
cars1 = {"Ford": 25000, "Chevy": 35000, "Dodge": 37500}

def increase_price(car_list):
    result = []
    for car in car_list:
        new_price = "${:.2f}".format((car_list[car] * .15) + car_list[car])
        result.append(new_price)
    return result
print(increase_price(cars1))

#Write the above function as a lambda


# Formatting currency
two = 2
print(f"${two:.2f}")
print("${:.2f}".format(two))