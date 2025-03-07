# Basics Questions on For Loop

'''
Question:
Write a Python program to find the sum of all even numbers between 1 to 20
using a for loop.
'''

# sum = 0

# for num in range(1,21) :
#   if num%2==0 :
#     sum += num

# print("Sum of even numbers are ", sum)





'''
Write a Python program to count the number of vowels in a given string.
'''
str = input("Please provide the string")

count = 0

for ch in str :
  #Check if ch is a vowel or not
  if ch.lower() in [ 'a', 'e','i','o','u']:
    count +=1

print("Total count of vowel is ", count)

