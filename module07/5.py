# Sequence(Tuple Data Type and Inbuilt Method)

# ordered(indexed) based
# can store different type of data
# immutable

# defining a tuple

# method 1
# tup1 = (3, 5, 8)
# print(tup1)
# print(type(tup1))



# method 2 - tuple constructor
# we can make a tuple from another list/string/tuple

# t1 = tuple([1,2,4])
# print(t1)


# t2 = tuple('tom')
# print(t2)


# aRandomTuple = (5, 2)
# t3 = tuple(aRandomTuple)
# print(t3)


# if i make a single element tuple then it will behave like a normal integer
# t = (5)
# print(type(t))
# so i have to put a comma after the element
# t = (5,)
# print(type(t))


# find how many times an element is present in a tuple
# fruits = ('apple', 'mango', 'apple', 'strawberry')
# print(fruits.count('apple'))
# print(fruits.count('blueberry'))


# find element index
# print(fruits.index('apple'))
# print(fruits.index('blueberry')) - this will give error ValueError: tuple.index(x): x not in tuple


# find tuple length
# print(len(fruits))




# access the elements of a tuple
# fruits = ('apple', 'mango', 'apple', 'strawberry')
# print(fruits[1])
# print(fruits[-2])

# fruits[2] = 'blueberry'
# tuple is immutable. this will give error. TypeError: 'tuple' object does not support item assignment

# print(fruits)



# slicing
# fruits = ('apple', 'mango', 'apple', 'strawberry')
# print(fruits[1:3])