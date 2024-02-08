# Add functionality to an existing function with decorators. 
# This is called metaprogramming.
# A function can take a function as argument (the function to be decorated) and #return the same function with or without extension.
# Extending functionality is very useful at times.

#Functions are first-class objects

def func1():
    print("This is a function")

# I can assign a function to a variable! 
another_func = func1
another_func()
#--------------------------------------------------

# Example of nested functions
# Passing exponents to a number
def outer1(exp):
    def inner(num):
        return num ** exp
    return inner

add_exps = outer1(5)

# the above equals this
# def outer1(5):
#     def inner(num):
#         return num ** 5
#     return inner

result = add_exps(6)
print(result)

#-------------------------------------------------

#---------------------------------------------------------
# Basic decorator functionality

def outer(func):
    print("Beginning the outer function")
    def wrapper():
        print("Beginning the wrapper function")
        func()
        print("Returning the wrapper function")
    return wrapper

def basic_func():
    print("I'm just a basic function")

result = outer(basic_func)
result()
#---------------------------------------------------------

#---------------------------------------------------------
# Python decorators are functions that takes in a function and returns it by adding some functionality

def authenticator(func):
    # define inner function
    def wrapper():
        # additional behavior
        print("I'm authenticating a plain ol' django view")
        # call the original function
        func()
    return wrapper

def some_view():
    print("I'm a plain ol' django view")

# Decorating the function by passing the some_view function to the authenticator
# The authenticator returns the wrapper function and assigns it to a variable
result = authenticator(some_view)

# Calling the wrapper function
result()

#-----------------------OR---------------------------------
print()

@authenticator
def some_view():
    print("I'm a plain ol' django view")

some_view()

print()
#----------------------------------------------------------
# Decorator functions with parameters
# A function to check if 2 string are equal

def str_check(func):
    def wrapper(n1, n2):
        print("I'm going to check if the names are equal")
        if n1 == n2:
            print("The name must be different")
            return
        print("The names are different")
        return func(n1, n2)
    return wrapper


# The best way
@str_check
def full_name(fname, lname):
    print(f"{fname} {lname}")

full_name("glenn", "langdon")

#Verbose way    
# concat_name = str_check(full_name)          
# concat_name("glenn", "laurie")



#----------------------------------------------------------
# DO IN THE PYTHON INTERPRETER
def fave_piano(piano):
    return f"This {piano} is my favorite"

def auditioned_piano(a_function):
    return a_function("Bösendorfer")

auditioned_piano(fave_piano)


def my_name(name):
    return f"My name is {name}"

def your_name(another_name):
    return f"Your name is {another_name}"

def who_is(a_function):
    return a_function("Glenn")

who_is(my_name)
who_is(your_name)

print()








