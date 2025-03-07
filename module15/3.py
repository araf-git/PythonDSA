# Raise, assert & Inbuilt exception


# raise
# arr = [1,2,3]

# python dont have any problem with this array. but i have. for me, the array length must be atleast 4. so to do this, i can create my own error(to create own error, use raise keyword)


# if len(arr) < 4 :
#     raise Exception(f'Length if the given list is {len(arr)} which is < 4')



# assert (use inside function to validate the arguments)
# def cube_root(num):
#     # check if the num is positive and if not, i would raise an exception
#     assert (num >= 0) , "Pass a positive number"
#     return num**(1/3)

# print(cube_root(8))

# try :
#     val = cube_root(-8)
#     print(val)
# except: 
#     print('Please provide valid positive integer for the cube root')

# print('last line')




# handling error with try-else. (normally if-else exists in other programming language. but in python you can combine try-else)
# if error occurs, then except will execute. if no error occurs, then else will execute
# def operate(num):
#     try:
#         result = 5/num
#     except ZeroDivisionError:
#         print('cant divide a number by 0')
#     else: 
#         print(result)

# operate(2)
# operate(0)





# if i want a part of my code to get executed everytime(even if there is error), then i will write that part of code inside finally block
def operate(num):
    try:
        result = 5/num
    except ZeroDivisionError:
        print('cant divide a number by 0')
    finally: 
        print("This portion of the code will always be executed")

operate(2)
operate(0)   
