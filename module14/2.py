# Polymorphism

# Poly = Multi
# morph = form

# polymorphism says, depending on the context, the object might behave differently




#Polymorphism

# class Animal :
#   def eat(self):
#     print("Animal is eating")

# class Dog(Animal) :
#   def eat(self):   #Method overrriding
#     print("Dog is eating")


# class Cat(Animal) :
#   def eat(self):  #Method overriding
#     print("Cat is eating")



# c = Cat()
# d = Dog()
# a = Animal()

# c.eat()
# d.eat()
# a.eat()
# same eat method is called on different object. but the output is different cause for every eat method, the object is different.
# this is a example of polymorphism using inheritence





# example of polymorphism without inheritence
# Duck typing concept
class BirdFly :
  def flyBird(self, bird): #bird is like a variable, i can change. it can be parrot, crow, sparrow
    bird.fly()

class Parrot :
  def fly(self):
    print("Parrot is flying")

class Crow :
  def fly(self):
    print("Crow is flying")

p = Parrot()
c = Crow()

bf = BirdFly()

bf.flyBird(p)
bf.flyBird(c)



# so
# depending on which object is present at the runtime, the output of same method can be different. this is called pollymorphism

