'''
Write a Python program to print the multiplication table of a given number.
'''
num = int(input('Enter the number to generate the multiplication table'))

for i in range(1,11):
  print(num, "*",i , "=", num*i)