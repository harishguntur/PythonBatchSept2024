#!/usr/bin/python3

"""
## Assignment -- create a dict one with single dimension 
# and another with dict with dict (mulgti-dimension) and 
# see the importanvce of dict.copy() (shallow copy ) and 
# copy.deepcopy
"""

import copy

# Single-dimensional dictionary
single_dim_dict = {'a': 1, 'b': 2}
shallow_copy_single = single_dim_dict.copy()

# Multi-dimensional dictionary
multi_dim_dict = {'a': {'key1': 1}, 'b': {'key2': 2}}
shallow_copy_multi = multi_dim_dict.copy()
deep_copy_multi = copy.deepcopy(multi_dim_dict)

# Modify the original multi-dimensional dictionary
multi_dim_dict['a']['key1'] = 100

# Output results
print("Single-dimensional Dict - Original:", single_dim_dict)
print("Single-dimensional Dict - Shallow Copy:", shallow_copy_single)

print("Multi-dimensional Dict - Original:", multi_dim_dict)
print("Multi-dimensional Dict - Shallow Copy:", shallow_copy_multi)
print("Multi-dimensional Dict - Deep Copy:", deep_copy_multi)