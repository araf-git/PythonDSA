# Pass by Value(Immutable Datatypes)


#Pass by Value - Means Passing The Copy. Not The Original Value
# if we change the copy then the original value wont change

# num = 5

# def modify_num(num):
#   num +=1
#   print(num)

# modify_num(num) # this num is the copy of original num = 5 variable

# print("Original num", num)


# if the arguments are immutable data types, then pass by value will be activated
# Immutable datatypes : Numbers, String, tuple -- Passed by Value




# if the arguments are mutable data types, then pass by reference will be activated
# change will impact the original data
# Pass by reference : -> Mutable datatypes : List, Disctionary

my_list = [1,2,4]

def modify_list(li):
  li.append(5)
  print(li)

print("Before calling fun", my_list)

modify_list(my_list)

print("After calling fun", my_list)