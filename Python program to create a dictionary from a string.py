# Python program to create a dictionary from a string

from collections import defaultdict, Counter

str1 = 'w3resource'       # Example string is given in assignment
my_dict = {}
for letter in str1:
    my_dict[letter] = my_dict.get(letter, 0) + 1
print(my_dict)
