# This is a tuple!
composers = "Beethoven", "Ravel", "Debussy", "Rachmaninof", "Chopin", "von Weber"
print(type(composers))

def v_composers(l):
    new_composers = []
    for composer in l:
        if "v" in composer:
            new_composers.append(composer)
    print(new_composers)

v_composers(composers)

#list_comp = [expression for item in iterable (if condition == True)]

# 1) Render the above function as a list comprehension


# 2) Render the above function but return the list as lower case