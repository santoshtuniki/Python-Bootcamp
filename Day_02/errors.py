num_len = len(input("What is your name?"))
# print("Your name has " + num_len + " characters.")

'''
TypeError: can only concatenate str (not "int") to str
'''

# print(type(num_len))

new_len = str(num_len)
print("Your name has " + new_len + " characters.")
