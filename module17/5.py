# Bubble sort code dry run


def bubble_sort(arr):
    n = len(arr)  # n = 5

    for i in range(n - 1): # i = [0,1,2,3] (for first iteration)
        for j in range(n - i - 1): # j = [0,1,2,3] (for first iteration)
            if arr[j] > arr[j + 1]:
                # left is more than right, so swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [5, 1, 3, 4, 2]
print(arr)
bubble_sort(arr)
print(arr)


