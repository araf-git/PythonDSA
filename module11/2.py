# Print the Fibonacci Series


'''
Write a Python program to print the Fibonacci series up to n terms.

1 , 1 , 2, 3, 5, 8, 13 ...

'''

# in a ficonacci serise, nth term = (n-1)th + (n-2)th term


n = int(input("Please enter the value of n - upto which we want the fibonacci series"))
print(n)
if (n <=0):
  print("Number entered is not correct. It should be > 0. Entered num", n)

print(1, end=",")
if(n==1):
  pass
else :
  print(1, end=",")
  if(n==2):
    pass
  else:
    #print the remaining part of the series
    prev = 1
    prev_prev=1
    for num in range(3, n+1):
      print(prev+prev_prev, end=",")
      prev, prev_prev = prev+prev_prev , prev
