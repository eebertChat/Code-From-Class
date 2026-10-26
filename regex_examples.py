# Regular Expressions

# We want to specify some patterns of text to search for.
# Phone numbers

# Validating phone numbers of the format xxx-xxx-xxxx
# Without regular expressions

def validate_phone_num(pn):
    '''
    Purpose: To validate that the argument passed is a string is in the format
    xxx-xxx-xxxx
    Parameter: pn is the string that needs to be verified.
    Return Value: True if the string has the proper format and false otherwise.
    '''

    if(len(pn) != 12):
        return False
    if(pn[3] != '-' or pn[7] != '-'):
        return False

    for i in range(0,3):
        if(not pn[i].isdigit()):
            return False

    for i in range(4,7):
        if(not pn[i].isdigit()):
            return False

    for i in range(8,12):
        if(not pn[i].isdigit()):
            return False

    return True

# phone_num = "555-x11-2323"
# print(validate_phone_num(phone_num))

# With Regular Expressions
import re           # The re module contains tools for regex

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo_phone_number = phoneNumRegex.search("555-444-1212")
print(mo_phone_number.group())
mo_phone_string = phoneNumRegex.search("My phone number is 555-333-1216")
print(mo_phone_string.group())

# Using Capture Groups
phoneNumRegex2 = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo_capture_pn = phoneNumRegex2.search("My phone number is 555-333-1216")
print(mo_capture_pn.group())    # group() and group(0) are the same
print(mo_capture_pn.group(1))
print(mo_capture_pn.group(2))

# Using the method groups() we get a tuple, and we can use tuple unpacking
print(mo_capture_pn.groups())
area_code, phone_number = mo_capture_pn.groups()
print(area_code)
print(phone_number)

# ? The preceding capture group is optional
batREgex = re.compile(r'Bat(wo)?man')
mo1 = batREgex.search("The adventrues of Batman!")
mo2 = batREgex.search("The adventures of Batwoman")
print(mo1)
print(mo2)

# * matches on zero or more instances
batREgex2 = re.compile(r'Bat(wo)*man')
mo1 = batREgex2.search("The adventures of Batman!")
mo2 = batREgex2.search("The adventures of Batwoman!")
mo3 = batREgex2.search("The adventures of Batwowowoman")

print(mo1)
print(mo2)
print(mo3)

# + match on at least one
batREgex3 = re.compile(r'Bat(wo)+man') # This will not accept "Batman"


# Character Classes:
# \d - numeric digits 0-9
# \D - any char not 0-9
# \w - any letter, numeric digits, or underscre
# \s - any space, tab, or new line character
# [a-z] - any lowercase character
# [A-Z] - any uppercase character
# [a-zA-Z] - both upper and lower
# [0-5] - any number between 0 and 5 inclusive

# <(.*)> - will greedily match anything between two angle brackets
# <(.*?)> - will match anything between two angle brackets in a nongreedily

# Exercise
# What regular expression would be used to match at least one digit, followed
# by a space and then at least one alphanumeric character

regex = "\d+\s\w+"

this_regex = re.compile(r'\d+\s\w+')
mo = this_regex.search("67 b")
mo2 = this_regex.search("67ten")

print(mo)
print(mo2)      # If there is no match, then the pattern group doesn't exist
                # The type that is returned is None
                # You can use None to decide if there was match

# Exercise 
# Write a regular expression to validate a basic E-mail address
# Format: at least one alphanumeric character, followed by an '@', then at
# least one lower or upper case character, then a period and then three letters

email_regex = "\w+@[a-zA-Z]+.\w{3}"

# Using a period by itself will match on any character. To match the
# literal period you have to use an escape character \.

email = re.compile(r'\w+@[a-zA-Z]+\.\w{3}')
mo = email.search("jjackson@moobly.com")
mo1 = email.search("jjackson@mooblyXcom")

print(mo)
print(mo1)