#Encapsulation
# is a way to bind the data(state) of the object with methods
# easy definition - hide or make the state(data) private. so if any other object directly want to change the state of my object, they should not be able to do it

# encapsulation
# 1. all the fields/properties should be private
# 2. use setter, getter to access them. they(setter, getter) should be public

class Person :
  def __init__(self, name, car):
    self.__name = name
    self.__car = car


  #Getters and Setters - public method to allow the contolled interactions
  def getName(self):
    return self.__name
  def setName(self, name):
    self.__name = name
  def getCar(self):
    return self.__car
  def setCar(self, car):
    self.__car = car


per = Person("Vishwa", "BMW")

print(per.getName())
per.setName("Vishwa Mohan Singh")
print(per.getName())