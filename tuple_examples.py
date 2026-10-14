# Tuples

# Tuples are an ordered immutable sequence. They look like ordered tuples in 
# math (1,5,7,11); ('a', 'x', 'c')

# Create an empty tuple
point = ()

# The comma that distinguishes a tuple
point = (2) # the integer 2
point = 2, # the tuple containing a single element 2
print(point)

# Concatenate Tuples
point = point + (3,)
print(point)
point = point + (-1,4)
print(point)

#Tuple Unpacking
x,y,z,w = point
print(f"x: {x}, y: {y}, z: {z}, w: {w}")

# Things the interpreter gets mad about
# x,y = point - Note enough variables (places) to store the items in the tuple.

# The proper way to ignore items in a tuple
a,b,_,_ = point     # Use an underscored for the itmes you want to ignore
print(f"a: {a}, b: {b}")

# We can index tuples
print(point[2])

# Tuples are immutable so we cannot change items in a tuple.
# point[2] = -3


# Exchange Values
# Suppose we want to exchange the values in two variables
s = 5
t = 8

# With tuples
print(f"Before Swap - s: {s}, t: {t}")
(s,t) = (t,s)
print(f"After Swap - s: {s}, t: {t}")

# Without tuples - using a temporary variable
temp = s
s = t
t = temp

# Returning multiple items out of a function
my_scores = [88,95,70,62,99,24,74,85]

def find_max_min(scores):
    '''
    Purpose: Find the maximum and minimum items in a list
    Parameters: scores - the numerical list we want the max / min of; list
    Return Values: max, min; float / int
    '''

    minimum = scores[0]
    maximum = scores[0]

    for item in scores:
        if (item < minimum):
            minimum = item
        if (item > maximum):
            maximum = item

    return minimum, maximum

min, max = find_max_min(my_scores)
print(f"Min: {min}, Max: {max}")

# Here's an Exercise for you

my_rocks = [('talc', 1), ('lead', 1.5), ('copper', 3), ('nickel', 4), ('silicon', 6.5),
         ('emerald', 7.5), ('boron', 9.5), ('diamond', 10)]

# The first element of the tuple is the mineral and the second is the hardness
# rating of the mineral. 
# Soft - rating of 1-3
# Medium - rating of 3.1-5
# Hard - rating of 5.1-8
# Very Hard - rating of 8.1 - 10

def hardness(rocks):
    '''
    Purpose: To take a list of (mineral, hardness) and make a dictionary of
    hardness categories
    Parameters: rocks is a list of tuples of minerals and hardness ratings
    Return Value: dictionary where the hardness categories are the keys and
    the values are a list of minerals for that category.

    Example:
        hardness(my_rocks)
            {'soft' : ['talc', 'lead', 'copper'],
             'medium' : ['nickel'],
             'hard' : ['silicon', 'emerald'],
             'very hard' : ['boron', 'diamond']}
    '''

    category_dict = {'soft' : [], 'medium' : [], 'hard' : [], 'very hard' : []}

    for item in rocks:
        if (item[1] > 8):
            category_dict['very hard'].append(item[0])
        elif (item[1] > 5):
            category_dict['hard'].append(item[0])
        elif (item[1] > 3):
            category_dict['medium'].append(item[0])
        else:
            category_dict['soft'].append(item[0])

    return category_dict

# Advantages of Tuples
# Tuples use less space than lists
# You can't change tuples by mistake
# You can use tuples as dictionary keys
# Function arguments are passed as tuples
# Return more than one item out of a function using a tuple.