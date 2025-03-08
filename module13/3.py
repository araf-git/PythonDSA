# Initializer and constructor

# class Person :
#   name = "Vishwa"
#   age = 99

# per1 = Person()
# per2 = Person()
# per3 = Person()

# print(per1.name)
# print(per2.name)
# print(per3.name)

# every object will have same name. cause name is defined in class level
# but every object should have different name. so i should define name in object level


# example with initializer/constructor
# class Person :
#   #initializer/constructor for objects
#   #initializer/constructor is a special type method(function) which is defined inside a class
#   #initializer/constructor name starts with __ and ends with __. and the name(__init__) is fixed. you cant change it
#   #Person class use kore je object banabo shei object ke represent kore initializer/constructor er first parameter(self)
#   def __init__(self, name, age):
#     # here we are initializing the state of the object to be created
#     self.name= name
#     self.age = age

# per1 = Person("Vishwa", 99)

# per2 = Person("Shivani", 97)


# print(per1.name)
# print(per2.name)





# q. can we have multiple __init__ methods? ans: no. in python  multiple __init__ methods are not allowed

# class Person :
#   def __init__(self, name , age):
#     self.name = name
#     self.age = age
  
#   #this __init__ method is actually present in Person class. upper one is not present
#   #the last defined __init__ method will be treated as the only intializer for that class
#   def __init__(self, name):
#     self.name = name

# per = Person("Vishwa Mohan",99)
# print(per.name)
# this will give error: TypeError: Person.__init__() takes 2 positional arguments but 3 were given



# passing variable number of arguments with default parameters
# class Person :
#   #default parameters
#   #here age and hobby are optional parameters
#   def __init__(self, name, age=99, hobby="Cricket"):
#     self.name = name
#     self.age = age
#     self.hobby= hobby


# per1 = Person("Vishwa")
# per2 = Person("Vishwa", 56)
# per3 = Person("Vishwa", 43,"Football")

# print(per1.hobby)
# print(per3.hobby)






class Person :
  #class er property/attribute amra initializer er vitore lekhi na. __init__ function er baire, class er vitore lekhi
  #every object created using Person class will have same country
  #this(country) is same for all object
  #this is class level property
  country = "India"
  def __init__(self, name , age):
    # this 2 attribute(name, age) is called instance(object) attribute. these keeps changing for all objects
    #these are object level property
    self.name = name
    self.age = age

per1 = Person("Vishwa", 99)
per2 = Person("Shweta", 73)

print(per1.name,per1.country)
print(per2.name, per2.country)

# we dont need to create object to use class level property. it can be directly called(used)
print(Person.country)