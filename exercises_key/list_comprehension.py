# List comprehension offers a shorter syntax when you want 
#to create a new list based on the values of an existing list.

# A function to return all composers with 'v' in the name

# tuple
composers = "Beethoven", "Ravel", "Debussy", "Rachmaninoff", "Chopin", "von Weber"
print(type(composers))

def v_composers(l):
    new_composers = []
    for composer in l:
        if "v" in composer:
            new_composers.append(composer)
    print(new_composers)

v_composers(composers)

#list_comp = [expression for item in iterable (if condition == True)]
#The return value is a new list, leaving the old list unchanged.

#The expression is the current item in the iteration but also the outcome which can #be manipulated before it is added to the new lists
# The condition is like a filter that only accepts the items that valuate to True.

new_composers0 = [composer for composer in composers if "v" in composer]
print(new_composers0)

# # The expression is the current item in the iteration but also the outcome which can be manipulated before it is added to the new lists

# # Examples

new_composers1 = [composer.lower() for composer in composers if "v" in composer]
print(new_composers1)






