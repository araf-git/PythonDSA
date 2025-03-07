# Sequence ( String Data Type and Inbuilt Method)

# String = group of characters
# String immutable

# Defining a String
# name = 'unknown'
# city = "chittagong"
# country = '''BD'''




# index


# +ve index, from left to right --> index start from [0, length-1]
# name = 'unknown'
# print(name[3])
# print(name[8]) = this will give error cause 8th index is not defined in name


# -ve index, from right to left  <-- index start from [-length, -1]
# name = 'unknown'
# print(name[-1])
# print(name[-7])


# string immutable. i cant modify it. if i modify then a new string will be created. but the existing string will not change
# myStr = 'something'
# myStr[0] = 'm'
# print(myStr)
# this will give error = TypeError: 'str' object does not support item assignment



# string concatenation
# first_name = 'tom'
# last_name = 'jerry'
# complete_name = first_name + last_name
# complete_name = first_name +' '+ last_name
# print(complete_name)


# string length
# first_name = 'tom'
# last_name = 'jerry'
# complete_name = first_name +' '+ last_name
# print(len(complete_name))




# string slicing
# str[a:b] --> new string will be [a, b-1]
# str = 'my string'
# print(str[3:8])

# slicing from a particular index till the end
# str = 'my new string'
# print(str[3:])


# slicing from 0th index to a particular index
# str = 'my new string'
# print(str[:6])

# from 0th to the last index
# str = 'my new string'
# print(str[:])


# slice with negative index
# str = 'my new string'
# print(str[-10:-1])


# mixing +ve, -ve index
# str = 'my new string'
# print(str[-9:9])


# Uppercase
# myStr = 'tom'
# print(myStr.upper())

# lowercase
# myStr = 'ToM'
# print(myStr.lower())

# Capitalize
# myStr = 'tOM'
# print(myStr.capitalize())

# remove extra space
# myStr = '    tOM      '
# print(myStr.strip())


# replace method
# myStr = 'hello dear, I am very good, I am very nice, I am wow'
# # print(myStr.replace('I am', 'We are'))
# print(myStr.replace('I am', 'We are', 2))


# Escape character
# print('Hello \n user') 
# new line Escape character
# print('tom\tjerry')
# tab space Escape character
# print('tom \'jerry\'')

