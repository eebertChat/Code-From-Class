# Dictionaries

# Dictionaries are implemented as hash maps or hash tables with hash functions.
# A dicitonary is a pairing between the set of keys and the set values. Every
# entry in the dictionary is a key : value pair. 

# Immutable and Mutable data. Mutable data can be changed and often is in
# memory. Example of a mutable data structure is a list. Immutable data 
# structures cannot be changed. Example of an immutable data structure is 
# a string.

# The keys in a dictionary need to be an immutable type. This is so that
# the hash function obtains the same value every time the key is looked up.

# The values can be mutable or immutable.

# Adding and retrieving things out of a dicitonary can be done quickly. This
# is what makes them a well-used data structure.

# Empty dictionary
my_dict = {}

phone_list = {"Caroline" : "555-3691", "Mori" : "555-2211", "Keoki" : "055-1133"}

print(phone_list)
print(phone_list.keys())    # The method to get the dictionary keys is keys()
print(phone_list.values())  # The method to get the dictionary values is values()

# Lookup the value for a particular key phone_list[key]
print(phone_list["Mori"])

# Add to a dictionary
phone_list["Saanvi"] = "222-3145"
print(phone_list)

# Change a value in a dictionary
phone_list["Keoki"]="555-1133"
print(phone_list)

# Frequency counts
phrase = "A picture is worth a thousand words"
letter_count = {}

for letter in phrase:
    if letter in letter_count:      # Is letter already a key in letter_count?
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1

print(letter_count)


# An Exercise for you
# Change the above so that it counts the words in 
new_phrase = "the quick brown fox jumped over the quick brown dog who jumped \
    over the brown log"

def freq_count(phrase):
    word_count = {}
    words = phrase.split()

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

print(freq_count(new_phrase))


# Write a function

def classList(students, year):
    '''
    Purpose: To take a dictionary students with student : grad year pairs
    and produce a list with students who graduate in the parameter year.

    Parameters:
        students - a dictionary with with names as keys and class years as 
        values; dict
        year - the year that students are graduating; int

    Return Value: List of students who are graduating in year; list

    Examples:
        student_List = {"Caroline" : 2027, "Xavier" : 2030, "Melissa" : 2029, "Kathy" : 2027}

        classList(student_List, 2030)
            ["Xavier"]
        classLIst(student_List, 2027)
            ["Caroline", "Kathy"]
        classList(student_list, 2022)
            []
    '''

    names = []

    for name in students:
        if students[name] == year: 
            names.append(name)

    return names



student_List = {"Caroline" : 2027, "Xavier" : 2030, "Melissa" : 2029, "Kathy" : 2027}

print(classList(student_List, 2022))
