# Bubble sort code
# 1. compare 2 adjacent elements
# 2. swap if left>right
# 3. Repeat until sorted.


# def bubble_sort(arr):
#     n = len(arr)

#     for i in range(n - 1):
#         for j in range(n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 # left is more than right, so swap
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]

# arr = [5,1,3,4,2]
# print(arr)
# bubble_sort(arr)
# print(arr)




# is it useful in dsa?
# Not much. Bubble Sort is slow (O(n²)) and not used in real-world DSA problems. Use Merge Sort (O(n log n)) or Quick Sort (O(n log n)) instead.