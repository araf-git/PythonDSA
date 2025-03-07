# Different Types of Arguments


#Default argument

# def greet(name, message="Good Morning"):
#   print(name, message)

# greet("Asdf")




#keyword arguments
# def greet(name, age, message):
#   print(message, name, "your age is", age)

# # greet('asdf', 200, "Hello")
# greet(age=99, message="Hello",name="Asdf") # with keywords arguments, you can swap arguments order





#positional arguments

# def add_numbers(x, y):
#   print("x ", x)
#   print("y ", y)
#   print(x+y)

# add_numbers(5,6)
# add_numbers(6,5)




# passing variable number of arguments in a function

# def sum_numbers(*args):
#   print(type(args))
#   print(args)

#   sum = 0
#   for num in args :
#     sum +=num
#   return sum

# print(sum_numbers(1,2,3,4,5))




# normal arguments with variable args. (like javaScript rest parameters)
# def fn(a,b,*args):
#   print(a)
#   print(b)
#   print(args)
#   print(*args)


# fn(5,6,7,8,9)






# you cant reverse this. TypeError: fn() missing 2 required keyword-only arguments: 'a' and 'b'
# def fn(*args,a,b):
#   print(a)
#   print(b)
#   print(args)
#   print(*args)


# fn(5,6,7,8,9)


# to solve this problem
# *args should be the last parameter
# or use keyword arguments like this


# def fn(*args,a,b):
#   print(a)
#   print(b)
#   print(args)
#   print(*args)


# fn(5,6,7,a=8,b=9)






