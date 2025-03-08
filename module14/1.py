# Abstraction
# provide only the important details
# hide unnecessary details

# it makes software/web easy for the customers
# protect/avoid internal information to be leaked


# in python or any oop oriented programming language
# we implement abstraction by using Abstract class


# Abstract Class
# 1. it can't be initialized
# 2. it should have atleast one abstract method(it should not have any implementation details)
# 3. Child Class should implement this abstract method later


# in python, we create abstract class by using inbuilt abc module
# abc module have ABC Class. inside ABC class, their is a decorator  abstractmethod
# if i want to make Animal class abstract, then Animal class should be a child of ABC Class
# and the methods have to be anotated by @abstract method


# creating abstract class

# class Animal :
#   def eat(self):
#     pass

# animal = Animal()
# animal.eat()


# importing ABC class from existing module abc
from abc import ABC,abstractmethod

class Animal(ABC) :
  @abstractmethod
  def eat(self):
    pass


# a = Animal() 
# we cant create object of abstract class
# this will give error. TypeError: Can't instantiate abstract class Animal without an implementation for abstract method 'eat'
# You cannot instantiate an abstract class that has unimplemented abstract methods.
# i have to implement abstract method in concrete child class. using method overriding

# concrete implementation
class Dog(Animal):

  def sleep(self):
    print("Dog is sleeping")
  def eat(self):
    print("Dog is eating")

d = Dog()
# if the parent have an abstract method, then i have to define the same method in child class. (method overriding). otherwise python will give error

