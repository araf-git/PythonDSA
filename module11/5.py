'''
Python program to print the following pattern
*
**
***
****
*****
'''

for row in range(5):
  for j in range(row+1):
    print("*", end="")
  print()