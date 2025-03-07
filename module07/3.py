# Sequence(List Data Type and Inbuilt Method)

# List = Collection of Elements
# List is order(index) based
# List is Mutable(mutable means, i can change it)


# students = ['a', 'b', 'c']
# print(students)
# print(type(students))



# make a list from another list
# students = ['a', 'b', 'c']
# list2  = list(students)
# print(list2)
# this is list constructor method


# make a list from another string
# list3 = list('asdf')
# print(list3)


# make a list from another tuple
# list4 = list((3,4,'zxcv'))
# print(list4)



# Accessing the elements of a list
# access elements based on their index
# +ve index
# list = [1, 3, 5]
# print(list[1])
# +ve index value will always be [0, length-1]

# -ve index
# list = [-1, -3, -5]
# print(list[-1])
# -ve index value will always be [-length, -1]





# adding(inserting) elements to the list

# append will add elements to the end of the list
# arr = [3, 2, 1]
# arr.append(11)
# print(arr)


# to insert at a particular index we need to use insert(index, element)
# arr = [3, 2, 1]
# arr.insert(2, 43)
# print(arr)
# array(list) is mutable. cause i can modify it



# adding l2 list elements to l1 list using l1.extend(l2)
# l1  = [1,3]
# l2 = ['something', 'asdf']

# l1.extend(l2)

# print(l1)





# Remove elements from  the list

# remove - i have to mention which element i want to remove
# arr = [3,5,2]
# arr.remove(5)
# print(arr)

# arr = [3,5,2,1,7,1,9]
# arr.remove(1)
# print(arr)
# if array have duplicate element then remove will only remove the first occurance of that element



# pop - will remove from the last

# arr = [3,5,2]
# print(arr.pop())
# print(arr)

# pop with index - will remove from that particular index
# arr = [3,5,2]
# print(arr.pop(1))
# print(arr)


# replace the value at a given index 
# students = ['a', 'b', 'c', 'd']
# students[2] = 'z'
# print(students)


# replace the value at a range
# students = ['a', 'b', 'c', 'd']
# students[1:3] = 'q','w'
# end index is not included
# print(students)


# replacing 2 element with 1 value
# students = ['a', 'b', 'c', 'd']
# students[1:3] = 'q'
# print(students)


# reversing a list
# l1 = [1, 3, 5, 7]
# l1.reverse()
# print(l1)


# copying a list with copy()
# it will create a different object with different address
# l1 = [1, 3, 5, 7]
# l1_copy = l1.copy()
# print(l1_copy)
# print(id(l1_copy), id(l1))


# sorting a list
# l1 = [7, 1, 5, 3]
# l1.sort()
# print(l1)










# keys to understand Python data types
# 1. Sequence: Ordered collection supporting indexing and slicing.
# 2. Indexing: Accessing elements using position numbers.
# 3. Mutability: Ability to change data after creation.
# 4. Immutability: Data cannot be changed after creation.
# 5. Ordering: Maintaining element sequence as inserted.
# 6. Iterability: Ability to loop over elements.