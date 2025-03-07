# Relationship of association

# two object. one is person another one is car. they can exist independently. but in real world
# the person has a car
# this type of relationship is called aggregation



#Has A - Aggregation

class Car :
  def __init__(self, brand, color):
    self.brand = brand
    self.color = color


class Person :
  def __init__(self, name , car): #here car is a object. cause person hasA car
    self.name = name
    self.car = car


car = Car("BMW", "Black")
person = Person("Vishwa", car)




# two object. one is human-body another one is heart
# heart can only exist if human-body is there
# heart is totally dependent on the human-body
# this type of relationship between the two objects's is called composition

#Composition - one object will be created inside another object
class Engine :
  def engineDetails(self):
    print("Car engine is model E1213")

class Tyres :
  def tyreDetails(self):
    print("Car tyre is apollo")

class Doors :
  def doorDetails(self):
    print("Doors of the car is automatic")


class Car :
  def __init__(self):
    self.engine = Engine() #here engine, tyre, doors objects are created. (inside the car)
    self.tyres = Tyres()
    self.doors = Doors()

  def printDetails(self):
    self.engine.engineDetails()
    self.tyres.tyreDetails()
    self.doors.doorDetails()

c = Car()
c.printDetails()