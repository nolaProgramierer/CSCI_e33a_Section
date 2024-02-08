# Tuples
#A tuple is sequence of values, of any type, that are immutable
#Tuples are written with round brackets.

t = 'a', 'b', 'c', 'd', 'e'
print(t)

# More common way to express tuples
t1 = ('a', 'b', 'c', 'd', 'e')
print(t1)

# Create a tuple, the final comma is required
t2 = 'a',
print(t2)

# this is not a tuple!
t2 = ('Hello')
print(t2)


# One value of tuples is their ability to return multiple values.
# divmod is a built-in function that take two arguments and 
# returns a tuple of 2 values

result = divmod(101, 50)
print(result)

# also you can assign the result to different values

quotient, result1 = divmod(101 , 50)
print(quotient)
print(result1)

# Using min and max methods, which are built-in functions
# that find the smallest and largest numbers of a sequence

# Return a tuple
def find_biggest_smallest(result):
    return min(result), max(result)

r = find_biggest_smallest(result)
print(r)

#---------------------------------------------------
# gather & scatter
gather_args = "Hello", 1, {"fname" : "glenn"}, 1001

#gather example
def print_gather(*args):
    print(args)

print_gather(gather_args)

#Sum a tuple
t3 = (1, 2, 3, 4)

print(sum(t3))


  