# Dictionary Data Type and Inbuilt Method(WIth Key Value pair)


# Dictionary key must be a immutable data type (int, string, boolean, tuple)
# key has to be unique


# dict1 = {1: 'Tom', 2: 'Jerry', True: 'Love'}
# print(dict1)
# Output = {1: 'Love', 2: 'Jerry'} karon python e 1⟷True. tai key match howar karone value overwrite hoye geche


# Dictionary constructor methods
# dict1 = dict(name='Tom', age=5, True='Love')
# it will give error. SyntaxError: cannot assign to True
# constructor use korle key True use kora jabena. karon True ekta keyword
# dict1 = dict(name='Tom', age=5)
# print(dict1)
# print(type(dict1))



# Accessing the elements 
# students_details = {'name': 'Tom', 'age': 6, 'city': 'ctg'}
# print(students_details['name'])

# getting all the keys
# print(students_details.keys())
# getting all the values
# print(students_details.values())
# getting all the key,values = list of the tuples of key, value pair
# print(students_details.items())




# Adding elements in the dictionary
# students_details = {'name': 'Tom', 'age': 6, 'city': 'ctg'}
# students_details['country'] = 'BD'
# print(students_details)




# adding one in another
# students_details = {'name': 'Tom', 'age': 6, 'city': 'ctg'}
# marks_details = {'English': 100, 'Math': 78, 'Science': 92}
# students_details.update(marks_details)
# print(students_details)



# Remove elements from dictionary
students_details = {'name': 'Tom', 'age': 6, 'city': 'ctg'}

# print(students_details.pop('city'))
# pop requires a key
# print(students_details)

# print(students_details.popitem())
# popItem will remove the last element
# print(students_details)


# del students_details['age']
# print(students_details)

students_details.clear()
print(students_details)

