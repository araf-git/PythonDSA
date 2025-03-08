# Access Modifier



'''
  access modifier 2 type er hoy
  public and private
'''

#everything(class, method, property) is by default public


class Person :
  def __init__(self, name, age, salary):
    self.name = name #public
    self.age = age #public
    self.__salary = salary #private
    #to make a property private, use self.__property = property
    #private property can only be accessed inside the class
    #cant be accessed outside the class

  def findAge(self): #public
    return self.age

  def getSalary(self):
    print(self.__salary)
    self.__calculateTax()

  def __calculateTax(self): #private method
    print("calculating tax")


per = Person("Vishwa", 99, 5000)

print(per.name)
# print(per.__salary) #this will give error


per.getSalary() #this can read salary. cause getSalary() is defined inside the class

# per.__calculateTax() #this will give error. i cant call private method outside the class. but i can call it inside the class




# so
# to make property/method private use __
# it can be called inside the class
# cant be called outside the class




# but 
# i can still use private property/method outside the class
# to use private property/method outside the class
# use object._Class__property/method
print(per._Person__salary)
print(per._Person__calculateTax())