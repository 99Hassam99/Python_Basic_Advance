# write a python function to determine if a given string is palindrome

# a palindrome is a phrase that reads the same forwards as backwards
# input= string to evaluate
# output = boolean value
# only consider A-Z letters
# ignore cases eg A==a

import re

def is_palindrome(phrase):
    forwards=''.join(re.findall(r'[a-z]+',phrase.lower()))
    backwards = forwards[::-1]
    return forwards==backwards

a= is_palindrome("EMME")
print(a)