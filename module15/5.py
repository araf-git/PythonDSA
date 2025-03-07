# Operator Overloading

# print(3*5)

# print('Asdf'*3)


# class  Num :
#     def __init__(self, num):
#         self.num = num


# num1 = Num(5)
# num2 = Num(7)

# res = num1 + num2
# # here num1 and num2 are 2 different object's. you cant add to objects using + operator. this will give error.
# # TypeError: unsupported operand type(s) for +: 'Num' and 'Num'

# print(res)



















# class  Num :
#     def __init__(self, num):
#         self.num = num

#     # manual oveloading of the operators in python
#     # here add is a magic method that extends the plus operator functionality
#     def __add__(self, U):
#         return self.num + U.num

# num1 = Num(5)
# num2 = Num(7)

# # because of method overloading, now plus is working on object
# res = num1 + num2
# print(res)





# class ComplexNum :
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def __add__(self, C):
#         return self.x + C.x, self.y + C.y
    
# c1 = ComplexNum(2,5)
# c2 = ComplexNum(3,6)

# print(c1+c2)






# class DemoComparisonOverload :
#     def __init__(self, x):
#         self.x = x
    
#     def __gt__(self, O):
#         if(self.x > O.x):
#             return True
#         else:
#             return False
        
# num1  = DemoComparisonOverload(4)
# num2  = DemoComparisonOverload(7)
# print(num1>num2)