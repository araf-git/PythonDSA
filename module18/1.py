# Selection And Insertion Sort


def selectionSort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap
    return arr


print(selectionSort([5, 3, 6, 2, 10]))  # Output: [2, 3, 5, 6, 10]


# Selection Sort finds the minimum and swaps it, while Bubble Sort repeatedly swaps adjacent elements to move the largest to the end.
# Insertion Sort: Inserts each element into its correct position in the sorted part of the array.


# def insertionSort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#     return arr

# print(insertionSort([5, 3, 6, 2, 10]))  # Output: [2, 3, 5, 6, 10]
