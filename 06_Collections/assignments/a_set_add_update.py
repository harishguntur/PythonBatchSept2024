#!/usr/bin/python3

"""Adding a string to both set.add and set.update 
& observe the difference using 'potato'
"""
# Creating an empty set
string = set()

# Using set.add() with the string 'potato'
string.add('potato')
print("After set.add('potato'):", string)

# Resetting the set
string = set()

# Using set.update() with the string 'potato'
string.update('potato')
print("After set.update('potato'):", string)