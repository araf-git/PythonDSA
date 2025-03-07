# Lamda Function - like JavaScript Arrow Function
# they dont have name, so they are anonymous function
# it can take any number of arguments
# body expression is single line


# lambda arguments : expression
# func = lambda x : x+10

# print(func(5))




add = lambda a , b : a+b

print(add(5,6))





# normal function returning lambda function
def myFunc() :
  #return a new function
  return lambda msg : print(msg)

myFunc()("Hello World")
