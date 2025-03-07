# Inheritance and its types

# inheritance
# what?
#1. import to achieve reusability
#2. to stablish hierarical(parent-child) relationship

# when?
# c1 and c2 are 2 different class
# if isA test is true = then c1 can be the child of c2
# if isA test is false = then inheritence can't be applied


# example
# Cat isA Animal -> true = inheritence can be applied
# Cat isA Machine -> false = inheritence can't be applied


# class Animal :
#   def __init__(self, name):
#     self.name = name

#   def eat(self):
#     print(self.name + " animal is eating")


# class Dog(Animal):
#   def __init__(self,name, type):
#     #Call the constructor/initializer of Animal class
#     Animal.__init__(self, name)
#     self.type = type

#   def getTheNameOfDog(self):
#     print(self.name)


# dog = Dog("Moti", "Dobberman")
# dog.eat()

# dog.getTheNameOfDog()




#super keyword

#Access the Parent Class properties/methods from Child Class
# self = child properties
# super = parent properties

# class Parent :
#   property = 90

#   def eat(self):
#     print("Parent eating")

# class Child(Parent):
#   property = 99

#   def display(self):
#     print("Child property ", self.property)
#     print("Parent property ", super().property)

#   def eat(self):
#     print("Child eating")

#   def callEat(self):
#     self.eat()
#     super().eat()

# obj = Child()
# obj.display()

# obj.callEat()






#using super for calling the parent intializer
# class Animal :
#   def __init__(self, name):
#     self.name = name

#   def eat(self):
#     print(self.name + " animal is eating")


# class Dog(Animal):
#   def __init__(self,name, type):
#     #Call the constructor/initializor of Animal class
#     #Animal.__init__(self, name)
#     super().__init__(name) #call the parent constructor or initializer
#     self.type = type

#   def getTheNameOfDog(self):
#     print(self.name)


# dog = Dog("Moti", "Dobberman")
# dog.eat()

# dog.getTheNameOfDog()



# 3 different things
# 1. property
# 2. method
# 3. initializer/constructor






#Types of inheritance
# 1. single level inheritence
# 2. multi level inheritence
# 3. hiearical inheritence
# 4. multi inheritence
# 5. hybrid inheritence - mix of all

#Single inheritance

# class Animal :
#   def __init__(self, name):
#     self.name = name

#   def eat(self):
#     print("Animal is eating")

# class Dog(Animal) :
#   def __init__(self, name , type):
#     super().__init__(name)
#     self.type = type



#Multi Level Inheritance
# class Animal :
#   def __init__(self, name):
#     self.name = name

#   def eat(self):
#     print("Animal is eating")

# class Dog(Animal) :
#   def __init__(self, name , type):
#     super().__init__(name)
#     self.type = type

# class Pet(Dog):
#   def __init__(self,name,type, houseName):
#     super().__init__(name, type)
#     self.houseName = houseName





#Hierarichal
# class Animal :
#   def __init__(self, name):
#     self.name = name

#   def eat(self):
#     print("Animal is eating")

# class Dog(Animal) :
#   def __init__(self, name , type):
#     super().__init__(name)
#     self.type = type

# class Cat(Animal):
#   def __init__(self, name , type):
#     super().__init__(name)
#     self.type = type





#Multi Inheritance

# class A :
#   def meth1(self):
#     print("Hello from A")

# class B :
#   def meth2(self):
#     print("Hello from B")

# class C(A,B):
#   def meth(self):
#     print("Hello from the child")

# c = C()

# c.meth1()
# c.meth2()



# same method in both parent
# MRO = Method Resolution Order decides the order of methods
# class A :
#   def meth(self):
#     print("Hello from A")

# class B :
#   def meth(self):
#     print("Hello from B")

# class C(A,B): #MRO = from left to right, jetay age method pabo sheta call hobe. 
# # class C(B,A):
#   def meth1(self):
#     print("Hello from the child")

# c = C()
# c.meth()

# print(C.__mro__) #find the mro order





#Hybrid inheritance

# class Pet(Dog,Cat):
#   pass
