# Classes and Object

# class is nothing but a type, and defined as a blueprint
# if class is a blueprint, then object is a specific instance of that blueprint(class)


# in a class, every student will have a id, name, age, interest. this is called as a blueprint
# now a student have an id:10, name: 'asdf', age:15, interest: football. this student object is a instance of the class blueprint
# another student have an id:13, name: 'zxcv', age:16, interest: cricket. this student object is another instance of the class blueprint

# instance = উদাহরণ (google)

# so
# class = blueprint
# object = instance
# with the help of class, we create object(instance)


# to define a class, we use class keyword.
# class name starts with Capital letter
# class Person :
#     pass

# creating object with Person class
# obj = Person()

# print(type(obj))
# print(obj) # it will print the address of obj object




class Person :
  name = "Vishwa"
  age = 99

per = Person()

print(per.name)
print(per.age)


# adding new attributes/properties in per object
per.hobby = "Cricket"
per.loveName = "Babu"

print(per.loveName)
# this hobby and loveName is only specific or added to this per object only. 
# if i create another object using Person class, then that object wont have this hobby or loveName


obj = Person()
print(obj.loveName) # this will give error. AttributeError: 'Person' object has no attribute 'loveName'

