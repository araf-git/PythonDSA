# Time and space complexity

# Bubble Sort
# TC = O(n^2)

# even for sorted array, Bubble sort TC = O(n^2). so bubble sort algorithm is bad and people don't use it



def bubble_sort_enhanced(arr):
  n = len(arr)

  for i in range(n-1):
    is_sorted = True
    for j in range(n-i-1):
      if(arr[j]>arr[j+1]):
        is_sorted = False
        #left is more than right , swap
        arr[j],arr[j+1] = arr[j+1],arr[j]
    if is_sorted :
      break

arr =  [ 5,2,1,9,4]
bubble_sort_enhanced(arr)
print(arr)

arr1 = [1,2,3,4,5]
bubble_sort_enhanced(arr1)
print(arr1)

# in the best case TC = O(n) = when it is already sorted
#  bubble sort is an in-place sorting algorithm because it sorts the elements within the array itself without needing extra space.
# The space complexity of bubble sort is O(1), as it only requires a constant amount of extra space.

