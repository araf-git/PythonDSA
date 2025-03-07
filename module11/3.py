# Number is Prime or Not

'''
Write a Python program to check if a number is prime or not.
'''
# prime number = 1/self diye divisible

num = int(input("Enter the num"))

isPrime = True
if(num <=1):
  isPrime = False

for i in range(2, int(num/2)+1):
  if num%i==0 :
    isPrime = False
    break

print("Number passed is prime :", isPrime)


