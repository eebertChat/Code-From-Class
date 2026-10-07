phrase = "Robots are the best!"

# Print the first character at index zero
print(phrase[0])
print(phrase[-20])

# Print the length of the string. How many characters there are
print(len(phrase))

# If we try to print character 20. There isn't actually a character at index 20.
# print(phrase[20])

# Print the last character of a string
print(phrase[len(phrase)-1])
print(phrase[-1])

wish = " My first class starts at 11am \t "
print(wish)

# String Methods
print(wish.strip()) #Strips the whitespace at the beginning and the end

lunch = "sandwich, chips, cauliflower, ginger ale"
# print(lunch.split(',')) 
# split will take a string and create a list where it splits on the argument
# passed. In this case, we split on a comma.

lunch_list = lunch.split(',')

# Write a function that takes a list and strips off the leading and trailing
# whitespace of the items in the list.

def strip_list(list_items):
    '''
    Purpose: The function takes a list and strips leading and trailing
    whitespace from the items.

    Parameters: list_items - this the list to be processed; list of strings

    Return Value: the list with whitespace removed
    '''

    for index in range(len(list_items)):
        list_items[index] = list_items[index].strip()

    return list_items

lunch_list = strip_list(lunch_list)
print(lunch_list)

# Slicing
# string_var[start, stop, skip]
# start is inclusive
# stop is exclusive
# skip, how many steps to take

print(wish[0:5]) # The first character through the 4th character
print(wish[:5]) # This is the same as above
print(wish[:8:3]) # Upto the 7th character and taking every 3rd chracter
print(wish[::3]) # Take every 3rd chracter