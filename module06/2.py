#  Comments and I-O in python

# Single Line Comment

# Multi Line Comment - ''' Doc String  ''' 

'''
hello
hello
'''






# i/o - input output
# input()
# print(input())
#  It allows you to take user input as a string. When you run a Python script with input() in the terminal, the program will pause and wait for the user to type something and press Enter.
# The input() function always returns a string.

# name = input()
# print(name)

# input with optional text
# age = input('Please Sir, Enter Your age in years')
# print(age)

# If you need numeric input, you can convert the string to an integer or float:
# age = int(input("Enter your age: "))






# Output in Python
# print('Hello User')

# name = 'user'
# age= 200
# print('My name is ', name, 'and my age is ', age)




# formated string support in python
# name = 'user'
# age= 200
# print(f'My name is {name} and age is {age}')


# print value in csv(comma separated value)
# x=2
# y=3
# z=4
# print(x,y,z,sep=',')
# print(x,y,z,sep='$')



# dont go to next line while printing (by default it will go to next line) 
print('Hello', end= ' ')
print('User', end= ' ')
print('!')