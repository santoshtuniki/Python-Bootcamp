starting_dictionary = {
    "a": 9,
    "b": 8,
}

'''
final_dictionary = starting_dictionary.append({"c":7})
AttributeError: 'dict' object has no attribute 'append'
'''

'''
final_dictionary = starting_dictionary.update({"c":7})
{'a': 9, 'b': 8, 'c': 7}
None
'''

'''
final_dictionary = starting_dictionary += {"c":7}
final_dictionary = starting_dictionary["c"]:7
SyntaxError: invalid syntax
'''

'''
final_dictionary = starting_dictionary["c"] = 7
{'a': 9, 'b': 8, 'c': 7}
7
'''

starting_dictionary["c"] = 7
final_dictionary = starting_dictionary
'''
{'a': 9, 'b': 8, 'c': 7}
{'a': 9, 'b': 8, 'c': 7}
'''


print(starting_dictionary)
print(final_dictionary)
