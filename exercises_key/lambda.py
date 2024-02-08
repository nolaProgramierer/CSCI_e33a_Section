# A lambda is a small anonymous function.
# It can take any number of arguments, but have only one expression
# Useful whenever you want to create a function that's only a single line

# lambda is a keyword defining the anonymous function
# argument is the placeholder
# expression is the code you want to execute in the lambda function

#A lambda function is a small anonymous function.

#A lambda function can take any number of arguments, but can only have one expression.
# Use it when the result is only needed for a short period of time

# Use lambda functions with iterables like filter and map
pianos = {"Steinway": 85000, "Bechstein": 95000, "Steingräber": 105000, "Rönisch": 65000, "Blüthner": 92000}
list1 = [1, 2, 3, 4]

#----------------------------------------------
def add_ten(num):
    return num + 10
print(add_ten(10))

#-----------------------------------------------
# The argument before the ":" is the argument
# The expression is after the ":"
x = lambda a : a + 10
print(x(10))

#-----------------------------------------------
# Write the above lambda without passing in an argument to the function variable
z = (lambda x: x + 5)(2)
print(z)

#-----------------------------------------------
# Write a lambda which sums 3 arguments
y = lambda a, b, c : a + b + c
print(y(1, 2, 3))

#-----------------------------------------------
# Write a lambda which multiplies the argument by 10
def multiply_by_2(num):
    return num * 2

print(multiply_by_2(10))

product = lambda num: num * 2
print(product(10))

#-----------------------------------------------------
# Insert a lambda function inside another function, passing in
# an argument to the 'outer'function, then call the lambda passing
# in the argument to the lambda
def my_func(n):
    return lambda a : a * n

mydoubler = my_func(2)
print(mydoubler(11))

#---------------------------------------------------
#Finding expensive pianos conventional loops
def expensive_piano(list):
    for piano in list:
        if list[piano] > 100000:
            print(piano)      
expensive_piano(pianos)

# Using lambda functions
# The arguments are all the piano keys, the lambda checks each value of the
# key to see if it satisfies the filter.
expensive_pianos = list(filter(lambda x: pianos[x] > 100000, pianos.keys()))
print(expensive_pianos)

#-----------------------------------------------------
list1 = ["Neytiri", "Ronal", "Quaritch", "Tonowari", "Spider"]
# Iterating through a list with a conditional the long way
def five_ltr(list):
    n = []
    for i in list:
        if len(i) == 5:
            n.append(i)
    return n

print(five_ltr(list1))

#Using lambda with filter
fiveLtrName = list(filter(lambda a : len(a) == 5, list1))
print(fiveLtrName)

#-----------------------------------------------------------------------
cars1 = {"Ford": 25000, "Chevy": 35000, "Dodge": 37500}

def increase_price(car_list):
    result = []
    for car in car_list:
        new_price = (car_list[car] * .15) + car_list[car]
        result.append(new_price)
    return result
print(increase_price(cars1))

#Using lambda with map, if you want to modify every value in an iterable

newPrice = list(map(lambda k: "${:.2f}".format((cars1[k] * .15) + cars1[k]), cars1))
print(newPrice)

# Formatting currency
two = 2

print(f"${two:.2f}")
print("${:.2f}".format(two))

#-----------------------------------------------------------------------








