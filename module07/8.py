# Sets and Inbuilt Method

# No duplicates allowed. All elements unique
# Mutable
# Unordered


# my_set = {1, 2, 3, 5}
# curly bracket er vitore number dile set hoye jay
# print(my_set)
# print(type(my_set))


# s1 = {1, 4, 2, 1, 5}
# print(s1)


# set constructor
# s2 = set()
# print(s2)

# s3 = set({5,6,7})
# print(s3)



# Add Elements to set
# s = set()

# s.add(5)
# s.add(2)
# s.add(5)

# print(s)




# Remove Elements from set
# s1 = {3, 9, 7}
# print(s1.discard(9))
# print(s1)

# s1 = {3, 9, 7}
# s1.discard(6)

# print(s1)




# can i create a immutable set?(is it possible)
# yes. FrozenSet is immutable
# fs = frozenset([1, 3])
# creating from a list
# print(fs)
# print(type(fs))


# fs = frozenset({1, 3})
# creating from a set
# print(fs)
# print(type(fs))






# dictionary er key immutable hote hoy. set jehetu mutable tai dictionary er key set hote parbena. but frozenset hote parbe, karon frozenset immutable
fs = frozenset({1, 3})
dict1 = {fs : 'Tom'}
print(dict1)

