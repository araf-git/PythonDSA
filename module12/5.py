# Kwargs in python

# def display_info(**kwargs):
#   print(kwargs)
#   print(type(kwargs))

#   for key, value in kwargs.items():
#     print(key ," -> " ,value)

# display_info(name="Asdf", age=99, city = "CTG")





# example with positional, args, kwargs arguments

# def func (a, b, *args, **kwargs):
#   print(a)
#   print(b)
#   print(args)
#   print(kwargs)


# func(5,6,7,8,9,name="Asdf", age=99)



# kwargs should be the last parameter. this example will give error
# def func1(**kwargs, a,b):
#   print(kwargs)
#   print(a)
#   print(b)


# func1(name="Asdf",age=99, 7,9)