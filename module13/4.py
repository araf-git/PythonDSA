# Methods and its types

# Method = Behaviour

# Method 3 prokar er hoy
# 1. Instance Method
# 2. class method
# 3. static method


#instance/object method
# class Person :
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   #this findAge is instance/object method. 
#   #ei method sudhu matro object diye call kora jabe
#   #aage object banate hobe. erpor oi object use kore object method call korte parbo
#   #self pass kora mandatory. pass kortei hobe.
#   def findAge(self):
#     return self.age


# per = Person("Vishwa", 99)
# print(per.findAge())





#class method
#class method, class level e banate hoy
# class Person :

#   # class level variable
#   country = "India"

#   # @classmethod is a decorator, a additional info. it tells python that greet method(function) is a class method
#   # class method will have access to the class variables, properties, fields
#   # no access to the object properties(no access to self)
#   @classmethod
#   def greet(cls):
#     print("Hello from the ", cls.country)

#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def findAge(self):
#     return self.age


# per = Person("Vishwa", 99)
# print(per.findAge())

# Person.greet()
# # we can use class method using object.
# per.greet()

# so
# class method
# can be called by class/object both
# have no access to object properties
# have access to the class properties






# static method
class Person :

  country = "India"

  @classmethod
  def greet(cls):
    print("Hello from the ", cls.country)

  #static method is totally independent
  #it dont have access to class or object properties
  @staticmethod
  def hello():
    # print(country) #this will give error
    print("Hello")

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def findAge(self):
    return self.age


per = Person("Vishwa", 99)
print(per.findAge())

Person.greet()
per.greet()

Person.hello()
per.hello()