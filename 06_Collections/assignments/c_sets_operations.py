# Define two sets
setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}

# Logical Operations
# Union of setA and setB
union = setA.union(setB)  
print("Union:", union)

# Intersection of setA and setB
intersection = setA.intersection(setB)  
print("Intersection:", intersection)

 # Elements in setA not in setB
difference = setA.difference(setB) 
print("Difference:", difference)


# Relational Operations
# Checks if setA is a subset of setB
subset = setA.issubset(setB)  
print("Is A subset of B?", subset)


# Checks if setA is a superset of setB
superset = setA.issuperset(setB) 
print("Is A superset of B?", superset)

