# Problems on sorting

# q1. how much maximum swaps are needed to sort array of length 6?

# maximum swap needed when array is reversly sorted


# Return the count of swaps
# def bubble_sort_swap_count(arr):
#     n = len(arr)
#     count = 0

#     for i in range(n - 1):
#         is_sorted = True
#         for j in range(n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 is_sorted = False
#                 count = count + 1
#                 # left is more than right , swap
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#         if is_sorted:
#             break
#     return count


# print(bubble_sort_swap_count([5, 4, 3, 2, 1]))








# q2. sort a string in decreasing order of values associated after removal of values smaller than x

# def sortTheString(str, x):

#   #Create the list
#   my_list  = str.split()

#   n = len(my_list)

#   #Remove the pair whose value is less than given number
#   for i in range(n-1,0,-2):
#     if int(my_list[i])<x:
#       del(my_list[i-1:i+1])

#   n = len(my_list)

#   #Sort the given list of elements

#   for i in range(1,n, 2):
#     for j in range(1,n-i,2):
#       if my_list[j] <my_list[j+2] or (my_list[j-1] < my_list[j+1] and my_list[j] == my_list[j+2] ) :
#         my_list[j], my_list[j+2] = my_list[j+2] , my_list[j]
#         my_list[j-1], my_list[j+1] = my_list[j+1], my_list[j-1]

#   return " ".join(my_list)



# str = "Akshay 43 Vishwa 79 Mohan 83 Nikhil 79 Shivani 43"

# print(sortTheString(str, 50))







# q3. push zeroes to end while maintaining the relative order of other elements

#Pushing all the zeros to the end.

# def push_zeroes_to_end(arr):
#   count = 0 #Count of non-zero elements
#   n = len(arr)
#   temp = [0]*n

#   for i in range(n):
#     if(arr[i]!=0):
#       temp[count] = arr[i]
#       count +=1

#   while(count <n):
#     temp[count] =0
#     count +=1

#   for i in range(n):
#     arr[i] = temp[i]



# arr = [1,2,0,4,3,0,5,0]
# push_zeroes_to_end(arr)
# print(arr)