# Method Overloading

# method overloading means multiple methods with same name

#this is explicit method overloading. pythod don't support explicit method overloading
class Calculator :

  def add(self, a, b):
    return a+b

  def add(self,a,b,c):
    return a+b+c

cal = Calculator()

print(cal.add(5,6,7)) #this will work
print(cal.add(5,6)) #this will give error



#Implicit method overloading
#this is implicit method overloading. python supports implicit method overloading
#if i use optional parameters, they will help me to do implicit method overloading
class Calculator :

  def add(self,a,b,c=0):
    return a+b+c

cal = Calculator()

print(cal.add(5,6,7))

